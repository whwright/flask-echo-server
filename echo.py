from flask import Flask, jsonify, request
from werkzeug.routing import Rule
from optparse import OptionParser
from pprint import pprint
import time

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
    if not validate_status_code(status_code):
        status_code = 200

    data = {
        'success' : True,
        'status' : status_code,
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
        'cookies' : extract(request.cookies)
    }

    if app.config['VERBOSE']:
        pprint(data)

    response = jsonify(data)
    response.status_code = status_code
    return response

def main():
    parser = OptionParser()
    parser.add_option('--port', dest='port', default=5000, help='port to run server on - default 5000')
    parser.add_option('-v', '--verbose', dest='verbose',
        default=False, action='store_true', help='increased verbosity - outputs response to console')
    parser.add_option('--debug', dest='debug',
        default=False, action='store_true', help='enable debug mode in flask')
    (options, args) = parser.parse_args()
    app.debug = options.debug
    app.config['VERBOSE'] = options.verbose
    app.run(port=int(options.port))

if __name__ == '__main__':
    main()