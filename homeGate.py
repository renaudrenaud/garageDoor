#
# Garage Door
#
#

from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
relay = port.PA6
gpio.init()
gpio.setcfg(relay, gpio.OUTPUT)
sleep(1)
gpio.output(relay, gpio.LOW)
sleep(1)
gpio.output(relay, gpio.HIGH)