from bottle import route, run, get, post, request, redirect

from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import socket

# Define and initiate GPIO
relay = port.PA6
gpio.init()
gpio.setcfg(relay, gpio.OUTPUT)
gpio.output(relay, gpio.LOW) # we start at LOW

# Grab the IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
ipAddress = s.getsockname()[0]
s.close()

@get('/opendoor') #
def login():
    return '''
        <form action="/login" method="post">
            <font size="10"><center>This is the open page!</center><hr>
            <div title="hit the button to open">
                <button style="text-align:center;font-size:80px" type="submit"> Open door </button>
            </div /font>
        </form>
    '''
@post('/opendoor') # 

def do_login():
    gpio.output(relay, gpio.HIGH)
    sleep(1)
    gpio.output(relay, gpio.LOW)
    redirect('/login')

run(host=ipAddress, port=8080, debug=True) # we use thez IP address grabbed before and port 8080
