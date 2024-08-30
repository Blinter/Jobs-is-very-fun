from xvfbwrapper import Xvfb
import random

from extensions_undetected_chromedriver import (
    uc_chromium_pull_page,
    destroy_chromium_process,
    cleanup_temp_profile_data,
    destroy_display
)


# def debug_chromedriver():
#     try:
#         # Start the ChromeDriver service
#         service = Service('/usr/bin/chromedriver')
#         service.start()
#
#         options = webdriver.ChromeOptions()
#         # Specify the path to chromium
#         chromium_path = '/usr/bin/chromium'
#         print(f"Using Chromium at: {chromium_path}")
#         options.binary_location = chromium_path
#
#         # Add options to prevent errors
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--headless')  # Run headless if necessary
#         options.add_argument(
#             '--disable-gpu')  # Disable GPU if running headless
#         options.add_argument('--remote-debugging-port=9222')
#         Debugging port
#
#         driver = webdriver.Chrome(service=service, options=options)
#
#         # Get the Chrome/Chromium version
#         chrome_version = driver.capabilities['browserVersion']
#         print(f"Chrome/Chromium version: {chrome_version}")
#
#         driver.quit()
#     except SessionNotCreatedException as e:
#         print("Error: Session not created")
#         print(f"Exception message: {e}")
#     except Exception as e:
#         print("An error occurred")
#         print(f"Exception message: {e}")

# debug_chromedriver()

# raise ValueError("Done")

display = Xvfb()
try:
    display.start()

    from extensions_user_agents import user_agent_list
    user_agent: str = random.choice(user_agent_list)

    response: str = uc_chromium_pull_page(
                        user_agent=user_agent,
                        proxy_server="socks5://0.0.0.0:0",
                        url="https://jobs.is-very.fun"
                    )

    # Run killall after response is retrieved
    destroy_chromium_process()

    if response is None:
        raise EnvironmentError("Response returned nothing.")

    print(response)


finally:
    display.stop()
    destroy_display()
    destroy_chromium_process()
    cleanup_temp_profile_data()
