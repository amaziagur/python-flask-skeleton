from flask import Flask
from flask import request

from skeleton_greeter.clock import clock
from skeleton_greeter.message_manager import messageManager

GREETING_MSG = 'hello world from flask'

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return messageManager(request.args.get('name'),
                          clock(app.config['TESTING'] )).message()

if __name__ == '__main__':
    app.run(debug=True)