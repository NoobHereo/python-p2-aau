import time as time
from turtle import right
from obis_laser_cotroller import ObisLaserController
from vector2dLib import Vector2D
import numpy as np

class LaserComponent:
    def init():
        time.sleep(5)



class BrushComponent:
    torque = 0
    rpm = 0
    state = False
        
    def off(torque, rpm, state):
        if torque != 0:
            torque = 0
        state = False

    def on(torque, rpm):
        torque = 50
        rpm = 1600
        state = True

class Navigation:
    global rightSpeed
    global leftSpeed
    rightSpeed = np.zeros((2), dtype=np.int16)
    leftSpeed = np.zeros((2), dtype=np.int16)
    
    global drivePattern
    drivePattern = np.array(["f", "l", "f"])

    global i

    class Movement:
        def setSpeed_Direction(leftSpeed, rightSpeed):
            i = 0
            TimeSpeed = np.array([[10, 5, 10],[100, 50, 100]])

            while i < 2:
                if drivePattern[i] == "f":
                    leftSpeed[i] = TimeSpeed[1][i]
                    rightSpeed[i] = TimeSpeed[1][i]
                elif drivePattern[i] == "l":
                    leftSpeed[i] = -TimeSpeed[1][i]
                    rightSpeed[i] = -TimeSpeed[1][i]
            

                motorSpeed = [leftSpeed, rightSpeed]
                time.sleep(TimeSpeed[0, i])
                i += 1

    #class Movement:
    #    global driving
    #    driving = False

    #    def turn(char = 'l'):
            # TODO: Simulate a robot turn action in Webots
            time.sleep(1)

     #   def drive(time = 0):
            # TODO: Drive 0 degrees forward (straight forward)
      #      time.sleep(time)
            # TODO: Stop driving
            
    
class Robot:
    laser = LaserComponent()
    brush = BrushComponent()
    navi = Navigation()


    def main():
        time.sleep(5)
