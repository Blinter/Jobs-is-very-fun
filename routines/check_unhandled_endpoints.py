"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from app import create_app, db
from models.mariadb.api_endpoints import APIEndpoint

app = create_app()

with app.app_context():
    try:
        end_str = []
        endpoint_data = db.session.query(APIEndpoint).all()

        for i in endpoint_data:
            temp_params = i.endpoint_params
            temp_bodies = i.endpoint_bodies
            if len(temp_params) > 0 and len(temp_bodies) > 0:
                print(str(i.nice_name) + " includes both params "
                                         "and bodies.", flush=True)
                end_str.append(i.nice_name)

        print("Endpoints with params and bodies (Check that param should be "
              "only Path param.)", flush=True)

        for i in end_str:
            print(str(i), flush=True)

        db.session.close()
    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        raise e
    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        raise e
    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        raise e
    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e
