from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("http://automationpractice.com/index.php")
login = driver.find_element_by_class_name("login")
login.send_keys(Keys.RETURN)

create_acc=driver.find_element_by_id("email_create")
create_acc.send_keys("finalGo1@gmail.com")
driver.find_element_by_id("SubmitCreate").click()
time.sleep(6)
driver.find_element_by_id("id_gender1").click()
time.sleep(2)
driver.find_element_by_id("customer_firstname").send_keys("Abcd")
time.sleep(2)
driver.find_element_by_id("customer_lastname").send_keys("Wxyz")
time.sleep(2)
driver.find_element_by_id("passwd").send_keys("12345678")
time.sleep(2)
driver.find_element_by_id("days").send_keys("12")
time.sleep(2)
driver.find_element_by_id("months").send_keys("June")
time.sleep(2)
driver.find_element_by_id("years").send_keys("2000")
time.sleep(2)
driver.find_element_by_id("newsletter").click()
time.sleep(2)
driver.find_element_by_id("firstname").send_keys("Mirpur")
time.sleep(2)
driver.find_element_by_id("lastname").send_keys("Dhaka")
time.sleep(2)
driver.find_element_by_id("company").send_keys("Guchi")
time.sleep(2)
driver.find_element_by_id("address1").send_keys("178 ns road")
time.sleep(2)
driver.find_element_by_id("city").send_keys("wqeqr")
time.sleep(2)
driver.find_element_by_id("id_state").send_keys("h")
time.sleep(2)
driver.find_element_by_id("postcode").send_keys("00000")
time.sleep(2)
driver.find_element_by_id("id_country").send_keys("u")
time.sleep(2)
driver.find_element_by_id("phone_mobile").send_keys("1234567891")
time.sleep(2)
driver.find_element_by_id("alias").send_keys("My address12")
time.sleep(2)
register = driver.find_element_by_id("submitAccount")
time.sleep(2)
register.send_keys(Keys.RETURN)


print("First user's account created successfully!!!")

time.sleep(2)


driver.find_element_by_class_name("logout").click()
time.sleep(6)

print("Scecond user is creating!!")

create_acc=driver.find_element_by_id("email_create")
create_acc.send_keys("finalGo2@gmail.com")
driver.find_element_by_id("SubmitCreate").click()
time.sleep(6)
driver.find_element_by_id("id_gender2").click()
time.sleep(2)
driver.find_element_by_id("customer_firstname").send_keys("Abcd")
time.sleep(2)
driver.find_element_by_id("customer_lastname").send_keys("Wxyz")
time.sleep(2)
driver.find_element_by_id("passwd").send_keys("7654321")
time.sleep(2)
driver.find_element_by_id("days").send_keys("16")
time.sleep(2)
driver.find_element_by_id("months").send_keys("October")
time.sleep(2)
driver.find_element_by_id("years").send_keys("2002")
time.sleep(2)
driver.find_element_by_id("newsletter").click()
time.sleep(2)
driver.find_element_by_id("firstname").send_keys("Banani")
time.sleep(2)
driver.find_element_by_id("lastname").send_keys("Dhaka")
time.sleep(2)
driver.find_element_by_id("company").send_keys("Balak")
time.sleep(2)
driver.find_element_by_id("address1").send_keys("221 st road")
time.sleep(2)
driver.find_element_by_id("city").send_keys("wqeqr")
time.sleep(2)
driver.find_element_by_id("id_state").send_keys("h")
time.sleep(2)
driver.find_element_by_id("postcode").send_keys("00000")
time.sleep(2)
driver.find_element_by_id("id_country").send_keys("u")
time.sleep(2)
driver.find_element_by_id("phone_mobile").send_keys("0177976721")
time.sleep(2)
driver.find_element_by_id("alias").send_keys(" is this")
time.sleep(2)
register = driver.find_element_by_id("submitAccount")
time.sleep(2)
register.send_keys(Keys.RETURN)

print("Second user's account created successfully!!!")

time.sleep(4)

driver.find_element_by_class_name("logout").click()
time.sleep(4)

#Now for the shopping process

driver.find_element_by_id("email").send_keys("finalGo1@gmail.com")
driver.find_element_by_id("passwd").send_keys("12345678")
driver.find_element_by_id("SubmitLogin").click()
time.sleep(6)

driver.find_element_by_link_text("DRESSES").click()
time.sleep(3)
driver.find_element_by_link_text("Casual Dresses").click()
time.sleep(3)
driver.find_element_by_link_text("Add to cart").click()
time.sleep(2)
driver.find_element_by_class_name("continue").click()
time.sleep(2)
driver.find_element_by_link_text("T-SHIRTS").click()
time.sleep(5)
driver.find_element_by_id("layered_id_attribute_group_14").click()
time.sleep(3)
driver.find_element_by_link_text("Add to cart").click()
time.sleep(2)
driver.find_element_by_link_text("Proceed to checkout").click()
time.sleep(2)
driver.find_element_by_link_text("Proceed to checkout").click()
time.sleep(2)
driver.find_element_by_name("processAddress").click()
time.sleep(2)
driver.find_element_by_id("cgv").click()
time.sleep(2)
driver.find_element_by_name("processCarrier").click()
time.sleep(2)
driver.find_element_by_class_name("cheque").click()
time.sleep(5)
driver.find_element_by_class_name("logout").click()

print("Completed for user 1")

driver.find_element_by_id("email").send_keys("finalGO2@gmail.com")
driver.find_element_by_id("passwd").send_keys("7654321")
driver.find_element_by_id("SubmitLogin").click()
time.sleep(6)

driver.find_element_by_link_text("DRESSES").click()
time.sleep(3)
driver.find_element_by_link_text("Casual Dresses").click()
time.sleep(3)
driver.find_element_by_link_text("Add to cart").click()
time.sleep(2)
driver.find_element_by_class_name("continue").click()
time.sleep(2)
driver.find_element_by_link_text("T-SHIRTS").click()
time.sleep(5)
driver.find_element_by_id("layered_id_attribute_group_14").click()
time.sleep(3)
driver.find_element_by_link_text("Add to cart").click()
time.sleep(2)
driver.find_element_by_link_text("Proceed to checkout").click()
time.sleep(2)
driver.find_element_by_link_text("Proceed to checkout").click()
time.sleep(2)
driver.find_element_by_name("processAddress").click()
time.sleep(2)
driver.find_element_by_id("cgv").click()
time.sleep(2)
driver.find_element_by_name("processCarrier").click()
time.sleep(2)
driver.find_element_by_class_name("cheque").click()
time.sleep(5)
driver.find_element_by_class_name("logout").click()

print("completed for user 2")

driver.quit()












