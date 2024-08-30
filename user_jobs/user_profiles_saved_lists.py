from flask import (
    Blueprint,
    session,
    make_response,
    jsonify, request
)
from psycopg2 import IntegrityError, OperationalError
from sqlalchemy import exists, and_, asc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.functions import count

from enums.response_codes import ResponseCodesGeneric
from extensions_sql import db
from models.postgres.company import Company
from models.postgres.listed_job import ListedJob
from models.postgres.saved_company import SavedCompany
from models.postgres.saved_job import SavedJob
from models.postgres.user import User
from models.postgres.profile import Profile

from user_jobs.user_limits import (
    maximum_user_saved_jobs,
    maximum_user_saved_companies
)

user_profiles_saved_lists_rest_bp = Blueprint(
    'user_profiles_saved_lists_rest',
    __name__
)


@user_profiles_saved_lists_rest_bp.route(
    "/retrieve_saved_data_complete_profile/<int:profile_id>",
    methods=["GET"]
)
def user_retrieve_saved_data_complete_profile_select(profile_id):
    """
    REST API
    Load all saved data (jobs and companies)
    for the current user's specific profile ID
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check profile_id is a valid integer
    if (not isinstance(profile_id, int) or
            profile_id < 0):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on request
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        selected_jobs = (
            db.session.query(SavedJob)
            .filter(SavedJob.user_profile_id ==
                    int(profile_id))
            .all()
        )

        selected_companies = (
            db.session.query(SavedCompany)
            .filter(SavedCompany.user_profile_id ==
                    int(profile_id))
            .all()
        )

        selected_data = (
            (
                [i.to_dict_rest_complete()
                    for i in selected_jobs],
                [i.to_dict_rest_complete()
                    for i in selected_companies]
            )
        )
        db.session.close()

        # Return successful status code upon creation.
        return make_response(
            jsonify(selected_data),
            int(ResponseCodesGeneric.OK)
        )

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


@user_profiles_saved_lists_rest_bp.route(
    "/retrieve_saved_data_complete",
    methods=["GET"]
)
def user_retrieve_saved_data_complete():
    """
    REST API
    Load all saved data (jobs and companies)
    for the current user's active profile ID
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False),
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        selected_jobs = (
            db.session.query(SavedJob)
            .filter(SavedJob.user_profile_id ==
                    int(session['profile_id']))
            .all()
        )

        selected_companies = (
            db.session.query(SavedCompany)
            .filter(SavedCompany.user_profile_id ==
                    int(session['profile_id']))
            .all()
        )

        selected_data = (
            (
                [i.to_dict_rest_complete()
                    for i in selected_jobs],
                [i.to_dict_rest_complete()
                    for i in selected_companies]
            )
        )
        db.session.close()

        # Return successful status code upon creation.
        return make_response(
            jsonify(selected_data),
            int(ResponseCodesGeneric.OK)
        )

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


@user_profiles_saved_lists_rest_bp.route(
    "/retrieve_saved_data",
    methods=["GET"]
)
def user_retrieve_saved_data():
    """
    REST API
    Load ID's of saved data (jobs and companies)
    for the current user's active profile ID
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False),
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        # Two separate queries utilizing hash map indexes on both tables
        # Client will sort data after receiving it.
        selected_data = (
            ([i[0] for i in db.session.query(SavedJob.listed_job_id)
              .filter(SavedJob.user_profile_id == int(session['profile_id']))
              # .order_by(
              #   asc(SavedJob.list_name),
              #   asc(SavedJob.order),
              # )
              .all()],
             [i[0] for i in db.session.query(SavedCompany.company_id)
              .filter(
                 SavedCompany.user_profile_id == int(session['profile_id']))
              # .order_by(
              #    asc(SavedCompany.list_name),
              #    asc(SavedCompany.order)
              # )
              .all()])
        )
        db.session.close()

        # Return successful status code upon creation.
        return make_response(
            jsonify(selected_data),
            int(ResponseCodesGeneric.OK)
        )

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


@user_profiles_saved_lists_rest_bp.route(
    "/retrieve_saved_jobs",
    methods=["GET"]
)
def user_retrieve_saved_jobs():
    """
    REST API
    Load all saved jobs (ID's) for the current user and active profile ID
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id'])
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False),
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        # select all jobs

        selected_jobs = [
            i[0] for i in db.session.query(SavedJob.listed_job_id)
            .filter(SavedJob.user_profile_id == int(session['profile_id']))
            .all()
        ]
        db.session.close()

        # Return successful status code upon creation.
        return make_response(
            jsonify(selected_jobs),
            int(ResponseCodesGeneric.OK)
        )

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


@user_profiles_saved_lists_rest_bp.route(
    "/retrieve_saved_companies",
    methods=["GET"]
)
def user_retrieve_saved_companies():
    """
    REST API
    Load all saved companies (ID's) for the current user and active profile ID
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False),
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        # select all jobs

        selected_companies = [
            i[0] for i in db.session.query(SavedCompany.company_id)
            .filter(SavedCompany.user_profile_id == int(session['profile_id']))
            .all()
        ]
        db.session.close()

        # Return successful status code upon creation.
        return make_response(
            jsonify(selected_companies),
            int(ResponseCodesGeneric.OK)
        )

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


@user_profiles_saved_lists_rest_bp.route(
    "/save_job/<int:profile_id>/<int:job_id>",
    methods=["PUT"]
)
def user_add_saved_job(profile_id: int, job_id: int):
    """
    REST API
    Save a job to a specified user's profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Job is a valid ID
    if (not isinstance(job_id, int) or
            job_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if Profile is a valid number
    if (not isinstance(profile_id, int) or
            profile_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if profile has saved too many Profile jobs
        if (db.session.query(count(SavedJob.user_profile_id)).filter(
                SavedJob.user_profile_id == int(profile_id)
        ).scalar() >= maximum_user_saved_jobs):
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.IM_USED))

        # Check if job ID exists in the ListedJob Database
        if not db.session.query(exists().where(
                ListedJob.id == int(job_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if job ID already exists in the Saved Job List
        if db.session.query(exists().where(
                and_(
                    SavedJob.user_profile_id == int(profile_id),
                    SavedJob.listed_job_id == int(job_id),
                )
        )).scalar():
            db.session.close()
            # return make_response(
            #     '', int(ResponseCodesGeneric.ALREADY_REPORTED))
            # Already there, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # print("Attempting to add saved job to profile " +
        #       str(session['profile_id']))
        new_saved_job = SavedJob(
            user_profile_id=int(profile_id),
            listed_job_id=int(job_id),
        )

        db.session.add(new_saved_job)
        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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


@user_profiles_saved_lists_rest_bp.route(
    "/save_company/<int:profile_id>/<int:company_id>",
    methods=["PUT"]
)
def user_add_saved_company(profile_id: int, company_id: int):
    """
    REST API
    Save a company to the specified profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Company is a valid ID
    if (not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if Profile is a valid number
    if (not isinstance(profile_id, int) or
            profile_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if profile has saved too many Profile companies
        if (db.session.query(count(SavedCompany.user_profile_id)).filter(
                SavedCompany.user_profile_id == int(profile_id)
        ).scalar() >= maximum_user_saved_companies):
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.IM_USED))

        # Check if company ID exists in the Company Database
        if not db.session.query(exists().where(
                Company.id == int(company_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if company ID already exists in the Saved Company List
        if db.session.query(exists().where(
                and_(
                    SavedCompany.user_profile_id == int(profile_id),
                    SavedCompany.company_id == int(company_id),
                )
        )).scalar():
            db.session.close()
            # return make_response(
            #     '', int(ResponseCodesGeneric.ALREADY_REPORTED))
            # Already there, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # print("Attempting to add saved company to profile " +
        #       str(session['profile_id']))
        new_saved_company = SavedCompany(
            user_profile_id=int(profile_id),
            company_id=int(company_id),
        )

        db.session.add(new_saved_company)
        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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


@user_profiles_saved_lists_rest_bp.route(
    "/unsave_job/<int:profile_id>/<int:job_id>",
    methods=["DELETE"]
)
def user_unsave_job(profile_id: int, job_id: int):
    """
    REST API
    Remove a saved job from the specified profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Job is a valid ID
    if (not isinstance(job_id, int) or
            job_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if Profile is a valid ID
    if (not isinstance(profile_id, int) or
            profile_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if job ID exists in the ListedJob Database
        if not db.session.query(exists().where(
                ListedJob.id == int(job_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if job ID does not exist in the Saved Job List for the profile
        if not db.session.query(exists().where(
                and_(
                    SavedJob.user_profile_id == int(profile_id),
                    SavedJob.listed_job_id == int(job_id),
                )
        )).scalar():
            db.session.close()
            # return make_response('', int(ResponseCodesGeneric.NOT_FOUND))
            # Already gone, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # Checks completed
        # Delete the row
        db.session.query(SavedJob).filter(
            and_(
                SavedJob.user_profile_id == int(profile_id),
                SavedJob.listed_job_id == int(job_id),
            )
        ).delete()

        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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


@user_profiles_saved_lists_rest_bp.route(
    "/unsave_company/<int:profile_id>/<int:company_id>",
    methods=["DELETE"]
)
def user_unsave_company(profile_id: int, company_id: int):
    """
    REST API
    Remove a saved company from a specific profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Company is a valid ID
    if (not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if Profile is a valid ID
    if (not isinstance(profile_id, int) or
            profile_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if company ID exists in the Company Database
        if not db.session.query(exists().where(
                Company.id == int(company_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if company ID does not exist in the
        # Saved Company List for the profile
        if not db.session.query(exists().where(
                and_(
                    SavedCompany.user_profile_id == int(profile_id),
                    SavedCompany.company_id == int(company_id),
                )
        )).scalar():
            db.session.close()
            # return make_response('', int(ResponseCodesGeneric.NOT_FOUND))
            # Already gone, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # Checks completed
        # Delete the row
        db.session.query(SavedCompany).filter(
            and_(
                SavedCompany.user_profile_id == int(profile_id),
                SavedCompany.company_id == int(company_id),
            )
        ).delete()

        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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


@user_profiles_saved_lists_rest_bp.route(
    "/update_saved_job/<int:profile_id>/<int:job_id>",
    methods=["PATCH"]
)
def user_profile_update_saved_job(profile_id: int, job_id: int):
    """
    REST API
    Update a saved job for a specific profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if input Profile ID and Job ID has content.
    if (not isinstance(profile_id, int) or
            profile_id < 0 or
            not isinstance(job_id, int) or
            job_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Set the new name as a temp variable for convenience.
    try:
        temp_list_name = request.json.get('listName', None)
        if (temp_list_name is not None and
                temp_list_name == ""):
            temp_list_name = None

        temp_order = request.json.get('order', None)
        if temp_order is not None:
            if temp_order == "":
                temp_order = None
            else:
                temp_order = int(temp_order)

        temp_notes = request.json.get('notes', None)
        if (temp_notes is not None and
                temp_notes == ""):
            temp_notes = None
    except Exception as e:
        print(str(e))
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new list name has an input.
    if (temp_list_name is not None and
            not isinstance(temp_list_name, str)):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new temp order has an input.
    if (temp_order is not None and
            not isinstance(temp_order, int)):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new temp notes has an input.
    if (temp_notes is not None and
            not isinstance(temp_notes, str)):
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
                Profile.id == int(profile_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if profile ID belongs to user.
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Update the existing SavedJob
        selected_saved_job: SavedJob = (
            db.session.query(SavedJob)
            .filter(
                and_(
                    SavedJob.user_profile_id == int(profile_id),
                    SavedJob.listed_job_id == int(job_id),
                )
            ).first()
        )
        if (selected_saved_job.list_name != temp_list_name or
                selected_saved_job.order != temp_order or
                selected_saved_job.notes != temp_notes):
            selected_saved_job.verified = True
        else:
            db.session.close()
            # Return successful upon profile name change
            return make_response('', int(ResponseCodesGeneric.NOT_MODIFIED))

        if selected_saved_job.list_name != temp_list_name:
            selected_saved_job.list_name = temp_list_name

        if selected_saved_job.order != temp_order:
            selected_saved_job.order = temp_order

        if selected_saved_job.notes != temp_notes:
            selected_saved_job.notes = temp_notes

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


@user_profiles_saved_lists_rest_bp.route(
    "/update_saved_company/<int:profile_id>/<int:company_id>",
    methods=["PATCH"]
)
def user_profile_update_saved_company(profile_id: int, company_id: int):
    """
    REST API
    Update a saved company for a specific profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if input Profile ID and Company ID has content.
    if (not isinstance(profile_id, int) or
            profile_id < 0 or
            not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Set the new name as a temp variable for convenience.
    try:
        temp_list_name = request.json.get('listName', None)
        if (temp_list_name is not None and
                temp_list_name == ""):
            temp_list_name = None

        temp_order = request.json.get('order', None)
        if temp_order is not None:
            if temp_order == "":
                temp_order = None
            else:
                temp_order = int(temp_order)

        temp_notes = request.json.get('notes', None)
        if (temp_notes is not None and
                temp_notes == ""):
            temp_notes = None
    except Exception as e:
        print(str(e))
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new list name has an input.
    if (temp_list_name is not None and
            not isinstance(temp_list_name, str)):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new temp order has an input.
    if (temp_order is not None and
            not isinstance(temp_order, int)):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check that new temp notes has an input.
    if (temp_notes is not None and
            not isinstance(temp_notes, str)):
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
                Profile.id == int(profile_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.NOT_FOUND))

        # Check if profile ID belongs to user.
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(profile_id),
                    Profile.user_id == int(session.get('user_id'))
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Update the existing SavedCompany
        selected_saved_company: SavedCompany = (
            db.session.query(SavedCompany)
            .filter(
                and_(
                    SavedCompany.user_profile_id == int(profile_id),
                    SavedCompany.company_id == int(company_id),
                )
            ).first()
        )
        if (selected_saved_company.list_name != temp_list_name or
                selected_saved_company.order != temp_order or
                selected_saved_company.notes != temp_notes):
            selected_saved_company.verified = True
        else:
            db.session.close()
            # Return successful upon profile name change
            return make_response('', int(ResponseCodesGeneric.NOT_MODIFIED))

        if selected_saved_company.list_name != temp_list_name:
            selected_saved_company.list_name = temp_list_name

        if selected_saved_company.order != temp_order:
            selected_saved_company.order = temp_order

        if selected_saved_company.notes != temp_notes:
            selected_saved_company.notes = temp_notes

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


@user_profiles_saved_lists_rest_bp.route(
    "/save_job_active/<int:job_id>",
    methods=["PUT"]
)
def user_add_saved_job_active(job_id: int):
    """
    REST API
    Save a job to the active user's profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Job is a valid ID
    if (job_id is None or
            job_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response(
                'Check if profile exists and belongs to user',
                int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False),
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        # Check if profile has saved too many Profile jobs
        if (db.session.query(count(SavedJob.user_profile_id)).filter(
                SavedJob.user_profile_id == int(session['profile_id'])
        ).scalar() >= maximum_user_saved_jobs):
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.IM_USED))

        # Check if job ID exists in the ListedJob Database
        if not db.session.query(exists().where(
                ListedJob.id == int(job_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if job ID already exists in the Saved Job List
        if db.session.query(exists().where(
                and_(
                    SavedJob.user_profile_id == int(session['profile_id']),
                    SavedJob.listed_job_id == int(job_id),
                )
        )).scalar():
            db.session.close()
            # return make_response(
            #     '', int(ResponseCodesGeneric.ALREADY_REPORTED))
            # Already there, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # print("Attempting to add saved job to profile " +
        #       str(session['profile_id']))
        new_saved_job = SavedJob(
            user_profile_id=session['profile_id'],
            listed_job_id=int(job_id),
        )

        db.session.add(new_saved_job)
        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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


@user_profiles_saved_lists_rest_bp.route(
    "/save_company_active/<int:company_id>",
    methods=["PUT"]
)
def user_add_saved_company_active(company_id: int):
    """
    REST API
    Save a company to the active user's profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Company is a valid ID
    if (company_id is None or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False),
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        # Check if profile has saved too many Profile companies
        if (db.session.query(count(SavedCompany.user_profile_id)).filter(
                SavedCompany.user_profile_id == int(session['profile_id'])
        ).scalar() >= maximum_user_saved_companies):
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.IM_USED))

        # Check if company ID exists in the Company Database
        if not db.session.query(exists().where(
                Company.id == int(company_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if company ID already exists in the Saved Company List
        if db.session.query(exists().where(
                and_(
                    SavedCompany.user_profile_id == int(session['profile_id']),
                    SavedCompany.company_id == int(company_id),
                )
        )).scalar():
            db.session.close()
            # return make_response(
            #     '', int(ResponseCodesGeneric.ALREADY_REPORTED))
            # Already there, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # print("Attempting to add saved company to profile " +
        #       str(session['profile_id']))
        new_saved_company = SavedCompany(
            user_profile_id=session['profile_id'],
            company_id=int(company_id),
        )

        db.session.add(new_saved_company)
        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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


@user_profiles_saved_lists_rest_bp.route(
    "/unsave_job_active/<int:job_id>",
    methods=["DELETE"]
)
def user_unsave_job_active(job_id: int):
    """
    REST API
    Remove a job from the active user's profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Job is a valid ID
    if (not isinstance(job_id, int) or
            job_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False)
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))
            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        # Check if job ID exists in the ListedJob Database
        if not db.session.query(exists().where(
                ListedJob.id == int(job_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if job ID does not exist in the Saved Job List for the profile
        if not db.session.query(exists().where(
                and_(
                    SavedJob.user_profile_id == int(session['profile_id']),
                    SavedJob.listed_job_id == int(job_id),
                )
        )).scalar():
            db.session.close()
            # return make_response('', int(ResponseCodesGeneric.NOT_FOUND))
            # Already gone, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # Checks completed
        # Delete the row
        db.session.query(SavedJob).filter(
            and_(
                SavedJob.user_profile_id == int(session['profile_id']),
                SavedJob.listed_job_id == int(job_id),
            )
        ).delete()
        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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


@user_profiles_saved_lists_rest_bp.route(
    "/unsave_company_active/<int:company_id>",
    methods=["DELETE"]
)
def user_unsave_company_active(company_id: int):
    """
    REST API
    Remove a company from the active user's profile.
    Returns a Status Code as the outcome.
    """

    # Check if User is logged in.
    if not session.get('user_id', False):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    # Check if Company is a valid ID
    if (not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    # Check if User has an active profile
    if not session.get('profile_id', False):
        return make_response('', int(ResponseCodesGeneric.EXPECTATION_FAILED))

    try:
        # Check that user is existent in database.
        if not db.session.query(exists().where(
                User.id == int(session.get('user_id')))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

        # Check if profile exists and belongs to user based on session
        if not db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                )
        )).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if active profile is the currently active profile in database
        # if not, set it as active.
        if db.session.query(exists().where(
                and_(
                    Profile.id == int(session['profile_id']),
                    Profile.user_id == int(session['user_id']),
                    Profile.active.is_(False)
                )
        )).scalar():
            selected_profile = db.session.query(Profile).filter(
                    Profile.id == int(session['profile_id'])
            ).first()
            # Check that profile user ID belongs to the current user and is
            # not None.
            if (selected_profile is None or
                    selected_profile.user_id != int(session['user_id'])):
                db.session.close()
                return make_response('', int(ResponseCodesGeneric.FORBIDDEN))
            selected_profile.active = True
            selected_profile.verified = True
            db.session.commit()

        # Check if company ID exists in the ListedJob Database
        if not db.session.query(exists().where(
                Company.id == int(company_id))).scalar():
            db.session.close()
            return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

        # Check if company ID does not exist in the Saved Company
        # List for the profile
        if not db.session.query(exists().where(
                and_(
                    SavedCompany.user_profile_id == int(session['profile_id']),
                    SavedCompany.company_id == int(company_id),
                )
        )).scalar():
            db.session.close()
            # return make_response('', int(ResponseCodesGeneric.NOT_FOUND))
            # Already gone, so allow client to update the DOM.
            return make_response('', int(ResponseCodesGeneric.OK))

        # Checks completed
        # Delete the row
        db.session.query(SavedCompany).filter(
            and_(
                SavedCompany.user_profile_id == int(session['profile_id']),
                SavedCompany.company_id == int(company_id),
            )
        ).delete()
        db.session.commit()
        db.session.close()

        # Return successful status code upon creation.
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
