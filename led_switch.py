from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

IP_ADDRESS = '192.168.0.12' # of your Pi

# Configure the GPIO pin
GPIO.setmode(GPIO.BCM)
RED_PIN = 4

GPIO.setup(RED_PIN, GPIO.OUT)

# Initialize all RGB to OFF
GPIO.output(RED_PIN,GPIO.HIGH)

# Handler for the home page
@route('/')
def index(name='time'):
    return template('home.tpl')

# Handler for the 'rgbled' page
@route('/rgbon', method='POST')
def new_item():
    GPIO.output(RED_PIN,GPIO.LOW)
    return template('home.tpl')

@route('/rgboff', method='POST')
def new_item():
    GPIO.output(RED_PIN,GPIO.HIGH)
    return template('home.tpl')

# Start the webserver running on port 80
try:
    run(host=IP_ADDRESS, port=80)
finally:
    print('Cleaning up GPIO')
    GPIO.cleanup()
