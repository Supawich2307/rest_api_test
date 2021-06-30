import flask
from flask.globals import request
app = flask.Flask(__name__)

@app.route('/HelloWorld',methods=['GET'])
def hello():
    return "Hello "+request.values.get('name')

@app.route('/Calculate',methods=['POST'])
def cal():
    number = request.get_json()
    num1 = number.get('num1')
    num2 = number.get('num2')
    result = int(num1)+int(num2)
    return str(result)
