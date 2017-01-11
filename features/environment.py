
from skeleton_greeter.greeter import app

def before_feature(context, feature):
    context.client = app.test_client()

def before_tag(context, tag):
    app.config['TESTING'] = True

