from behave import *
from features.pages.login_page import LoginPage


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


@then(u'He should be logged in to the system - the message of "{expected_success_msg_text}" should be displayed')
def step_impl(context, expected_success_msg_text):
    assert context.login_page.check_success_message(expected_success_msg_text)


@when(u'He adds an invalid username as "{username}" and a valid password as "{password}" in the form')
def step_impl(context, username, password):
    context.login_page.set_username(username)
    context.login_page.set_password(password)


@then(u'System displays a failed validation message for username - "{expected_warning_msg_text}"')
def step_impl(context, expected_warning_msg_text):
    assert context.login_page.check_warning_message(expected_warning_msg_text)


@when(u'He adds a valid username as "{username}" and an invalid password as "{password}" in the form')
def step_impl(context, username, password):
    context.login_page.set_username(username)
    context.login_page.set_password(password)


@then(u'System displays a failed validation message for password - "{expected_warning_msg_text}"')
def step_impl(context, expected_warning_msg_text):
    assert context.login_page.check_warning_message(expected_warning_msg_text)