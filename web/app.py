from wsgiref.simple_server import make_server

def web_app(environment, response):

    # for status it must be 4 char long
    status = "200 OK"
    headers = [("Content-type", "text/html; charet=utf-8")]

    response(status, headers)

    return [b'<strong>Hello, This is my first WSGI</strong>']

with make_server('', 8000, web_app) as our_server:
    print("serving on port 8000\nTo kill the server press CRL+C")

    our_server.serve_forever()