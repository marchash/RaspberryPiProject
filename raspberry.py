import RPi.GPIO as GPIO
 
#GPIO.BOARD is to use the numbers from pin order, while GPIO.BCM is to use port order. See image for reference.
GPIO.setmode(GPIO.BOARD)
#Input and output
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
#Loop to detect button pressing to turn LED on/off
While(True):
    if GPIO.input == False:
         GPIO.output(12,1)
    if GPIO.output == True:
         GPIO.output(12,0)