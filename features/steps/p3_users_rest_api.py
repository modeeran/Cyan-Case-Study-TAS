from behave import *
import requests


@given(u'The API "{endpoint}" returns a response of users details')
def step_impl(context, endpoint):
    context.endpoint = endpoint


@when(u'There is a GET request to the users endpoint')
def step_impl(context):
    context.response = requests.get(context.endpoint)
    context.json_data = context.response.json()


@then(u'Verify that user as "{user}" exists')
def step_impl(context, user):
    """
    It returns a list of matching items for the given key and value. The list can be empty or non-empty.
    """
    context.filter_data = list(filter(lambda json_data: json_data['name'] == user, context.json_data))
    if context.filter_data:
        if len(context.filter_data) == 1:
            context.specific_user_data = context.filter_data[0]
            assert user == context.specific_user_data['name']
        else:
            raise Exception("There are more than 1 instance for the searched name")
    else:
        raise Exception("The searched name does not exist!")


@then(u'verify that if this user exists, his address contains the following data')
def step_impl(context):
    context.specific_user_address_data = context.specific_user_data['address']
    if context.specific_user_address_data:
        context.specific_user_geo_data = context.specific_user_address_data['geo']
        address_keys = ['street', 'suite', 'city', 'zipcode']
        geo_keys = ['lat', 'lng']
        for i in context.table:
            for key in address_keys:
                assert context.specific_user_address_data[key] == i[key], f"Key {key} does not match"
            for key in geo_keys:
                assert context.specific_user_geo_data[key] == i[key], f"Key {key} does not match"
    else:
        raise Exception("The address data is not available")
