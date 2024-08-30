from flask import session
from models.postgres.user import User
from models.postgres.profile import Profile
from sqlalchemy import exists, and_
from extensions_sql import db
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError


def user_check_set_active_profile():
    """
    Access profiles database for the logged-in user and set the active profile
    based on the database.
    Does not close the session
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            return

        # Check if any profile exists for the user.
        if not db.session.query(exists().where(
                Profile.user_id == int(session['user_id']))).scalar():
            return

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        # Only called if profile is active on the session but not in the
        # database.
        if (session.get('profile_id') is not None and
                db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False),
                ))).scalar()):

            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                # Remove the profile from the session if profile ID doesn't
                # belong to the user.
                if session.get('profile_id') is not None:
                    session.pop('profile_id', None)
                return
            # Update all other user profiles and deactivate once this change is
            # reflected.
            print(selected_profile)
            print(isinstance(selected_profile, list))

            selected_profile.active = True
            selected_profile.verified = True

            db.session.query(Profile).filter(
                and_(
                    Profile.user_id == int(session['user_id']),
                    Profile.id != int(selected_profile.id),
                )
            ).update({'active': False})

            db.session.commit()
            return

        # Check if the database has an active profile set for the user,
        # Apply it to the user's session if it has not yet been set.
        elif (session.get('profile_id') is None and
              db.session.query(exists().where(
                  and_(
                      Profile.user_id == int(session['user_id']),
                      Profile.active.is_(True),
                  ))).scalar()):
            selected_profile = (
                db.session.query(Profile).filter(
                    and_(
                        Profile.user_id == int(session['user_id']),
                        Profile.active.is_(True),
                    )).first())
            # Check that profile user ID belongs to the current user and is
            # not None.

            if selected_profile is not None:
                session['profile_id'] = int(selected_profile.id)
            return

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        # raise e

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        # raise e

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        # raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        # raise e
