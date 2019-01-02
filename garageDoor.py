from bottle import route, run, get, post, request, redirect

from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import socket

relay = port.PA6
gpio.init()
gpio.setcfg(relay, gpio.OUTPUT)
gpio.output(relay, gpio.LOW)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
ipAddress = s.getsockname()[0]
s.close()


@route('/hello')
def hello():
    return "Hello World!"


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            <input value="Open Door Garage" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    gpio.output(relay, gpio.HIGH)
    sleep(1)
    gpio.output(relay, gpio.LOW)
    redirect('/login')

run(host=ipAddress, port=8080, debug=True)
