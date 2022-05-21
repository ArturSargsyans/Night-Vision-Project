import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import random
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

camera = PiCamera()
camera.rotation = 180

imnum=0
vidnum=0
imname = 'image'
vidname = 'video'
rec_state = 0

def capture(pin):
	global imnum
	global imname
	camera.capture(imname+str(imnum)+'.jpg')
	imnum=imnum+1

def record(pin):
	global rec_state
	global vidnum
	global vidname
	if rec_state == 0:
		camera.start_recording(vidname+str(vidnum)+'.h264')
		camera.annotate_text = "Recording started" 
		vidnum=vidnum+1
		rec_state = 1
	else:
		camera.stop_recording()
		camera.annotate_text = " "
		rec_state = 0

def shutDown(pin):
	os.system("sudo shutdown -h now")

GPIO.add_event_detect(4, GPIO.FALLING, callback=record, bouncetime=300)
GPIO.add_event_detect(27,GPIO.FALLING, callback=capture, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=shutDown, bouncetime=300)



camera.start_preview()

while True:
	sleep(2)
	a = int(input("watiing"))
	if(a==3):
		break

camera.stop_preview()
