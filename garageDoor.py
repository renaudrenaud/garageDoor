from bottle import route, run, get, post, request, redirect

from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

relay = port.PA6
gpio.init()
gpio.setcfg(relay, gpio.OUTPUT)
gpio.output(relay, gpio.LOW)

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

run(host='192.168.1.103', port=8080, debug=True)
