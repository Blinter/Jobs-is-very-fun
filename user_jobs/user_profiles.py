from flask import (
    Blueprint,
    session,
    make_response,
    redirect,
    url_for,
    flash,
    render_template
)

from psycopg2 import IntegrityError, OperationalError
from sqlalchemy import exists, and_
from sqlalchemy.exc import SQLAlchemyError

from enums.response_codes import ResponseCodesGeneric
from extensions_sql import db
from extensions_user import get_authenticated_user_name
from models.postgres.user import User
from models.postgres.profile import Profile

from user_jobs.users_jobs import logout

user_profiles_bp = Blueprint(
    'user_profiles',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/user_profiles'
)


@user_profiles_bp.route(
    "/profile/<int:profile_id>",
    methods=["GET"]
)
def view_user_profile(profile_id):
    """
    Provides information to the user about the profile that was selected. (GET)
    Send data back to the user and uses a jinja template to display details.
    """
    # Check if User is logged in.
    if not session.get('user_id', False):
        flash("Sorry, you cannot access this page since you are not "
              "logged in.", 'danger')
        return redirect(url_for('general.home'))

    # Check if Profile ID has content.
    if profile_id is None:
        flash("Sorry, you didn't select a profile to view.", 'danger')
        return redirect(url_for('user.user_dashboard'))
        # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            # Clear session state by logging them out.
            logout()
            flash("Sorry, your user ID is not found in our database.", 'danger')
            return redirect(url_for('general.home'))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session.get('user_id')))).scalar():
            db.session.close()
            flash("Sorry, you have no profiles that can be viewed.", 'danger')
            return redirect(url_for('user.user_dashboard'))

        # Check if profile name exists and belongs to the user.
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            flash("Sorry, you cannot view this profile.", 'danger')
            return redirect(url_for('user.user_dashboard'))

        # Retrieve the existing profile
        retrieved_profile = db.session.query(Profile).filter(
            and_(
                Profile.id == int(profile_id),
                Profile.user_id == int(session.get('user_id'))
            )
        ).first()

        # result = retrieved_profile.to_dict_jinja()
        # print(result)

        # render template with retrieved data upon creation
        return render_template(
            'profile/profile_dashboard.html',
            profile=retrieved_profile.to_dict_jinja(),
            user=get_authenticated_user_name(),
            email=session.get('email', None)
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))
