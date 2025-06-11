from datetime import datetime
from lib2to3.fixes.fix_input import context
from lib2to3.pgen2 import driver
from operator import contains

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# def before_scenario(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://tutorialsninja.com/demo/")
#
# def after_scenario(context):
#     context.driver.quit()

@given(u'User navigates to register page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT,'Register').click()

@when(u'User enter below details to all mandatory fields')
def step_impl(context):
    for row in context.table:
        context.driver.find_element(By.ID,"input-firstname").send_keys(row["first_name"])
        context.driver.find_element(By.ID,"input-lastname").send_keys(row["last_name"])
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        new_email = "vyd" + time_stamp + "@gmail.com"
        context.driver.find_element(By.ID,"input-email").send_keys(new_email)
        context.driver.find_element(By.ID,"input-telephone").send_keys(row["telephone"])
        context.driver.find_element(By.ID,"input-password").send_keys(row["password"])
        context.driver.find_element(By.ID,"input-confirm").send_keys(row["password"])

@when(u'User click on privacy statement')
def step_impl(context):
    context.driver.find_element(By.NAME,"agree").click()


@when(u'User clicks on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input [@value='Continue']").click()


@then(u'Account should be created')
def step_impl(context):
    expected_message="Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_message)


@when(u'User enter details to all fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Vyd")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Par")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "vyd" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("848972842")
    context.driver.find_element(By.ID, "input-password").send_keys("23456")
    context.driver.find_element(By.ID, "input-confirm").send_keys("23456")
    context.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()



@when(u'User enter details to all fields except email address')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Vyd")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Par")
    context.driver.find_element(By.ID, "input-telephone").send_keys("848972842")
    context.driver.find_element(By.ID, "input-password").send_keys("23456")
    context.driver.find_element(By.ID, "input-confirm").send_keys("23456")
    context.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()


@when(u'User enter existing email address')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("vy@gmail.com")



@then(u'Proper warning message is displayed')
def step_impl(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
        expected_warning)


@when(u'User does not enter any details')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")

@then(u'Proper warning message is displayed for all fields')
def step_impl(context):
    expected_privacy_policy_warning="Warning: You must agree to the Privacy Policy!"
    expected_Firstname_warning="First Name must be between 1 and 32 characters!"
    expected_LastName_warning="Last Name must be between 1 and 32 characters!"
    expected_email_warning="E-Mail Address does not appear to be valid!"
    expected_telephone_warning="Telephone must be between 3 and 32 characters!"
    expected_password_warning="Password must be between 4 and 20 characters!"
    assert context.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]").text.__contains__(expected_privacy_policy_warning)
    assert context.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected_Firstname_warning)
    assert context.driver.find_element(By.XPATH,"//input[@id='input-lastname']/following-sibling::div").text.__eq__(expected_LastName_warning)
    assert context.driver.find_element(By.XPATH,"//input[@id='input-email']/following-sibling::div").text.__eq__(expected_email_warning)
    assert context.driver.find_element(By.XPATH,"//input[@id='input-telephone']/following-sibling::div").text.__eq__(expected_telephone_warning)
    assert context.driver.find_element(By.XPATH,"//input[@id='input-password']/following-sibling::div").text.__eq__(expected_password_warning)

    #context.driver.quit()