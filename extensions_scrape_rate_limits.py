import datetime
from datetime import datetime, UTC, timedelta

from models.mariadb.scrape_rate_limit import ScrapeRateLimits


def calculate_next_scrape_rate_limit(
        scrape_rate_limit_row: ScrapeRateLimits,
        current_date_time_utc=datetime.now(UTC)):
    """
    Calculate next query time after an API key is used.
    """
    if (scrape_rate_limit_row is None or
            not isinstance(scrape_rate_limit_row, ScrapeRateLimits)):
        return None

    try:
        max_date_time_utc = current_date_time_utc

        if scrape_rate_limit_row.month_limit is not None:
            # Calculate amount of queries per month
            # 31 days max
            max_date_time_utc = (
                max(
                    max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(days=(
                             31/scrape_rate_limit_row.month_limit
                     )))
                )
            )

        if scrape_rate_limit_row.daily_limit is not None:
            # Calculate amount of queries per day
            max_date_time_utc = (
                max(max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(hours=(24/scrape_rate_limit_row.daily_limit)))))

        if scrape_rate_limit_row.hour_limit is not None:
            # Calculate amount of queries per hour
            max_date_time_utc = (
                max(
                    max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(minutes=(
                             60/scrape_rate_limit_row.hour_limit
                     )))
                )
            )

        if scrape_rate_limit_row.minute_limit is not None:
            # Calculate amount of queries per minute
            max_date_time_utc = (
                max(
                    max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(seconds=(
                             60/scrape_rate_limit_row.minute_limit)))
                )
            )

        return max_date_time_utc
    # Catch any errors related to timedate or timedelta functions.
    except Exception as e:
        print(f"Error: {e}", flush=True)
        # Default to one extra day.
        return datetime.now(UTC) + timedelta(days=1)
