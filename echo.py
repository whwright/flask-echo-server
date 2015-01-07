from flask import Flask, jsonify, request
import time
import pprint

app = Flask(__name__)

@app.route('/', defaults={'path' : ''}, methods=('GET', 'POST', 'PUT', 'DELETE'))
@app.route('/<path:path>', methods=('GET', 'POST', 'PUT', 'DELETE'))
def echo(path):

    data = {
        'time' : time.time(),
        'path' : request.path,
        'method' : request.method,
        'headers' : {key: value for (key, value) in request.headers},
        'data' : request.data.decode(encoding='UTF-8'),
        'host' : request.host
    }

    pprint.pprint(data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)