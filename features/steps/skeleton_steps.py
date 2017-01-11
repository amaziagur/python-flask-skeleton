from behave import *

GREET_DOMAIN = 'http://localhost:5000/greet'

HELLO_WORLD_FROM_FLASK = 'hello world from flask'


@when("service alive")
def service_alive(context):
    assert context.client

@then("greet hello world when calling api")
def greet(context):
    response = context.client.get('%s' % GREET_DOMAIN)
    assert response.data == ('%s' % HELLO_WORLD_FROM_FLASK)

@then('greet personally given {name}')
def greet_with_name(context, name):
    response = context.client.get('%s?name=%s' % (GREET_DOMAIN, name))
    assert response.data == '%s %s' %(HELLO_WORLD_FROM_FLASK, name)


@then("greet zzz when clock between 14 and 16")
def greet_zzz_at_noon_time(context):
    response = context.client.get('%s' % GREET_DOMAIN)
    assert response.data == 'zzz'