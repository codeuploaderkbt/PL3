# ASSIGNMENT NO.:13		BATCH NO.:T		ROLL NO.:
# TITLE :
#	Develop Robotics(stepper motor) Application using Beagle Board.


#!/usr/bin/python 
 
# Import standard python libraries
import sys
import os
import time
from array import*

# Import GPIO part of Adafruit BBIO Library
import Adafruit_BBIO.GPIO as GPIO
# Import ADC part of Adafruit BBIO Library
import Adafruit_BBIO.ADC as ADC


# GPIO Pin definitions for Stepper Interfacing Board 


STEPPER_1   =    "P9_11"
STEPPER_2   =    "P8_7"
STEPPER_3   =    "P9_12"
STEPPER_4   =    "P8_8"
 	
MOTOR_EN    =    "P8_9"
ARM_ON	    =    "P9_26"	
ARM_STOP    =    "P8_17"
MAGNET_CTL  =    "P9_13"

START_ANGLE  = 30
STOP_ANGLE   = 120


# This function turns the Motor COntrol ON or OFF."1" will turn it ON and "0" will turn it OFF


def MOTOR_Control(val):
	GPIO.setup(MOTOR_EN, GPIO.OUT)
	if (val == "1"):
		GPIO.output(MOTOR_EN, GPIO.HIGH)
	else:
		GPIO.output(MOTOR_EN, GPIO.LOW)
	return 


# This function turns the stepper PIN ON .It will setup a PIN as GPIO, sets the direction as OUT and then makes the PIN high   
# @pin = Pin No associated with LED

def Stepper(pin, val):
	GPIO.setup(pin, GPIO.OUT)
	if (val == "1"):
		GPIO.output(pin, GPIO.HIGH)
	else:
		GPIO.output(pin, GPIO.LOW)
	return 


# This function writes the sequence on stepper motor pins. While writing start from LSB, hence LSB goes to stepper pin #1 	 


global NXT_STEP
STEP = array('i',[8,10,2,6,4,5,1,9])
stp_cnt=0
NXT_STEP = STEP[0]

def REV_StepMotor(val):
	global stp_cnt
	#CUR_STEP = STEP[stp_cnt]
	MOTOR_Control("0")
	Stepper(STEPPER_1, val[3])
	Stepper(STEPPER_2, val[2])
	Stepper(STEPPER_3, val[1])
	Stepper(STEPPER_4, val[0])
	MOTOR_Control("1")
	stp_cnt+=1
	NXT_STEP = STEP[stp_cnt]		
	#print "%d" %NXT_STEP
	if(stp_cnt ==7):
		stp_cnt = 0
	return NXT_STEP 


def FW_StepMotor(val):
	global stp_cnt
	#CUR_STEP = STEP[stp_cnt]
	MOTOR_Control("0")
	Stepper(STEPPER_1, val[3])
	Stepper(STEPPER_2, val[2])
	Stepper(STEPPER_3, val[1])
	Stepper(STEPPER_4, val[0])
	MOTOR_Control("1")
	NXT_STEP = STEP[7-stp_cnt]		
	#print "%d" %NXT_STEP
	stp_cnt+=1
	if(stp_cnt>7):
		stp_cnt = 0
	#print "%d" %stp_cnt
	return NXT_STEP 
#main

GPIO.setup(ARM_ON, GPIO.IN)
GPIO.setup(ARM_STOP, GPIO.IN)
GPIO.setup(MAGNET_CTL, GPIO.OUT)

while True:
	while(GPIO.input(ARM_STOP)):
			#print "Main NXT STEP = %d" %NXT_STEP
			stp_seq = str('{:04b}'.format(NXT_STEP))
			NXT_STEP = REV_StepMotor(stp_seq)
			time.sleep(0.1)			# pause
	time.sleep(1)			# pause	
	print "\nRoboticARM is INITIALIZING @ angle = ", START_ANGLE, "\n"	
	for i in range(0,START_ANGLE):  
			print "RoboticARM is STARTED @ angle ", START_ANGLE
			stp_seq = str('{:04b}'.format(NXT_STEP))
			NXT_STEP = FW_StepMotor(stp_seq)
			time.sleep(0.1)			# pause
	time.sleep(1)			# pause		
	GPIO.output(MAGNET_CTL, GPIO.HIGH)
	print "\nPicking object, please wait...\n"
	time.sleep(2)			# pause
	print "\nObject PICKED\n"		
	for i in range(START_ANGLE+1, STOP_ANGLE):
			print "RoboticARM is MOVED @ angle = ", START_ANGLE , "upward to @ angle = " , STOP_ANGLE
			stp_seq = str('{:04b}'.format(NXT_STEP))
			NXT_STEP = FW_StepMotor(stp_seq)
			time.sleep(0.1)			# pause
	GPIO.output(MAGNET_CTL, GPIO.LOW)
	print "\nDropping object, please wait...\n"
	time.sleep(50)			# pause	
	print "\nObject DROPPED\n"	
	print "RoboticARM is STOPPED @ angle = ", STOP_ANGLE, "\n\n"
	exit()


'''
------------------------------------------------------------------------------------------
OUTPUT:

root@beaglebone:/home# clear

root@beaglebone:/home# python ra.py

RoboticARM is INITIALIZING @ angle =  30 

RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30
RoboticARM is STARTED @ angle  30

Picking object, please wait...


Object PICKED

RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120
RoboticARM is MOVED @ angle =  30 upward to @ angle =  120

Dropping object, please wait...


Object DROPPED

RoboticARM is STOPPED @ angle =  120 


root@beaglebone:/home#
'''
