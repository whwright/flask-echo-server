from flask import Flask, jsonify, request
from werkzeug.routing import Rule
import time
import pprint

app = Flask(__name__)

app.url_map.add(Rule('/', defaults={'path' : ''}, endpoint='index'))
app.url_map.add(Rule('/<path:path>', endpoint='index'))

def validate_status_code(status_code):
    if status_code < 600:
        return True
    return False

@app.endpoint('index')
def echo(path):

    status_code = request.args.get('status') or 200
    status_code = int(status_code)

    data = {
        'success' : True,
        'time' : time.time(),
        'path' : request.path,
        'method' : request.method,
        'headers' : {key: value for (key, value) in request.headers},
        'body' : request.data.decode(encoding='UTF-8'),
        'host' : request.host,
        'queryParams' : request.args,
        'status' : status_code
    }

    # pprint.pprint(data)

    response = jsonify(data)
    if validate_status_code(status_code):
        response.status_code = status_code

    return response

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()