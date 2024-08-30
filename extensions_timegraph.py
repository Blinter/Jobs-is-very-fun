from sqlalchemy import select, asc, desc
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from extensions_sql import db
from models.mariadb.database_timegraph import DatabaseTimegraph


def get_current_timegraph_data():
    """
    Query database and retrieve timegraph data
    """

    # Database methods are enclosed in a try-except block.
    try:
        # Access DatabaseTimegraph Table
        return (
            db.session.query(DatabaseTimegraph)
            .order_by(desc(DatabaseTimegraph.time)).limit(30).all()
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        return None
