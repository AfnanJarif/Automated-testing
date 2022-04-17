from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage():
    def __init__(self,driver):
        self.driver = driver

        self.create_email_textbox_id = "email_create"
        self.login_email_textbox_id = "email"
        self.create_account_button_id = "SubmitCreate"
        self.password_taxtbox_id = "passwd"
    def enter_create_username(self,username):
        self.driver.find_element_by_id(self.create_email_textbox_id).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_taxtbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.create_account_button_id).click()