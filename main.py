from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from complaint_bot import InternetSpeedTwitterBot
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = Service("C:\Development\chromedriver.exe")
TWITTER_EMAIL = os.environ.get("twitter_email")
TWITTER_PASSWORD = os.environ.get("twitter_password")

chrome_driver_service = CHROME_DRIVER_PATH
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("window-size=1200x600")
twitter_bot = InternetSpeedTwitterBot(chrome_driver_service, options)

twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)
