from flask import Flask, jsonify, request
from werkzeug.routing import Rule
import time
import pprint

app = Flask(__name__)

app.url_map.add(Rule('/', defaults={'path' : ''}, endpoint='index'))
app.url_map.add(Rule('/<path:path>', endpoint='index'))

@app.endpoint('index')
def echo(path):

    data = {
        'success' : True,
        'time' : time.time(),
        'path' : request.path,
        'method' : request.method,
        'headers' : {key: value for (key, value) in request.headers},
        'body' : request.data.decode(encoding='UTF-8'),
        'host' : request.host,
        'queryParams' : request.args
    }

    pprint.pprint(data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)