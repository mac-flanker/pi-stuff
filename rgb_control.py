import sys, time
import RPi.GPIO as GPIO

class RGBLed:
    
    GPIO.setmode(GPIO.BOARD)

    def __init__(self, rp, gp, bp):
        self.redPin   = rp
        self.greenPin = gp
        self.bluePin  = bp

        self.gpios = [rp,gp,bp]
        GPIO.setmode(GPIO.BOARD)
        for gpio in self.gpios:
            GPIO.setup(gpio, GPIO.IN)
    
        #for gpio in GPIOS:
        #    print('GPIO no: '+str(gpio)+ ' - '+str(GPIO.input(gpio)))
        GPIO.cleanup()

    def _assertLowPin(self, pin):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def _turnOffPin(self, pin):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def redOn(self):
        self._assertLowPin(self.redPin)

    def greenOn(self):
        self._assertLowPin(self.greenPin)

    def blueOn(self):
        self._assertLowPin(self.bluePin)

    def yellowOn(self):
        self._assertLowPin(self.redPin)
        self._assertLowPin(self.greenPin)

    def cyanOn(self):
        self._assertLowPin(self.bluePin)
        self._assertLowPin(self.greenPin)

    def magentaOn(self):
        self._assertLowPin(self.redPin)
        self._assertLowPin(self.bluePin)


    def redOff(self):
        self._turnOffPin(self.redPin)
        GPIO.cleanup()

    def greenOff(self):
        self._turnOffPin(self.greenPin) 
        GPIO.cleanup()


    def blueOff(self):
        self._turnOffPin(self.bluePin)

    def yellowOff(self):
        self._turnOffPin(self.redPin)
        self._turnOffPin(self.greenPin)

    def cyanOff(self):
        self._turnOffPin(self.bluePin)
        self._turnOffPin(self.greenPin)

    def magentaOff(self):
        self._turnOffPin(self.redPin)
        self._turnOffPin(self.bluePin) 
        GPIO.cleanup()


#rgb_led = RGBLed(33,35,37)

#rgb_led.greenOn()
#time.sleep(3)
#rgb_led.greenOff()

    