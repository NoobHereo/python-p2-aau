"""EpuckForward controller."""
# Import different libraries
import time as time
from typing import Counter

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

global TIME_STEP
TIME_STEP = 10
MaxSpeed = 6.28
global counter
counter = 0

# create the Robot instance.
robot = Robot()

# get a handler to the motors and set target position to infinity (speed control).
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# set up the motor to drive at 20% of the maximum speed.

# Create instance for the sensors
distanceSensorLeft = robot.getDevice('ps0')
distanceSensorLeft.enable(TIME_STEP)
distanceSensorRight = robot.getDevice('ps7')
distanceSensorRight.enable(TIME_STEP)

#Create passive delay
def passiveWait():
    global counter
    while True:
        print(counter)
        counter += 1
        if counter == 10000:
            break

passiveWait()



# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    passiveWait()
    # Read the sensors:
    dsleft = distanceSensorLeft.getValue()    
    dsright = distanceSensorRight.getValue()
    # Process sensor data here.
    dsDiff = dsleft - dsright
    print("left sensor: " + str(dsleft))
    print("Right sensor: " + str(dsright))

    # Send actuator commands here.
    rightMotor.setVelocity(0.2 * MaxSpeed)
    leftMotor.setVelocity(0.2 * -MaxSpeed)
    print("left motor: " + str(leftMotor.getVelocity()))
    print("right motor: " + str(rightMotor.getVelocity()))
    passiveWait()
    break
    rightMotor.setVelocity(0.2 * MaxSpeed)
    leftMotor.setVelocity(0.2 * MaxSpeed)
    passiveWait()

    if robot.step(TIME_STEP) == -1:
        print("End of simulation")
        break
# Enter here exit cleanup code.