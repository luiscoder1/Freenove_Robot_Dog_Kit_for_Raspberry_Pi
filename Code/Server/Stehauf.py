#from Control import *
#from Servo import *
#servo=Servo()
import Adafruit_PCA9685

#control=Control()
def map(value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

pwm = Adafruit_PCA9685.PCA9685()   
pwm.set_pwm_freq(50)

angle=90
date=map(angle,0,180,102,512)
pwm.set_pwm(4, 0, int(date))
angle=90
date=map(angle,0,180,102,512)
pwm.set_pwm(7, 0, int(date))
#servo.setServoAngle(4,0)