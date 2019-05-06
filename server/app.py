from flask import Flask, request
from utils import *
from json import loads

app = Flask(__name__)


@app.route('/optimize', methods=["POST"])
def hello_world():
    inp = request.json
    Voice, Sms, Data = inp['Voice'], inp['Sms'], inp['Data']
    return answer_formatter(optimize(Voice, Sms, Data))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
