from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    return 'hello world from flask ' + name

if __name__ == '__main__':
    app.run(debug=True)