# garageDoor
Open the Garage Door with OrangePi Zero

My remote for the garage door was broken. I found it was the dip switch inside the remote.

Instead of replacing the dip switch, I decided to use the Orange Pi Zero for controlling a relay (relay in place of the dip switch).

So it means now, woth only one remote, everybody at home can control the garage door.

## How to do this?
I use few lines of python to manage a relay. Also, the python script offers a "website" where a button is present: just push the button with
smartphone web app.

We need GPIO for relay control and bootle.py to create a web site.

## GPIO?
Yes. 

sudo apt-get install python-dev to get the last version of python
sudo apt-get install git because we need to grab files from github.
git clone "https://github.com/nvl1109/orangepi_zero_gpio"

cd orangepi_zero_gpio
sudo python setup.py install

### Test the lib
cd examples
sudo python blink_POWER_STATUS_PL10.py

## Website? Bottle!

Bootle is a micro framework for creating small website. 

sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py
sudo pip install bottle


## Runing the code?

Mmm... You can just:
sudo python garageDoor.py

if you want to close the session but continue with the garage door website, use:
nohup sudo python garageDoor.py


Enjoy!





