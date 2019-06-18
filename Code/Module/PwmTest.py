import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

#channel, frequency
p = GPIO.PWM(12, 63)
p.start(9.4)
time.sleep(2)
#rapport cyclique
#9.4 = 1.56ms(9 = 1.50ms)
#10 = 1.66ms, 11 = 1.82ms, 10.1 = 1.68ms, 10.2 = 1.70ms
p.start(9.95)
        

raw_input('entre stop')
p.stop()
GPIO.cleanup