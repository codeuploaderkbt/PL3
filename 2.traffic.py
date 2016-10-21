
 
# Import standard python libraries 
import sys
import time



LED_1	=	(0 * 32) + 3		
LED_2	=	(0 * 32) + 23		
LED_3	=	(0 * 32) + 2		
LED_4	=	(0 * 32) + 26		

LED_5	=	(1 * 32) + 17		
LED_6	=	(1 * 32) + 15		
LED_7	=	(0 * 32) + 15		
LED_8	=	(1 * 32) + 14		

LED_9	=	(0 * 32) + 14		
LED_10	=	(0 * 32) + 27		
LED_11	=	(0 * 32) + 22		
LED_12	=	(2 * 32) + 1	

NORTH_GREEN		=	LED_1
NORTH_YELLOW		=	LED_5
NORTH_RED		=	LED_9

EAST_GREEN		=	LED_2
EAST_YELLOW		=	LED_6
EAST_RED		=	LED_10

SOUTH_GREEN		=	LED_3
SOUTH_YELLOW		=	LED_7
SOUTH_RED		=	LED_11

WEST_GREEN		=	LED_4
WEST_YELLOW		=	LED_8
WEST_RED		=	LED_12

# PATH of a GPIO specific sysfs interfce directory on Linux system 
SYSFS_GPIO_DIR = "/sys/class/gpio"

def gpioExport (gpio): 
	try:
   		fo = open(SYSFS_GPIO_DIR + "/export","w")  
   		fo.write(gpio)
   		fo.close()
   		return
   	except IOError:
                return


def gpioUnexport (gpio):
	try: 
   		fo = open(SYSFS_GPIO_DIR + "/unexport","w")  
   		fo.write(gpio)
   		fo.close()
   		return
   	except IOError:
 		return

def gpioSetDir (gpio, flag):
	try: 
	   	fo = open(SYSFS_GPIO_DIR + "/gpio" + gpio + "/direction" ,"w")  
	   	fo.write(flag)
	   	fo.close()
	   	return
 	except IOError:
                return


def gpioSetVal (gpio, val):
	try: 
		fo = open(SYSFS_GPIO_DIR + "/gpio" + gpio + "/value" ,"w")  
		fo.write(val)
		fo.close()
		return
	except IOError:
                return


def lightExit (gpio):
	gpioSetVal(gpio, val="0")
	gpioUnexport(gpio)
	return 


def lightInit (gpio):
	gpioExport(gpio)
	gpioSetDir(gpio, flag="out")
 	gpioSetVal(gpio, val="0")
 	return


 	
def lightOn (gpio):
	gpioSetVal(gpio, val="1")
	return 


	
def lightOff (gpio):
	gpioSetVal(gpio, val="0")
	return 
	

def trafficInitAll():
	lightInit(str(NORTH_GREEN))
	lightInit(str(NORTH_YELLOW))
	lightInit(str(NORTH_RED))
	lightInit(str(EAST_GREEN))
	lightInit(str(EAST_YELLOW))
	lightInit(str(EAST_RED))
	lightInit(str(SOUTH_GREEN))
	lightInit(str(SOUTH_YELLOW))
	lightInit(str(SOUTH_RED))
	lightInit(str(WEST_GREEN))
	lightInit(str(WEST_YELLOW))
	lightInit(str(WEST_RED))
	return	



def trafficExitAll():
	lightExit(str(NORTH_GREEN))
	lightExit(str(NORTH_YELLOW))
	lightExit(str(NORTH_RED))
	lightExit(str(EAST_GREEN))
	lightExit(str(EAST_YELLOW))
	lightExit(str(EAST_RED))
	lightExit(str(SOUTH_GREEN))
	lightExit(str(SOUTH_YELLOW))
	lightExit(str(SOUTH_RED))
	lightExit(str(WEST_GREEN))
	lightExit(str(WEST_YELLOW))
	lightExit(str(WEST_RED))
	return	



def northSouthOn():
	lightOff(str(EAST_YELLOW))
	lightOff(str(WEST_YELLOW))
	lightOff(str(NORTH_RED))
	lightOff(str(SOUTH_RED))

	lightOn(str(EAST_RED))
	lightOn(str(WEST_RED))

	lightOn(str(NORTH_GREEN))
	lightOn(str(SOUTH_GREEN))

	time.sleep(10)

	lightOff(str(NORTH_GREEN))
	lightOff(str(SOUTH_GREEN))

	lightOn(str(NORTH_YELLOW))
	lightOn(str(SOUTH_YELLOW))
	time.sleep(1)
	return


def eastWestOn():
	lightOff(str(NORTH_YELLOW))
	lightOff(str(SOUTH_YELLOW))
	lightOff(str(EAST_RED))
	lightOff(str(WEST_RED))

	lightOn(str(NORTH_RED))
	lightOn(str(SOUTH_RED))

	lightOn(str(EAST_GREEN))
	lightOn(str(WEST_GREEN))

	time.sleep(10)

	lightOff(str(EAST_GREEN))
	lightOff(str(WEST_GREEN))

	lightOn(str(EAST_YELLOW))
	lightOn(str(WEST_YELLOW))
	time.sleep(1)
	return
	
	
try:		
	print "\nTraffic Signal Light Simulation using Python"
	print "-----------------------------------------------"
	trafficExitAll()				# Cleanup all the LED GPIOs first
	trafficInitAll()				# Initialize all LEDs and Turn them OFF
	for x in range(0, 10):					
		print "\nNORTH-SOUTH	--> [GO]"		
		print "EAST-WEST 	--> [STOP]\n"		
		northSouthOn()				# Call function to make NORTH-SOUTH traffic ON
		time.sleep(1)					
		print "\nEAST-WEST	--> [GO]"	
		print "NORTH-SOUTH 	--> [STOP]\n"	
		eastWestOn()				# Call function to make EAST-WEST traffic ON
		time.sleep(1)					

	trafficExitAll()					 
	print "done"						
	exit()							
except KeyboardInterrupt:  
	trafficExitAll()	
	print "Program Exit due to CTRL-C"
	exit()
    	sys.exit(0)

####
#********************************************************
#Output:-
#Terminal 1:-

#comp-sl-22@compsl22-OptiPlex-3020:~$ scp traffic.py root@192.168.7.2:/home
#Debian GNU/Linux 7

#BeagleBoard.org BeagleBone Debian Image 2014-04-23

#Support/FAQ: http://elinux.org/Beagleboard:BeagleBoneBlack_Debian
#elevator.py                                   100%   20KB  20.1KB/s   00:00    
#comp-sl-22@compsl22-OptiPlex-3020:~$ 

#********************************************************
#Terminal 2:-

#comp-sl-22@compsl22-OptiPlex-3020:~$ ssh root@192.168.7.2
#Debian GNU/Linux 7

#BeagleBoard.org BeagleBone Debian Image 2014-04-23

#Support/FAQ: http://elinux.org/Beagleboard:BeagleBoneBlack_Debian
#Last login: Wed Apr 23 20:29:15 2014 from 192.168.7.1
#root@beaglebone:~# python traffic.py

#Traffic Signal Light Simulation using Python
#-----------------------------------------------

#NORTH-SOUTH	--> [GO]
#EAST-WEST 	--> [STOP]


#EAST-WEST	--> [GO]
#NORTH-SOUTH 	--> [STOP]

#done
#root@beaglebone:~# 



