
from sqlalchemy import select, asc

from models.mariadb.api_keys import APIKey
from secrets_jobs.credentials import api_jobs_api_keys
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_headers import APIHeader
from models.mariadb.api_endpoints import APIEndpoint
from app import create_app, db

app = create_app()


with app.app_context():
    try:
        apijobdev_s = 'apijobs.dev'
        # retrieve API Endpoints in order to reference API ID.
        api_job_dev_api_list = db.session.query(APIListURL).filter(
            APIListURL.host == apijobdev_s).all()

        # add all APIJob.dev required API key headers
        db.session.add_all([
            APIHeader(
                api_id=i.id,
                header='apikey',
                required=True,
                api_key_header=True,
            ) for i in api_job_dev_api_list
        ])
        db.session.commit()
        print("APIJob.dev header seeded successfully!")

        api_job_dev_api_endpoint_list = [
            db.session.query(APIEndpoint)
            .filter(APIEndpoint.api_id == i.id).first()
            for i in api_job_dev_api_list
        ]

        for j, i in enumerate(api_job_dev_api_endpoint_list):
            if i is None:
                print("INVALID ENDPOINT")
                print(str(i) + " ID: " + str(j))
                raise ValueError("Invalid Endpoint: " + str(i) +
                                 " ID: " + str(j))
            else:
                pass

            # add APIJobs API Keys from credentials file.
            api_jobs_dev_url_list = (db.session.scalars(
                select(APIListURL.url)
                .filter(APIListURL.host == 'apijobs.dev')
                .order_by(asc(APIListURL.nice_name))
            ).all())

            db.session.add_all(
                [APIKey(
                    url=i,
                    key=j['key'],
                    preferred_proxy=(
                        j['preferred_proxy'] if 'preferred_proxy' in
                                                j.keys() else None)
                )
                    for j in api_jobs_api_keys
                    for i in api_jobs_dev_url_list
                ]
            )

            db.session.commit()

            print(APIKey.__tablename__ + " API Jobs seeded successfully!")

        db.session.add_all([
            APIHeader(
                api_id=i.id,
                header='Accept',
                value='application/json',
                required=True,
            ) for (i, j) in zip(
                api_job_dev_api_list,
                api_job_dev_api_endpoint_list
            )
        ])
        db.session.commit()
        print("API Job Headers seeded successfully!")

        db.session.close()
        print(APIHeader.__tablename__ + " seeded successfully!")

    except Exception as e:
        print(f"Error committing data: {e}")
        raise e
