"""EpuckForward controller."""
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor

# Initiate variables
global TIME_STEP; TIME_STEP = 32
MaxSpeed = 6.28

# create the Robot instance.
robot = Robot()

# get a handler to the motors and set target position to infinity (speed control).
leftMotor = robot.getDevice('left wheel motor'); rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf')); rightMotor.setPosition(float('inf'))

# set up the motor to drive at 20% of the maximum speed.

# Create instance for the sensors
distanceSensorLeft = robot.getDevice('ps0'); distanceSensorLeft.enable(TIME_STEP)
distanceSensorRight = robot.getDevice('ps7'); distanceSensorRight.enable(TIME_STEP)

# Directional drive commands





class Movement:
    def left():
        leftMotor.setVelocity(-MaxSpeed); rightMotor.setVelocity(MaxSpeed)
    def right():
        leftMotor.setVelocity(MaxSpeed); rightMotor.setVelocity(-MaxSpeed)
    def forward():
        leftMotor.setVelocity(0.2 *MaxSpeed); rightMotor.setVelocity(0.2 *MaxSpeed)
    def backward():
        leftMotor.setVelocity(0.2 * -MaxSpeed); rightMotor.setVelocity(0.2 * -MaxSpeed)

Move = Movement()

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:

    
    # Read the sensors:
    dsleft = distanceSensorLeft.getValue(); dsright = distanceSensorRight.getValue()
    
    # Process sensor data here.
    dsDiff = dsleft - dsright; print(dsDiff)
    dsComp = dsleft + dsright; print(dsComp)
    print("left sensor: " + str(dsleft)); print("Right sensor: " + str(dsright))
    
    # Send actuator commands here.
    # All code from this point on makes it move forward only
    # Needs to be fixed. 
    if dsDiff > 10:
        Move.right()
    elif dsDiff < -10:
        Move.left() 
    elif dsComp > 160:
        Move.right()
    else:
        Move.forward()
    

    print("Hello 1")
    if robot.step(TIME_STEP) == -1: print("End of simulation"); break
# Enter here exit cleanup code.