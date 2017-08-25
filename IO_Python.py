import time               		# For time delay pupose
import RPi.GPIO as GPIO   		# Import GPIO package as IO

GPIO.setmode(IO.BCM)      		# To Select GPIO representation(IO.BCM/IO.BOARD)
GPIO.setwarnings(False)   		# Clear warning of redeclaration of GPIO
GPIO.setup(4,IO.IN)   
GPIO.setup(2,IO.OUT)      		# To set as output (or) input  
GPIO.output(2,False)      		# Raspberry pi 2 pin is low

try:
    while 1:                    # For Infinite loop purpose
        if GPIO.input(4)==0:
            GPIO.output(2,True) # To set pin is high 
            print "LED 1 ON"    # Display output window in LED 1 ON
        else:       
            GPIO.output(2,False)# To set pin is low 
            print "LED 1 OFF"   # Display output window in LED 1 OFF
except:
    pass
GPIO.cleanup()					# to clean up all the ports used in program

