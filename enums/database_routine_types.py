"""
Database Routines Type
IntEnum
"""
from enum import IntEnum, Enum


class DatabaseRoutineTypes(IntEnum):
    """
    Enum representing various Database Routines mapped to integers.

    Attributes:
        NONE = 0

        QUERY_API = 1

        PROCESS_QUERIES = 2
        PROCESS_JOBS = 3
        PROCESS_COMPANIES = 4
        PROCESS_SCRAPES = 5

        FUNCTION_CLEAN_STALE_MONGO_DB = 6
        FUNCTION_CLEAN_MONGO_STORAGE = 7
        FUNCTION_CLEAN_MONGO_SCRAPE = 8

        FUNCTION_UPDATE_CRON_JOBS = 9
    """
    NONE = 0

    QUERY_API = 1

    PROCESS_QUERIES = 2
    PROCESS_JOBS = 3
    PROCESS_COMPANIES = 4
    PROCESS_SCRAPES = 5

    FUNCTION_CLEAN_STALE_MONGO_DB = 6
    FUNCTION_CLEAN_MONGO_STORAGE = 7
    FUNCTION_CLEAN_MONGO_SCRAPE = 8

    FUNCTION_UPDATE_CRON_JOBS = 9


class DatabaseRoutineTypeDescription(Enum):
    """
    Enum representing various Database Routines mapped to integers.

    Attributes:
        NONE = "None"
        QUERY_API = "QUERY_API"

        PROCESS_QUERIES = "Process Queries"
        PROCESS_JOBS = "Process Jobs"
        PROCESS_COMPANIES = "Process Companies"
        PROCESS_SCRAPES = "Process Scrape Links"

        FUNCTION_CLEAN_STALE_MONGO_DB = "Clean-up Unknown MongoDB Entries"
        FUNCTION_CLEAN_MONGO_STORAGE = "Clean-up Failed MongoStorage Entries"
        FUNCTION_CLEAN_MONGO_SCRAPE = "Clean-up Failed MongoScrape Entries"

        FUNCTION_UPDATE_CRON_JOBS = "Update CRON Jobs"
    """
    NONE = "None (Misc.)"
    QUERY_API = "Query API"

    PROCESS_QUERIES = "Process Queries"
    PROCESS_JOBS = "Process Jobs"
    PROCESS_COMPANIES = "Process Companies"
    PROCESS_SCRAPES = "Process Scrape Links"

    FUNCTION_CLEAN_STALE_MONGO_DB = "Clean-up Unknown MongoDB Entries"
    FUNCTION_CLEAN_MONGO_STORAGE = "Clean-up Failed MongoStorage Entries"
    FUNCTION_CLEAN_MONGO_SCRAPE = "Clean-up Failed MongoScrape Entries"

    FUNCTION_UPDATE_CRON_JOBS = "Update CRON Jobs"


def database_routine_type_to_description(database_routine: int):
    """Converts Database Routine Type to its description"""
    match database_routine:

        case DatabaseRoutineTypes.NONE:
            return DatabaseRoutineTypeDescription.NONE.value

        case DatabaseRoutineTypes.QUERY_API:
            return DatabaseRoutineTypeDescription.QUERY_API.value

        case DatabaseRoutineTypes.PROCESS_QUERIES:
            return DatabaseRoutineTypeDescription.PROCESS_QUERIES.value

        case DatabaseRoutineTypes.PROCESS_JOBS:
            return DatabaseRoutineTypeDescription.PROCESS_JOBS.value

        case DatabaseRoutineTypes.PROCESS_COMPANIES:
            return DatabaseRoutineTypeDescription.PROCESS_COMPANIES.value

        case DatabaseRoutineTypes.PROCESS_SCRAPES:
            return DatabaseRoutineTypeDescription.PROCESS_SCRAPES.value

        case DatabaseRoutineTypes.FUNCTION_CLEAN_STALE_MONGO_DB:
            return (DatabaseRoutineTypeDescription
                    .FUNCTION_CLEAN_STALE_MONGO_DB
                    .value)

        case DatabaseRoutineTypes.FUNCTION_CLEAN_MONGO_STORAGE:
            return (DatabaseRoutineTypeDescription
                    .FUNCTION_CLEAN_MONGO_STORAGE
                    .value)

        case DatabaseRoutineTypes.FUNCTION_CLEAN_MONGO_SCRAPE:
            return (DatabaseRoutineTypeDescription
                    .FUNCTION_CLEAN_MONGO_SCRAPE
                    .value)

        case DatabaseRoutineTypes.FUNCTION_UPDATE_CRON_JOBS:
            return (DatabaseRoutineTypeDescription
                    .FUNCTION_UPDATE_CRON_JOBS
                    .value)


db_routines_frequency_types = {
    str(DatabaseRoutineTypes.NONE.value):
        {
            "0": {
                "name": "6 days",
                "time_span": 8640, # 60 * 24 * 6
            },
            "1": {
                "name": "6 days",
                "time_span": 8640, # 60 * 24 * 6
            },
        },

    str(DatabaseRoutineTypes.QUERY_API.value):
        [],

    str(DatabaseRoutineTypes.PROCESS_QUERIES.value):
        [],
    str(DatabaseRoutineTypes.PROCESS_JOBS.value):
        [],
    str(DatabaseRoutineTypes.PROCESS_COMPANIES.value):
        [],
    str(DatabaseRoutineTypes.PROCESS_SCRAPES.value):
        [],

    str(DatabaseRoutineTypes.FUNCTION_CLEAN_STALE_MONGO_DB.value):
        [],
    str(DatabaseRoutineTypes.FUNCTION_CLEAN_MONGO_STORAGE.value):
        [],
    str(DatabaseRoutineTypes.FUNCTION_CLEAN_MONGO_SCRAPE.value):
        [],

    str(DatabaseRoutineTypes.FUNCTION_UPDATE_CRON_JOBS.value):
        [],
}
