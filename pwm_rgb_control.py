import sys, time
import RPi.GPIO as GPIO

def initPinsOut():
    GPIO.setmode(GPIO.BOARD)
    GPIOS = [33,35,37]
    for gpio in GPIOS:
        GPIO.setup(gpio, GPIO.IN)
    
    for gpio in GPIOS:
        print('GPIO no: '+str(gpio)+ ' - '+str(GPIO.input(gpio)))

    GPIO.cleanup()
    return


def main():
    
    print('Here we go')
    initPinsOut()

    redPin   = 33
    greenPin = 35
    bluePin  = 37

    RUNNING = True

    freq = 100

    GPIO.setmode(GPIO.BOARD)
    GPIOS = [33,35,37]
    for gpio in GPIOS:
        GPIO.setup(gpio, GPIO.OUT)

    redPwm = GPIO.PWM(redPin, freq)
    greenPwm = GPIO.PWM(greenPin, freq)
    bluePwm = GPIO.PWM(bluePin, freq)

    try:
        while RUNNING:
            redPwm.start(1)
            greenPwm.start(100)
            bluePwm.start(100)

            ### Change for Red to Green
            for x in range(1,101):
                greenPwm.ChangeDutyCycle(101-x)
                redPwm.ChangeDutyCycle(x)
                time.sleep(.05)

            ### Change from green to blue
            for x in range(1, 101):
                bluePwm.ChangeDutyCycle(101-x)
                greenPwm.ChangeDutyCycle(x)
                time.sleep(.05)

            ### Change from blue to red
            for x in range(1, 101):
                redPwm.ChangeDutyCycle(101-x)
                bluePwm.ChangeDutyCycle(x)
                time.sleep(.05)
          
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        RUNNING = False

    GPIO.cleanup()
    return

main()