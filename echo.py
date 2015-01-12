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

def extract(d):
    return {key: value for (key, value) in d.items()}

@app.endpoint('index')
def echo(path):

    status_code = request.args.get('status') or 200
    status_code = int(status_code)

    data = {
        'success' : True,
        'time' : time.time(),
        'path' : request.path,
        'script_root' : request.script_root,
        'url' : request.url,
        'base_url' : request.base_url,
        'url_root' : request.url_root,
        'method' : request.method,
        'headers' : extract(request.headers),
        'data' : request.data.decode(encoding='UTF-8'),
        'host' : request.host,
        'args' : extract(request.args),
        'form' : extract(request.form),
        'cookies' : extract(request.cookies),
    }

    # pprint.pprint(data)

    response = jsonify(data)
    if validate_status_code(status_code):
        response.status_code = status_code

    data['status'] = response.status_code
    return response

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()