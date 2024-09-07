import Data.user_data as user_data
import pytest
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.mark.login_linux
class TestLogin:

    # @pytest.mark.login
    @pytest.mark.positive_linux
    def test_positive_login(self):
        # Initialize ChromeOptions and set desired options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Example: Run Chrome in headless mode
        chrome_options.add_argument('--no-sandbox')  # Required for some Linux environments
        chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited /dev/shm space issues

        # Use WebDriver Manager to manage the ChromeDriver version
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="128.0.6613.119").install()), options=chrome_options)


        # # Get the path to the ChromeDriver executable
        # chrome_driver_path = ChromeDriverManager().install()

        # # Initialize the Chrome WebDriver with Service and Options
        # service = Service(chrome_driver_path)
        # driver = webdriver.Chrome(service=service, options=chrome_options)

        # Path to your ChromeDriver executable
        # chromedriver_path = r'D:\WORK\Training\Technical Test - PT Altech Omega Andalan\chromedriver-win64\chromedriver-win64\chromedriver.exe'

        # Set up the ChromeDriver service
        # current_dir = os.getcwd()
        # # print(current_dir)
        # chromedriver_path = os.path.join(current_dir,'chromedriver-win64', 'chromedriver.exe')
        # # print(chromedriver_path)

        # Set up the ChromeDriver service
        # service = Service(chromedriver_path)
        # driver = webdriver.Chrome(service=service, options=chrome_options)

        #Open Browser
        # driver = webdriver.Chrome()

        # Now you can use the 'driver' instance to interact with your web application
        driver.get(user_data.URL)

        # Set implicit wait time to 10 seconds
        driver.implicitly_wait(user_data.implicit_wait_time)

        # Type username into Username field
        username_locator = driver.find_element(By.ID, "user-name")
        username_locator.send_keys(user_data.STANDARD_USER)

        # Type password into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(user_data.STANDARD_PASSWORD)

        # Puch Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//input[@class='submit-button btn_action']")
        # submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        driver.implicitly_wait(user_data.implicit_wait_time)

        # Verify new page URL is home URL after user success login/
        actual_url = driver.current_url
        assert actual_url == user_data.home_url

        # Close the browser
        driver.quit()

    @pytest.mark.login_linux
    @pytest.mark.negative_linux
    def test_negative_login(self):
        # Initialize ChromeOptions and set desired options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Example: Run Chrome in headless mode
        chrome_options.add_argument('--no-sandbox')  # Required for some Linux environments
        chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited /dev/shm space issues

        # Use WebDriver Manager to manage the ChromeDriver version
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="128.0.6613.119").install()), options=chrome_options)


        # # Get the path to the ChromeDriver executable
        # chrome_driver_path = ChromeDriverManager().install()

        # # Initialize the Chrome WebDriver with Service and Options
        # service = Service(chrome_driver_path)
        # driver = webdriver.Chrome(service=service, options=chrome_options)
        # # Path to your ChromeDriver executable
        # chromedriver_path = r'D:\WORK\Training\Technical Test - PT Altech Omega Andalan\chromedriver-win64\chromedriver-win64\chromedriver.exe'
        # Set up the ChromeDriver service
        # current_dir = os.getcwd()
        # # print(current_dir)
        # chromedriver_path = os.path.join(current_dir,'chromedriver-win64', 'chromedriver.exe')
        # # print(chromedriver_path)
        # # Set up the ChromeDriver service
        # service = Service(chromedriver_path)
        # driver = webdriver.Chrome(service=Service, options=chrome_options)

        #Open Browser
        # driver = webdriver.Chrome()
        driver.maximize_window()

        # Now you can use the 'driver' instance to interact with your web application
        driver.get(user_data.URL)

        # Set implicit wait time to 10 seconds
        driver.implicitly_wait(user_data.implicit_wait_time)

        # Type username into Username field
        username_locator = driver.find_element(By.ID, "user-name")
        username_locator.send_keys(user_data.LOCKED_OUT_USER)

        # Type password into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(user_data.STANDARD_PASSWORD)

        # Puch Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//input[@class='submit-button btn_action']")
        # submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        driver.implicitly_wait(user_data.implicit_wait_time)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be displayed"
        # add message at the end after comma to print log message when the test is FAIL
      
        # Verify error message text is Your username is invalid
        error_message = error_message_locator.text
        # store the error message text on variable error_message
        assert error_message == "Epic sadface: Sorry, this user has been locked out.", "Error message is not expected"
        # add message at the end after comma to print log message when the test is FAIL

        # Close the browser
        driver.quit()



        