# flask-echo-server

A simple echo server built with flask.

#### Install
```
↪ python3 setup.py install
```

#### Usage
```
↪ flask-echo -h
Usage: flask-echo [options]

Options:
  -h, --help     show this help message and exit
  --port=PORT    port to run server on - default 5000
  --auth=AUTH    basic authentication credentials
  -v, --verbose  increased verbosity - outputs response to console
  --debug        enable debug mode in flask
```

#### Example
```
↪ flask-echo &
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
↪ http localhost:5000
127.0.0.1 - - [17/Mar/2015 22:11:20] "GET / HTTP/1.1" 200 -
HTTP/1.0 200 OK
Content-Length: 529
Content-Type: application/json
Date: Wed, 18 Mar 2015 03:11:20 GMT
Server: Werkzeug/0.10.1 Python/3.4.0

{
    "args": {},
    "base_url": "http://localhost:5000/",
    "cookies": {},
    "data": "",
    "form": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, compress",
        "Content-Length": "",
        "Content-Type": "",
        "Host": "localhost:5000",
        "User-Agent": "HTTPie/0.8.0"
    },
    "host": "localhost:5000",
    "method": "GET",
    "path": "/",
    "script_root": "",
    "status": 200,
    "success": true,
    "time": 1426648280.7245362,
    "url": "http://localhost:5000/",
    "url_root": "http://localhost:5000/"
}
```

#### Basic Authentication
You can enable basic auth by passing credentials with the command line argument --auth
```
↪ flask-echo --auth username:password
```

#### Request Arguments
Some additional arguments can be passed to change the response behavior.

##### status
```
↪ http 'localhost:5000?status=401'
HTTP/1.0 401 UNAUTHORIZED
...
```
