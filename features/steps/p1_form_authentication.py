from behave import *
from features.pages.login_page import LoginPage
import time


@given(u'A user goes to the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_login_page()


@when(u'He adds a valid username as "{username}" and password as "{password}" in the form')
def step_impl(context, username, password):
    context.login_page.set_username(username)
    context.login_page.set_password(password)


@when(u'He clicks on the login button')
def step_impl(context):
    context.login_page.click_login_button()
    time.sleep(2)


@then(u'He should be logged in to the system')
def step_impl(context):
    pass


@when(u'He adds an invalid username as "invalid_user" and a valid password as "SuperSecretPassword!" in the form')
def step_impl(context):
     pass


@then(u'The system should display a failed authentication validation message - Your username is invalid!')
def step_impl(context):
    pass


@when(u'He adds a valid username as "tomsmith" and an invalid password as "123" in the form')
def step_impl(context):
    pass


@then(u'The system should display a failed authentication validation message - Your password is invalid!')
def step_impl(context):
    pass


@when(u'He does not add any credentials in the form')
def step_impl(context):
    pass
