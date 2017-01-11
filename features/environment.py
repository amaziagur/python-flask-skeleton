
from skeleton_greeter.greeter import app

def before_feature(context, feature):
    app.config['TESTING'] = True
    context.client = app.test_client()
