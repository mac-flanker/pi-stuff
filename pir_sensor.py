import sys, time
import RPi.GPIO as GPIO
import rgb_control


def initPinsOut():
    GPIO.setmode(GPIO.BOARD)
    GPIOS = [11]
    for gpio in GPIOS:
        GPIO.setup(gpio, GPIO.IN)
    
    for gpio in GPIOS:
        print('GPIO no: '+str(gpio)+ ' - '+str(GPIO.input(gpio)))

    GPIO.cleanup()
    return

def main():

    GPIO.setmode(GPIO.BOARD)
    sensorOut = 11
    GPIO.setup(sensorOut, GPIO.IN)
    preVal    = GPIO.input(sensorOut)

    RUNNING   = True
    rgb_led   = rgb_control.RGBLed(33,35,37)
    print(str(preVal))
    if preVal == 0:
      print('Zero')


    try:
        while RUNNING:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(sensorOut, GPIO.IN)
            curVal = GPIO.input(sensorOut)

            if curVal == 1:
                rgb_led.redOn()
                if curVal != preVal:
                    print('New motion detected')

            else:
                rgb_led.redOff()
            
            preVal = curVal
    except Exception as e:
        print(e)
        reg_led.redOff()
        RUNNING = False
        GPIO.cleanup()
    except KeyboardInterrupt:
        rgb_led.redOff()
        RUNNING = False
        GPIO.cleanup()
    return


initPinsOut()
main()

