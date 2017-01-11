from behave import *

@when("service alive")
def service_alive(context):
    assert context.client

@then("greet hello world when calling api")
def greet(context):
    response = context.client.get('http://localhost:5000/greet?name=amazia')
    assert response.data == 'hello world from flask amazia'
