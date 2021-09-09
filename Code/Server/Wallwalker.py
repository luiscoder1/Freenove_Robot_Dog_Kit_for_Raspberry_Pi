from Control import *
from Ultrasonic import *

ultrasonic=Ultrasonic()

control=Control()


while(True):
    Distance=ultrasonic.getDistance()
    if Distance < 30:
        control.relax(flag=True)
        break
        
    else:
        control.forWard()
        print(Distance)
        
    