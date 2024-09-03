import os
import subprocess
import sys
from datetime import datetime
from time import sleep

from secrets_jobs.credentials import path_to_base

restart_timer = 90

current_checkpoint = "Mon, 02 Sep 2024 18:45:31.968000 UTC"


def jobs_process_routine(new_date=current_checkpoint):
    print("Running Jobs Processing Routine...")
    try:
        while True:
            try:
                from subprocess import Popen
                process = Popen([
                    'python3',
                    os.path.join(path_to_base, 'routines/process_jobs.py'),
                    "--date", new_date
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

                    if stdout_line == '' and process.poll() is not None:
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

            except ChildProcessError as e:
                e_str = str(e)

                if "Parsing Completed" in e_str:
                    print("Process Jobs routine completed. "
                          "\nSleeping " +
                          str(restart_timer) +
                          " seconds and running again...")
                    sleep(restart_timer)

                elif "Completed. Latest DateTime: [[" in e_str:
                    new_datetime = (
                        e_str[(e_str.find("Completed. Latest DateTime: [[") +
                               len("Completed. Latest DateTime: [[")
                               ):
                              e_str.find("]]")
                              ]
                    ).strip()
                    try:
                        if new_datetime != "earliest":
                            _ = datetime.strptime(new_datetime,
                                                  "%a, %d %b %Y %H:%M:%S.%f %Z")
                        else:
                            pass

                    except Exception as f:
                        print("Error parsing new datetime string " +
                              new_datetime)
                        raise f

                    print("Jobs routine has processed data. "
                          "New checkpoint: (" +
                          new_datetime + ")" +
                          "\n"
                          "Sleeping " +
                          str(restart_timer) +
                          " seconds and running again.")
                    new_date = new_datetime
                    sleep(restart_timer)

                else:
                    print("UNHANDLED ERROR")
                    raise e

    except KeyError as e:
        e_str = str(e)
        print("UNHANDLED ERROR")
        print("[" + e_str + "]")
        raise e

    except Exception as e:
        print(str(e))
        raise e


jobs_process_routine()
