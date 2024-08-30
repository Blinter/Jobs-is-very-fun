import os
import subprocess
import sys
from time import sleep
from datetime import datetime, timedelta
import pytz
from secrets_jobs.credentials import path_to_base


# def seconds_to_hour():
#     now = datetime.now(pytz.utc)
#     return int((datetime(now.year, now.month, now.day, now.hour).replace(
#         tzinfo=pytz.UTC) +
#             timedelta(hours=1) - now).total_seconds())


def seconds_to_midnight():
    now = datetime.now(pytz.utc)
    return int((datetime(now.year, now.month, now.day).replace(
        tzinfo=pytz.UTC) +
            timedelta(days=1) - now).total_seconds())


def seconds_to_next_2_hour_split():
    now = datetime.now(pytz.utc)
    current_hour = now.hour
    next_split_hour = ((current_hour // 2) + 1) * 2

    if next_split_hour >= 24:
        next_split_hour = 0
        next_split_day = now + timedelta(days=1)
    else:
        next_split_day = now

    next_split_time = datetime(year=next_split_day.year,
                               month=next_split_day.month,
                               day=next_split_day.day,
                               hour=next_split_hour,
                               tzinfo=pytz.UTC)

    return int((next_split_time - now).total_seconds())


def update_timegraph_database_jobs_routine():
    print("Running Timegraph generation for jobs...")
    try:
        while True:
            try:
                from subprocess import Popen
                process = Popen([
                    'python3',
                    os.path.join(
                        path_to_base,
                        'routines/generate_timegraph_jobs.py'),
                ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    start_new_session=True,
                    universal_newlines=True,
                    bufsize=1,
                )
                # Read stdout line by line
                while True:
                    stdout_line = process.stdout.readline()

                    if (stdout_line == '' and
                            process.poll() is not None):
                        break

                    if stdout_line:
                        print(stdout_line, end='')
                        sys.stdout.flush()

                # Get remaining stderr
                stderr = process.communicate()[1]

                if process.returncode != 0:
                    raise ChildProcessError(
                        str(
                            stderr
                            if stderr is not None
                            else 'UNKNOWN ERROR'
                        )
                    )

                raise ChildProcessError("Process completed but did not "
                                        "receive a successful status message")

            except ChildProcessError as e:
                e_str = str(e)

                if ("Count Completed"
                        in e_str):
                    print("Timegraph generation objects processed. "
                          "\nSleeping " + str(seconds_to_next_2_hour_split()) +
                          " seconds (until next 2 hour split) " +
                          "then running again.")
                    sleep(seconds_to_next_2_hour_split())

                else:
                    print("UNHANDLED ERROR")
                    print("[" + e_str + "]")
                    raise e

    except Exception as e:
        print(str(e))
        raise e


update_timegraph_database_jobs_routine()
