from Mercury import * 
import RPi.GPIO as io
from time import sleep
import random
import time

def flashGreenLED():
        io.output(green_led_io_pin, io.LOW)
        sleep(0.05)
        io.output(green_led_io_pin, io.HIGH)
        sleep(0.05)
        io.output(green_led_io_pin, io.LOW)
        sleep(0.05)
        io.output(green_led_io_pin, io.HIGH)
        sleep(0.05)
        io.output(green_led_io_pin, io.LOW)
        sleep(0.05)
        io.output(green_led_io_pin, io.HIGH)

def flashRedLED():
        io.output(red_led_io_pin, io.LOW)
        sleep(0.05)
        io.output(red_led_io_pin, io.HIGH)
        sleep(0.05)
	io.output(red_led_io_pin, io.LOW)
        sleep(0.05)
        io.output(red_led_io_pin, io.HIGH)
        sleep(0.05)
        io.output(red_led_io_pin, io.LOW)
        sleep(0.05)
        io.output(red_led_io_pin, io.HIGH)

def turnLEDOff():
	io.output(red_led_io_pin, io.HIGH)
	io.output(green_led_io_pin, io.HIGH)

io.setwarnings(False)
io.setmode(io.BCM)

red_led_io_pin = 5 
green_led_io_pin = 12
total_transactions = 0
total_time = 0
average_time_per_transaction = 0

io.setup(red_led_io_pin, io.OUT)
io.setup(green_led_io_pin, io.OUT)

turnLEDOff()

for count in range(0,10):
	total_transactions = total_transactions + 1
	amount = float("{0:.2f}".format(random.uniform(1,10)))

	start = time.clock()
	x = Mercury(amount)
	x.doCall()
	elapsed = time.clock() - start
	total_time = total_time + elapsed
	average_time_per_transaction = total_time / total_transactions

	print
	print elapsed
	print total_transactions
	print average_time_per_transaction
	print
	print x.authorize_response
	print x.cmdStatus_response

	if x.cmdStatus_response == 'Approved':
		flashGreenLED()	
	else:
		flashRedLED()

	sleep(0.5)

	if elapsed > 0.5:
		flashRedLED()	
	else:
		flashGreenLED()

	sleep(1)
