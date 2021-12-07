from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException,\
    ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
import os


class TryToDescribe:

    s = Service('driver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    def get_link(self, url):

        self.driver.get(url)

    def login_on_first_form(self):

        login = self.driver.find_element(By.ID, 'loginEmail')
        return login

    def password_on_first_form(self):

        password = self.driver.find_element(By.ID, 'loginPassword')
        return password

    def skip_incorrect_email_allert(self):

        self.driver.find_element(By.XPATH,
                                 '//*[@id="invalidEmailPassword"]/a').click()

    def click_auth_button(self):

        self.driver.find_element(By.ID, 'authButton').click()

    def first_form_testing(self, login, password):
        self.login_on_first_form().clear()
        self.password_on_first_form().clear()
        self.login_on_first_form().send_keys(login)
        self.password_on_first_form().send_keys(password)
        self.click_auth_button()

    def email_on_second_form(self):

        email = self.driver.find_element(By.ID, 'dataEmail')
        return email

    def name_on_second_form(self):

        name = self.driver.find_element(By.ID, 'dataName')
        return name

    def email_and_name_on_second_for_testing(self, email, name):
        self.email_on_second_form().clear()
        self.name_on_second_form().clear()
        self.email_on_second_form().send_keys(email)
        self.name_on_second_form().send_keys(name)
        self.click_data_send_button()

    def accept_data_add(self):
        self.driver.find_element(
            By.XPATH, '/html/body/div[3]/div/div/div[2]/button').click()

    def select_male(self, male):
        select = Select(self.driver.find_element(By.ID, 'dataGender'))
        select.select_by_visible_text(male)

    def select_var_1(self, choice):
        self.driver.find_element(By.ID, f'dataCheck1{choice}').click()

    def select_var_2(self, numb):

        self.driver.find_element(By.ID, f'dataSelect2{numb}').click()

    def check_data_in_table(self, tr, td):

        return self.driver.find_element(
            By.CSS_SELECTOR, f'#dataTable > tbody > tr:nth-child({tr})'
                             f' > td:nth-child({td})').text

    def click_data_send_button(self):

        self.driver.find_element(By.ID, 'dataSend').click()

    def email_format_testing(self, email, name):
        try:
            self.driver.find_element(
                By.CSS_SELECTOR, '#emailFormatError > a').click()
        except ElementClickInterceptedException:
            return False
        return True

    def check_exits_on_data_add(self):
        try:
            self.accept_data_add()

        except ElementClickInterceptedException:
            return False
        return True

    def check_exists_on_first_form_true(self, login, password):

        try:
            self.email_on_second_form().send_keys('')
        except ElementNotInteractableException:
            self.make_screenshot(login, password)

            return False
        return True

    def check_name_error(self):
        try:
            self.driver.find_element(
                By.CSS_SELECTOR, '#blankNameError > a').click()
        except ElementClickInterceptedException:
            return False
        return True

    def check_exists_on_invalid_password_or_login(self, login, password):
        try:
            self.driver.find_element(
                By.XPATH, '//*[@id="invalidEmailPassword"]/a').click()
        except ElementNotInteractableException:
            self.make_screenshot(login, password)
            return False
        return True

    def check_exists_on_login_format_error(self, login, password):
        try:
            self.driver.find_element(
                By.XPATH, '//*[@id="emailFormatError"]/a').click()

        except ElementNotInteractableException:
            self.make_screenshot(login, password)

            return False
        return True

    def make_screenshot(self, login, password):
        self.driver.get_screenshot_as_file(
            f'test_login_first_form_{login}_{password}.png')
        os.replace(f'test_login_first_form_{login}_{password}.png',
                   f'screenshots/test_login_first_form_{login}_{password}.png')
