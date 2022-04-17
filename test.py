import unittest
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

class LoginTest(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
          cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")


     def test_create_a_account(self):
         self.driver.get("http://automationpractice.com/index.php")
         self.driver.find_element_by_class_name("login").click()


         create_acc = self.driver.find_element_by_id("email_create")
         create_acc.send_keys("Justfortest119@gmail.com")
         self.driver.find_element_by_id("SubmitCreate").click()
         time.sleep(6)
         self.driver.find_element_by_id("id_gender1").click()
         time.sleep(2)
         self.driver.find_element_by_id("customer_firstname").send_keys("Abcd")
         time.sleep(2)
         self.driver.find_element_by_id("customer_lastname").send_keys("Wxyz")
         time.sleep(2)
         self.driver.find_element_by_id("passwd").send_keys("12345678")
         time.sleep(2)
         self.driver.find_element_by_id("days").send_keys("12")
         time.sleep(2)
         self.driver.find_element_by_id("months").send_keys("June")
         time.sleep(2)
         self.driver.find_element_by_id("years").send_keys("2000")
         time.sleep(2)
         self.driver.find_element_by_id("newsletter").click()
         time.sleep(2)
         self.driver.find_element_by_id("firstname").send_keys("Mirpur")
         time.sleep(2)
         self.driver.find_element_by_id("lastname").send_keys("Dhaka")
         time.sleep(2)
         self.driver.find_element_by_id("company").send_keys("Guchi")
         time.sleep(2)
         self.driver.find_element_by_id("address1").send_keys("178 ns road")
         time.sleep(2)
         self.driver.find_element_by_id("city").send_keys("wqeqr")
         time.sleep(2)
         self.driver.find_element_by_id("id_state").send_keys("h")
         time.sleep(2)
         self.driver.find_element_by_id("postcode").send_keys("00000")
         time.sleep(2)
         self.driver.find_element_by_id("id_country").send_keys("u")
         time.sleep(2)
         self.driver.find_element_by_id("phone_mobile").send_keys("1234567891")
         time.sleep(2)
         self.driver.find_element_by_id("alias").send_keys("My address12")
         time.sleep(2)
         register = self.driver.find_element_by_id("submitAccount")
         time.sleep(2)
         register.send_keys(Keys.RETURN)

         print("First user's account created successfully!!!")
         time.sleep(6)
         self.driver.close()
         self.drive.quit()

class LoginTest2(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
         cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")


     def test_create_another_account(self):
         self.driver.get("http://automationpractice.com/index.php")
         self.driver.find_element_by_class_name("login").click()






         print("Scecond user is creating!!")

         create_acc = self.driver.find_element_by_id("email_create")
         create_acc.send_keys("justFortest2@gmail.com")
         self.driver.find_element_by_id("SubmitCreate").click()
         time.sleep(6)
         self.fdriver.find_element_by_id("id_gender2").click()
         time.sleep(2)
         self.driver.find_element_by_id("customer_firstname").send_keys("Abcd")
         time.sleep(2)
         self.driver.find_element_by_id("customer_lastname").send_keys("Wxyz")
         time.sleep(2)
         self.driver.find_element_by_id("passwd").send_keys("7654321")
         time.sleep(2)
         self.driver.find_element_by_id("days").send_keys("16")
         time.sleep(2)
         self.driver.find_element_by_id("months").send_keys("October")
         time.sleep(2)
         self.driver.find_element_by_id("years").send_keys("2002")
         time.sleep(2)
         self.driver.find_element_by_id("newsletter").click()
         time.sleep(2)
         self.driver.find_element_by_id("firstname").send_keys("Banani")
         time.sleep(2)
         self.driver.find_element_by_id("lastname").send_keys("Dhaka")
         time.sleep(2)
         self.driver.find_element_by_id("company").send_keys("Balak")
         time.sleep(2)
         self.driver.find_element_by_id("address1").send_keys("221 st road")
         time.sleep(2)
         self.driver.find_element_by_id("city").send_keys("wqeqr")
         time.sleep(2)
         self.driver.find_element_by_id("id_state").send_keys("h")
         time.sleep(2)
         self.driver.find_element_by_id("postcode").send_keys("00000")
         time.sleep(2)
         self.driver.find_element_by_id("id_country").send_keys("u")
         time.sleep(2)
         self.driver.find_element_by_id("phone_mobile").send_keys("0177976721")
         time.sleep(2)
         self.driver.find_element_by_id("alias").send_keys(" is this")
         time.sleep(2)
         register = self.driver.find_element_by_id("submitAccount")
         time.sleep(2)
         register.send_keys(Keys.RETURN)

         print("Second user's account created successfully!!!")




