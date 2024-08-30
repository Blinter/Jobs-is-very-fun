import undetected_chromedriver as uc


options = uc.ChromeOptions()
options.add_argument("""--proxy-server=socks5://0.0.0.0:0""")
driver = uc.Chrome(options=options, headless=True, use_subprocess=False,
                   browser_executable_path="/usr/bin/chromium",
                   driver_executable_path="/tmp/chromedriver")
driver.get('https://api.ipify.org')
driver.save_screenshot('ip.png')
