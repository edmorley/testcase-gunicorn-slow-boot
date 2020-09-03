import time

print('test.py start')
time.sleep(40)

def app(environ, start_response):
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

print('test.py finish')
