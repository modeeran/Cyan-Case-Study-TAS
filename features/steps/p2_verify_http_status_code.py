from behave import *
from features.pages.status_codes_page import StatusPage


@given(u'A user goes to the Status Codes page')
def step_impl(context):
    context.driver.status_codes_page = StatusPage(context.driver)
    context.driver.status_codes_page.navigate_status_code_page()


@when(u'He selects a statusCode link as "{link}" and  navigates to the corresponding sub-page')
def step_impl(context, link):
    context.driver.status_codes_page.select_status_code_link(link)


@then(u'the correct http statusCode as "{statuscode:n}" should be returned per sub-page')
def step_impl(context, statuscode):
    assert context.driver.status_codes_page.collect_http_status_code(statuscode)
