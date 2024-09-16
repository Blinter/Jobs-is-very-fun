from app import create_app, db
import time
from sqlalchemy import asc
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import joinedload, load_only
from models.postgres.company import Company
from datetime import datetime
import pytz

from models.postgres.listed_job import ListedJob

app = create_app()

with app.app_context():
    try:
        # Performance check
        full_start_time = time.time()
        start_time = time.time()
        current_utc_time = datetime.now(pytz.utc)
        count = 0
        count_flush = 1000
        for current_company in (db.session.query(Company).options(
                load_only(Company.name),
                load_only(Company.listed_job_count),
                joinedload(Company.listed_jobs)
                .load_only(ListedJob.expiration_time_utc))
                .filter(Company.listed_job_count > 0).all()):
            count += 1
            if count >= count_flush:
                print(f"{count} companies counted, committing. "
                      f" Process Time: "
                      f"{(time.time() - start_time) * 1000:.6g} ms",
                      flush=True)
                count = 0
                start_time = time.time()
                db.session.commit()
            current_expired = (
                sum(1 for job in current_company.listed_jobs
                    if (job.expiration_time_utc is not None and
                        job.expiration_time_utc
                        .replace(tzinfo=pytz.UTC) <=
                        current_utc_time)))
            current_company.expired_listed_job_count = current_expired
            current_company.current_job_count = (
                    current_company.listed_job_count - current_expired)
            current_company.verified = True

        db.session.commit()
        print(f"Process Time: "
              f"{(time.time() - full_start_time) * 1000:.6g} ms", flush=True)

        raise ChildProcessError(
            "Company Jobs Expiration count completed successfully."
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        raise e

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        raise e

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        raise e

    except ChildProcessError as e:
        print(str(e))
        if ('Company Jobs Expiration count completed successfully.'
                not in str(e)):
            db.session.rollback()
        db.session.close()
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e

    finally:
        db.session.close()
