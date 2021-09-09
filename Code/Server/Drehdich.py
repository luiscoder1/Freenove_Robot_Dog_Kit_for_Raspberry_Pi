from Control import *
from Ultrasonic import *

ultrasonic=Ultrasonic()

control=Control()
control.speed=30

while(True):
    Distance=ultrasonic.getDistance()
    if Distance < 40:
        for i in range(10):
            control.turnRight()
        
        
    else:
        control.forWard()
        print(Distance)
        
