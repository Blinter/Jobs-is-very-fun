import os
import subprocess
import sys
from time import sleep

from secrets_jobs.credentials import path_to_base

restart_timer = 300


def scraping_routine():
    print("Running Scraper..")
    try:
        while True:
            try:
                from subprocess import Popen
                process = Popen([
                    'python3',
                    os.path.join(path_to_base, 'routines/process_scrape.py'),
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

                print("Scraping Routine completed.")
                sleep(restart_timer)

            except ChildProcessError as e:
                e_str = str(e)

                if "Completed" in e_str:
                    print("Scrapes completed."
                          "\n"
                          "Sleeping " +
                          str(restart_timer) +
                          " seconds then running again.")
                    sleep(restart_timer)

                elif "ValueError: Nothing to process." in e_str:
                    print("Scrapes completed."
                          "\n"
                          "Sleeping " +
                          str(restart_timer) +
                          " and running again.")
                    sleep(restart_timer)
                elif "ZOMBIE PROCESS CLEANUP" in e_str:
                    print("Scrapes batch completed."
                          "\nRunning again.")

                else:
                    print("UNHANDLED ERROR")
                    print("[" + e_str + "]")
                    raise e

    except KeyError as e:
        e_str = str(e)
        print("UNHANDLED ERROR")
        print("[" + e_str + "]")
        raise e

    except Exception as e:
        print(str(e))
        raise e


scraping_routine()
