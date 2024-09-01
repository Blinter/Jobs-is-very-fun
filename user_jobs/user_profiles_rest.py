import urllib.parse

from flask import (
    Blueprint,
    session,
    request,
    jsonify,
    make_response
)
from psycopg2 import IntegrityError, OperationalError
from sqlalchemy import exists, and_, asc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.functions import count

from enums.response_codes import ResponseCodesGeneric
from extensions_sql import db
from models.postgres.user import User
from models.postgres.profile import Profile
from models.postgres.saved_job import SavedJob
from models.postgres.saved_company import SavedCompany

from user_jobs.user_limits import maximum_user_profiles

user_profiles_rest_bp = Blueprint(
    'user_profiles_rest',
    __name__
)


@user_profiles_rest_bp.route(
    "/create_profile_name/<string:new_name>",
    methods=["PUT"]
)
def user_create_profile_name(new_name):
    """
    REST API
    Create a User Profile with a name
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Profile created has content.
    if (not isinstance(new_name, str) or
            len(new_name) == 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks
        if isinstance(new_name, str):
            new_name = urllib.parse.unquote(new_name)

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session['user_id']))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has a profile that exists for their input
        if db.session.query(exists().where(
                and_(
                    Profile.user_id == int(session['user_id']),
                    Profile.name == str(new_name),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.CONFLICT))

        # Check if user has created too many profiles
        if (db.session.query(count(Profile.user_id)).filter(
                Profile.user_id == int(session['user_id'])
        ).scalar() >= maximum_user_profiles):
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.IM_USED))

        # Create the new profile
        new_profile = Profile(
            name=str(new_name),
            user_id=int(session.get('user_id')),
            active=False,
        )

        # Add the new profile to session
        db.session.add(new_profile)

        # Commit to the database
        db.session.commit()

        # Return new ID and successful response upon creation
        return (jsonify([new_profile.to_dict_rest()]),
                int(ResponseCodesGeneric.OK))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@user_profiles_rest_bp.route(
    "/create_profile",
    methods=["POST"]
)
def user_create_profile():
    """
    REST API
    Create a User Profile with no name
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check that user has not reached their limit for profiles.
        if (db.session.query(count(Profile.user_id)).filter(
                Profile.user_id == int(session.get('user_id'))
        ).scalar() >= maximum_user_profiles):
            db.session.close()
            return make_response('', int(
                ResponseCodesGeneric.IM_USED))

        # Create the new profile
        new_profile = Profile(
            user_id=int(session.get('user_id')),
            active=False,
        )

        # Add the new profile to session
        db.session.add(new_profile)

        # Commit to the database
        db.session.commit()

        # Return new ID and successful upon creation
        return (jsonify([new_profile.to_dict_rest()]),
                int(ResponseCodesGeneric.OK))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@user_profiles_rest_bp.route(
    "/delete_profile_id/<int:existing_id>",
    methods=["DELETE"]
)
def user_delete_profile_id(existing_id):
    """
    REST API
    Delete a User Profile based on a Profile ID
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Profile ID value provided has content.
    if (existing_id is None or
            not isinstance(existing_id, int) or
            int(existing_id) < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile ID exists.
        if not db.session.query(exists().where(
                Profile.id == int(existing_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if user has a profile
        if not db.session.query(exists().where(
                Profile.user_id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if profile ID belongs to user.
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(existing_id),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Remove the profile from the session if it is set as the active
        # Profile.
        if (session.get('profile_id') is not None and
                session.get('profile_id') == int(existing_id)):
            session.pop('profile_id', None)

        # Delete the profile
        db.session.delete(
            db.session.query(Profile)
            .filter_by(id=int(existing_id)).first())

        # Commit to the database
        db.session.commit()
        db.session.close()

        # Return successful upon deletion
        return make_response('', int(ResponseCodesGeneric.OK))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@user_profiles_rest_bp.route(
    "/delete_profile_name/<string:profile_name>",
    methods=["DELETE"]
)
def user_delete_profile_name(profile_name):
    """
    REST API
    Delete a User Profile based on a Profile Name
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Profile created has content.
    if (not isinstance(profile_name, str) or
            len(profile_name) == 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Database methods are enclosed in a try-except block.
    try:
        if isinstance(profile_name, str):
            profile_name = urllib.parse.unquote(profile_name)
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has a profile that exists for their input.
        if not db.session.query(exists().where(
                and_(
                    Profile.user_id == int(session.get('user_id')),
                    Profile.name == str(profile_name)
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if profile Name belongs to user.
        if not db.session.query(exists().where(
                and_(
                    Profile.name == str(profile_name),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Delete the profile
        db.session.delete(
            db.session.query(Profile).filter(
                and_(
                    Profile.user_id == int(session.get('user_id')),
                    Profile.name == str(profile_name)
                )
            ).first()
        )

        # Commit to the database
        db.session.commit()
        db.session.close()

        # Return successful upon deletion
        return make_response('', int(ResponseCodesGeneric.OK))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@user_profiles_rest_bp.route(
    "/change_profile_name_id/<int:existing_id>",
    methods=["PATCH"]
)
def user_change_profile_name_id(existing_id):
    """
    REST API
    Change a profile name based on ID
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if input profile has content.
    if existing_id is None:
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Set the new name as a temp variable for convenience.
    try:
        temp_new_name = request.json.get('new_name', None)
        if isinstance(temp_new_name, str):
            temp_new_name = urllib.parse.unquote(temp_new_name)

    except Exception as e:
        print(str(e))
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new name has an input.
    if (not isinstance(temp_new_name, str) or
            len(temp_new_name) == 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if profile ID exists.
        if not db.session.query(exists().where(
                Profile.id == int(existing_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if profile ID belongs to user.
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(existing_id),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if new profile name were to conflict with another name.
        if db.session.query(exists().where(
                and_(
                    Profile.id != int(existing_id),
                    Profile.user_id == int(session.get('user_id')),
                    Profile.name == str(temp_new_name)
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.CONFLICT))

        # Check if new profile name is the same as the existing name.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(existing_id),
                    Profile.user_id == int(session.get('user_id')),
                    Profile.name == str(temp_new_name)
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_MODIFIED))

        # Update the existing profile
        (db.session.query(Profile)
         .filter_by(id=int(existing_id))
         .update({'name': temp_new_name}))

        # Commit to the database
        db.session.commit()
        db.session.close()

        # Return successful upon profile name change
        return make_response('', int(ResponseCodesGeneric.RESET_CONTENT))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@user_profiles_rest_bp.route(
    "/change_profile_name/<string:existing_name>",
    methods=["PATCH"]
)
def user_change_profile_name(existing_name):
    """
    REST API
    Change a profile name based on existing name
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Profile created has content.
    if existing_name is None:
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Set the new name as a temp variable for convenience.
    try:
        temp_new_name = request.json.get('new_name', None)
    except Exception as e:
        print(str(e))
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new name has an input.
    if (not isinstance(temp_new_name, str) or
            len(temp_new_name) == 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new name is not equal to existing name.
    if temp_new_name == existing_name:
        return make_response('', int(ResponseCodesGeneric.NOT_ACCEPTABLE))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if profile name belongs to the user.
        if not db.session.query(exists().where(
                and_(
                    Profile.name == str(existing_name),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if new profile name were to conflict with another name.

        # Get current Profile ID for the current name being changed.
        current_profile_id = db.session.query(Profile.id).filter(
            and_(
                Profile.user_id == int(session.get('user_id')),
                Profile.name == str(existing_name)
            )
        ).first()

        # Check for existing profile name if isn't the current profile ID.
        if db.session.query(exists().where(
                and_(
                    Profile.id != int(current_profile_id),
                    Profile.user_id == int(session.get('user_id')),
                    Profile.name == str(temp_new_name)
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.CONFLICT))

        # Update the existing profile
        db.session.query(Profile).filter(
            and_(
                Profile.user_id == int(session.get('user_id')),
                Profile.name == str(existing_name),
            )
        ).update({'name': temp_new_name})

        # Commit to the database
        db.session.commit()
        db.session.close()

        # Return successful upon successful change
        return make_response('', int(ResponseCodesGeneric.RESET_CONTENT))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@user_profiles_rest_bp.route(
    "/get_profile_id/<string:existing_name>",
    methods=["GET"]
)
def user_get_profile_id(existing_name):
    """
    REST API
    Get a specific profile name.
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Profile name queried has content.
    if existing_name is None:
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    if isinstance(existing_name, str):
        existing_name = urllib.parse.unquote(existing_name)

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Check if profile name exists and belongs to the user.
        if not db.session.query(exists().where(
                and_(
                    Profile.name == str(existing_name),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Retrieve the existing profile
        existing_profile_id = db.session.query(Profile.id).filter(
            and_(
                Profile.user_id == int(session.get('user_id')),
                Profile.name == str(existing_name)
            )
        ).first()

        # Return successful upon creation
        return (jsonify({'id': existing_profile_id[0]}),
                int(ResponseCodesGeneric.OK))

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


@user_profiles_rest_bp.route(
    "/get_profile_name/<int:existing_profile_id>",
    methods=["GET"]
)
def user_get_profile_name(existing_profile_id):
    """
    REST API
    Get a specific profile name for an ID.
    Return Status Code for outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Profile ID queried has content.
    if existing_profile_id is None:
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Check if profile exists
        if not db.session.query(exists().where(
                Profile.id == int(existing_profile_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Check if profile ID belongs to the user.
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(existing_profile_id),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Retrieve the existing profile name
        existing_profile_name = db.session.query(Profile.name).filter(
            and_(
                Profile.user_id == int(session.get('user_id')),
                Profile.id == int(existing_profile_id)
            )
        ).first()

        # Return successful upon creation
        return (jsonify({'name': existing_profile_name[0]}),
                int(ResponseCodesGeneric.OK))

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


@user_profiles_rest_bp.route(
    "/get_profiles",
    methods=["GET"]
)
def user_get_profiles():
    """
    REST API
    Retrieve user profiles data and send to client
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session['user_id']))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session['user_id']))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Retrieve the profiles
        # Convert to dictionary
        existing_profiles = [
            i.to_dict_rest()
            for i in (
                db.session.query(Profile)
                .filter_by(user_id=int(session['user_id']))
                .order_by(asc(Profile.id))
                .all()
            )
        ]
        # Return successful upon creation
        return jsonify(existing_profiles), int(ResponseCodesGeneric.OK)

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


@user_profiles_rest_bp.route(
    "/get_profile_status/<int:profile_id>",
    methods=["GET"]
)
def user_get_profile_status(profile_id):
    """
    REST API
    Get the active status for a profile ID
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if not isinstance(profile_id, int) or profile_id < 0:
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session['user_id']))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session['user_id']))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Check that profile is existent in database.
        if not db.session.query(exists().where(
                Profile.id == int(profile_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check that profile belongs to the user
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session['user_id'])
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        status = db.session.query(exists().where(
            and_(
                Profile.id == int(profile_id),
                Profile.user_id == int(session['user_id']),
                Profile.active.is_(True),
            )
        )).scalar()
        db.session.close()

        # Return profile status
        return make_response(jsonify(status), int(ResponseCodesGeneric.OK))

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


@user_profiles_rest_bp.route(
    "/get_job_status/<int:job_id>",
    methods=["GET"]
)
def user_get_job_save_status(job_id: int):
    """
    REST API
    Get the status of a job ID if it is saved to their active profile.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if User has an active profile.
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    if not isinstance(job_id, int) or job_id < 0:
        return make_response('', int(
            ResponseCodesGeneric.BAD_REQUEST))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session['user_id'])
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session['user_id'])
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Check that profile is existent in database.
        if not db.session.query(exists().where(
                Profile.id == int(session['profile_id'])
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check that profile belongs to the user
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id'])
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        status = db.session.query(exists().where(
            and_(
                SavedJob.listed_job_id == int(job_id),
                SavedJob.user_profile_id == int(session['profile_id']),
            )
        )).scalar()
        db.session.close()

        # Return profile status
        return make_response(jsonify(status), int(ResponseCodesGeneric.OK))

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


@user_profiles_rest_bp.route(
    "/toggle_profile/<int:active>",
    methods=["PATCH"]
)
def user_toggle_active_profile(active: int):
    """
    REST API
    Change a profile's status based on profile ID or profile name
    Return Status Code for outcome.

    Path: 0 or 1 for active
    profile_name: Body param
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if active value supplied by user is valid
    if (not isinstance(active, int) or
            (active != 0 and
             active != 1)):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Set the profile ID or name as a temp variable for convenience.
    try:
        temp_profile_name = request.json.get('profile_name', None)
        if isinstance(temp_profile_name, str):
            temp_profile_name = urllib.parse.unquote(temp_profile_name)

        temp_profile_id = request.json.get('profile_id', None)

        # print(str(temp_profile_id) + ", " +
        #       temp_profile_name + ", " +
        #       str(active))
    except Exception as e:
        print(str(e))
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that name or ID has an input.
    if (temp_profile_name is None and
            temp_profile_id is None):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Convert profile ID to int if it was passed as a string and catch error
    if (temp_profile_id is not None and
            not isinstance(temp_profile_id, int)):
        try:
            temp_profile_id = int(temp_profile_id)
        except Exception as e:
            print(str(e))
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Database methods are enclosed in a try-except block.
    try:
        # Database Checks

        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session['user_id'])
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if user has profiles
        if not db.session.query(exists().where(
                Profile.user_id == int(session['user_id'])
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Accept profile ID or profile name, or both, with preference to ID.
        if temp_profile_id is not None:
            # Start with Profile ID (int)

            # Check if profile ID belongs to the user.
            if not db.session.query(exists().where(
                and_(
                    Profile.id == int(temp_profile_id),
                    Profile.user_id == int(session['user_id']),
                )
            )).scalar():
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            # Get current Profile ID using the user provided Profile ID.
            current_profile_id = db.session.query(Profile.id).filter(
                and_(
                    Profile.user_id == int(session['user_id']),
                    Profile.id == int(temp_profile_id)
                )
            ).first()[0]

        else:
            # Check if profile name belongs to the user.
            if not db.session.query(exists().where(
                    and_(
                        Profile.name == str(temp_profile_name),
                        Profile.user_id == int(session['user_id']),
                    )
            )).scalar():
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            # Get current Profile ID using the user provided Profile name.
            current_profile_id = db.session.query(Profile.id).filter(
                and_(
                    Profile.user_id == int(session['user_id']),
                    Profile.name == str(temp_profile_name)
                )
            ).first()[0]

        # Check if profile status were to conflict. (i.e. two active profiles)
        # Check for existing active profile for the user if the active status
        # was set to 1.
        if active == 1:
            if db.session.query(exists().where(
                    and_(
                        Profile.id != int(current_profile_id),
                        Profile.user_id == int(session['user_id']),
                        Profile.active.is_(True),
                    )
            )).scalar():
                # Then set them to inactive.
                db.session.query(Profile).filter(
                    and_(
                        Profile.user_id == int(session['user_id']),
                        Profile.id != int(current_profile_id),
                    )
                ).update({'active': False})

            db.session.query(Profile).filter(
                and_(
                    Profile.id == int(current_profile_id),
                    Profile.user_id == int(session['user_id'])
                )
            ).update({'active': True})
            db.session.flush()

            print("Setting user's profile ID to " + str(current_profile_id))
            session['profile_id'] = int(current_profile_id)

        elif active == 0:
            # Deactivate the selected Profile ID for the user.
            db.session.query(Profile).filter(
                and_(
                    Profile.user_id == int(session['user_id']),
                    Profile.id == int(current_profile_id),
                )
            ).update({'active': False})
            db.session.flush()

            if session.get('profile_id') is not None:
                session.pop('profile_id', None)

        # Commit to the database
        db.session.commit()
        db.session.close()

        # Return successful upon successful change
        return make_response('', int(ResponseCodesGeneric.RESET_CONTENT))

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))
