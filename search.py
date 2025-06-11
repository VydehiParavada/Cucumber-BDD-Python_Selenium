from lib2to3.pgen2 import driver

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

@given(u'User is navigated to home page')
def step_impl(context):
    expected_title="Your Store"
    assert context.driver.title.__eq__(expected_title)
    # context.driver= webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.get("https://tutorialsninja.com/demo/")

@when(u'user entered valid product in search field')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("HP")

@when(u'user clicked on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@id='search']//button").click()

@then(u'Valid product should display in search result')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    # context.driver.quit()


@when(u'user entered invalid product in search field')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("Audi")


@then(u'Proper message should be displayed in search result')
def step_impl(context):
    expected_text="There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    # context.driver.quit()


@when(u'user did not enter any product in search field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")

