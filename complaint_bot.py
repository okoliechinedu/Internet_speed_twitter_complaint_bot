from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:

    def __init__(self, chrome_driver_service, options):
        self.driver = webdriver.Chrome(service=chrome_driver_service, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # cookie settings
        time.sleep(2)
        more_options = self.driver.find_element(By.XPATH, '//*[@id="onetrust-pc-btn-handler"]')
        more_options.click()
        time.sleep(3)
        confirm_my_choices = self.driver.find_element(By.XPATH, '//*[@id="onetrust-pc-sdk"]/div/div[3]/div[1]/button')
        confirm_my_choices.click()
        time.sleep(1)

        # Go button
        go = self.driver.find_element(By.CLASS_NAME, 'start-text')
        self.driver.execute_script("arguments[0].click();", go)

        time.sleep(50)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(f"Download speed: {self.down}Mbps")
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Upload speed: {self.up}Mbps")

    def tweet_at_provider(self, email, password):
        self.driver.get("https://twitter.com/home")

        # login to twitter
        time.sleep(4)
        fill_in = self.driver.find_element(By.CSS_SELECTOR, "input")
        fill_in.send_keys(email)
        time.sleep(2)

        next_button = self.driver.find_element(By.CLASS_NAME, "r-qvutc0")
        next_button.click()
        time.sleep(2)

        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/'
                                                    'div[1]/a/div')
        log_in.click()
        time.sleep(4)

        repeat_fill_in = self.driver.find_element(By.CSS_SELECTOR, 'input')
        repeat_fill_in.send_keys(email)
        self.driver.implicitly_wait(3)
        # time.sleep(10)
        # first_input_password = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/'
        #                                                           'div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/'
        #                                                           'div/div/div[3]/div/label/div/div[2]/div[1]/input')
        # first_input_password.send_keys(password)

        # troubleshooting next_button (still trying to figure out how to get the exact xpath)
        next_button_again = self.driver.find_element(By.XPATH, "//body/div[@id='react-root']/div[1]/div[1]/div[1]/"
                                                               "div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]"
                                                               "/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/"
                                                               "div[6]/div[1]")
        next_button_again.click()
        time.sleep(2)

        # bypass security
        security = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/'
                                                      'div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/'
                                                      'div[2]/div/input')
        security.send_keys("okoliechinedu5")
        next_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/'
                                                         'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/'
                                                         'div/div')
        next_button.click()
        time.sleep(2)

        # password
        input_password = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/'
                                                            'div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/'
                                                            'div[3]/div/label/div/div[2]/div[1]/input')
        input_password.send_keys(password)
        log_in_twitter = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/'
                                                            'div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/'
                                                            'div/div/div/div')
        log_in_twitter.click()
        time.sleep(10)

        # tweet at provider
        tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        tweet.send_keys(f"Hey @yettelhungary, Why is my internet speed {self.down}down/{self.up} "
                        f"when i pay for 150down/60up")
        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/'
                                                          'div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/'
                                                          'div[2]/div[3]/div')
        tweet_button.click()


