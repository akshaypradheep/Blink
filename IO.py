import time             		# For time delay pupose
import RPi.GPIO as GPIO   		# Import GPIO package as IO

GPIO.setmode(GPIO.BCM)      	# To Select GPIO representation(IO.BCM/IO.BOARD)
GPIO.setwarnings(False)   		# Clear warning of redeclaration of GPIO
GPIO.setup(2,GPIO.OUT)      	# To set as output (or) input  
GPIO.output(2,False)      		# Raspberry pi 2 pin is low

try:
    while 1:                	# For Infinite loop purpose
        print "LED ON"          # Display "LED ON"  in output window
        GPIO.output(2,True)		# To set pin is high 
        time.sleep(1)			# wait for 1 second

        print "LED OFF"         # Display "LED OFF" in output window
        GPIO.output(2,False)	# To set pin is low
        time.sleep(1)			# wait for one second
		
except:
    pass
GPIO.cleanup()					# to clean up all the ports used in program