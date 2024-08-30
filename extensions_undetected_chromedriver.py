import os
from time import sleep

import undetected_chromedriver as uc
from selenium.common import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import ChromeOptions

from secrets_jobs.credentials import (
    path_to_chromium_exe,
    path_to_chrome_driver
)


def cleanup_temp_profile_data():
    """
    Force kill all chromium lingering processes on Linux
    """
    # print("Cleaning up Temp chromium data", flush=True)
    os.system('rm -Rf /tmp/.org.chromium*')
    os.system('rm -Rf /tmp/.com.google*')
    os.system('rm -Rf /tmp/tmp*')


def destroy_display():
    """
    Force kill all lingering Xvfb processes on Linux
    """
    os.system('killall Xvfb -q -s 9 -u `whoami`')


def destroy_chromium_process():
    """
    Force kill all chromium lingering processes on Linux
    """
    # print("Killing all chromium processes.", flush=True)
    os.system('killall chromium -q -s 9 -u `whoami`')
    os.system('killall undetected_chromedriver -q -s 9 -u `whoami`')
    # os.system('killall google-chrome-stable -q -s 9 -u `whoami`')
    os.system('killall chrome_crashpad_handler -q -s 9 -u `whoami`')

    # Destroy zombie processes that have been spawned
#     os.system("""
# for pid in $(ps -xal | \
# grep -v grep | \
# grep -w ZN+ | \
# awk '{print $3}');do kill -9 $pid; done;\
# """)


def uc_chromium_pull_page(
        user_agent: str,
        proxy_server: str,
        url: str):
    """
    Use Undetected Chromedriver to launch chromium and load all javascript for
    the requested page.
    """
    # noinspection PyGlobalUndefined
    global driver

    options: ChromeOptions = uc.ChromeOptions()

    options.headless = False

    options.binary_location = path_to_chromium_exe

    options.add_argument(f'--proxy-server={proxy_server}')

    # print("Using Proxy: " + str(proxy_server), flush=True)

    options.add_argument(f"--user-agent={user_agent}")

    options.add_argument('--no-sandbox')

    # options.add_argument(
    #     '--disable-dev-shm-usage'
    # )

    # Only for Windows
    # options.add_argument(
    #     "--disable-gpu"
    # )

    try:

        driver = uc.Chrome(
            driver_executable_path=path_to_chrome_driver,
            options=options
        )

        driver.implicitly_wait(5)

        driver.get(url)

        WebDriverWait(
            driver=driver,
            timeout=15,
            poll_frequency=2,
        ).until(
            lambda d: d.execute_script(
                'return document.readyState'
            ) == 'complete'
        )

        # let page load in background
        sleep(8)

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        # Execute JavaScript to retrieve all text content from the page
        text_return: str = (
            driver.execute_script("return document.body.textContent")
        )

        # Fix to close the page and reduce close overhead
        driver.execute_script("window.open('', '_self', ''); window.close();")

        return text_return

    except OSError as e:
        print(f"OSError occurred: {e.strerror}", flush=True)
        print(f"URL: {url}")
        raise e

    except WebDriverException as e:
        if "unknown error: net::ERR_SOCKS_CONNECTION_FAILED" not in str(e.msg):
            print(f"WebDriverException {e.msg}", flush=True)
        print(f"Failed URL: {url}")
        raise e

    except Exception as e:
        print(f"An error occurred: {e}", flush=True)
        print(f"URL: {url}")
        raise e

    finally:
        if (driver is not None and
                isinstance(driver, uc.Chrome)):
            driver.close()
            driver.quit()
