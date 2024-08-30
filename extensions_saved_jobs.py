from flask import session
from sqlalchemy import exists, and_

from extensions_sql import db
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from models.postgres.profile import Profile
from models.postgres.saved_job import SavedJob
from models.postgres.user import User


def check_saved_job_status(job_id: int):
    """
    Check if a Job ID, and a user profile's status exists for a single job.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            not isinstance(session['profile_id'], int)):
        return False

    # Check if User has an active profile.
    if (not session.get('profile_id', False) or
            not isinstance(session['profile_id'], int)):
        return False

    # Check if Job ID is valid
    if (not isinstance(job_id, int) or
            job_id < 0):
        return False

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session['user_id']))).scalar():
            db.session.close()
            return False

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session['user_id']))).scalar():
            db.session.close()
            return False

        # Check that profile is existent in database.
        if not db.session.query(exists().where(
                Profile.id == int(session['profile_id']))).scalar():
            db.session.close()
            return False

        # Check that profile belongs to the user
        if not db.session.query(exists().where(
                and_(
                    Profile.user_id == int(session['user_id']),
                    Profile.id == int(session['profile_id']),
                )
        )).scalar():
            db.session.close()
            return False

        # Check if row exists in the SavedJob table
        if not db.session.query(exists().where(
                and_(
                    SavedJob.user_profile_id == int(session['profile_id']),
                    SavedJob.listed_job_id == int(job_id),
                )
        )).scalar():
            db.session.close()
            return False

        db.session.close()
        return True

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}")

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}")

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}")

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}")
