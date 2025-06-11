from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# def before_scenario(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://tutorialsninja.com/demo/")
#
# def after_scenario(context):
#     context.driver.quit()


@given(u'user has navigated to Login page')
def step_impl(context):
    #context.driver = webdriver.Chrome()
    #context.driver.maximize_window()
    #context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT,"Login").click()


@when(u'User enters valid email as "{email}" and password as "{password}"')
def step_impl(context,email,password):
    context.driver.find_element(By.ID ,'input-email').send_keys(email)
    context.driver.find_element(By.ID ,'input-password').send_keys(password)


@when(u'User clicks on submit button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Login']").click()


@then(u'User should login')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
    #context.driver.quit()


@when(u'User enters invalid email and valid password')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "amotoori" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID ,'input-email').send_keys(invalid_email)
    context.driver.find_element(By.ID ,'input-password').send_keys("12345")


@then(u'Proper valid message should be displayed')
def step_impl(context):

    expected_warning_message ="Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)


@when(u'User enters valid email and invalid password')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("123")



@when(u'User enters invalid email and invalid password')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "amotoori" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    context.driver.find_element(By.ID, "input-password").send_keys("12")


@when(u'User do not enter any credentials')
def step_impl(context):
    context.driver.find_element(By.ID,"input-email").send_keys("")
    context.driver.find_element(By.ID,"input-password").send_keys("")
