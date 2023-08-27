from flask import Flask
from flask import request

import requests

app = Flask(__name__)

@app.route('/u')
def u():
    response = requests.get('http://127.0.0.1:3000/users')
    res_json = response.json()

    

    return {
        'наш ответ': res_json
    }

@app.route("/use")
def use():
    response = requests.get("http://127.0.0.1:3000/user/1")
    res_json = response.json()

if __name__ == 'main':

    app.run(port=5000)