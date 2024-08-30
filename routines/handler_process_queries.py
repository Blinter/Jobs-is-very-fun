import os
import subprocess
import sys
from time import sleep
from urllib3.exceptions import ProtocolError
from secrets_jobs.credentials import path_to_base


restart_timer = 45


def queries_routine():
    print("Running Queries..")
    try:
        while True:
            try:
                from subprocess import Popen
                process = Popen([
                    'python3',
                    os.path.join(path_to_base, 'routines/process_queries.py'),
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

                if ("ChildProcessError: Parsing Completed" in e_str or
                        "ChildProcessError: No queries completed" in e_str):
                    print("Queries routine completed. "
                          "\nSleeping " +
                          str(restart_timer) +
                          " seconds and running again...")
                    sleep(restart_timer)

                else:
                    print("UNHANDLED ERROR")
                    raise e
            except urllib3.exceptions.ProtocolError as e:
                print(str(e))
                print("API closed connection. Retrying")

    except KeyError as e:
        e_str = str(e)
        print("UNHANDLED ERROR")
        print("[" + e_str + "]")
        raise e

    except Exception as e:
        print(str(e))
        raise e


queries_routine()
