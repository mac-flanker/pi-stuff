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

    RUNNING   = True
    rgb_led   = rgb_control.RGBLed(33,35,37)
    sensorOut = 11
    preVal    = GPIO.input(sensorOut)

    try:
        while RUNNING:
            curVal = GPIO.input(sensorOut)

            if curVal == 1:
                rgb_led.redOn
                if curVal != preVal:
                    print('New motion detected')

            else:
                rgb_led.redOff
            
            preVal = curVal
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        RUNNING = False
    
    GPIO.cleanup()
    return


main()