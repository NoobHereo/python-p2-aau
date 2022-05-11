"""PyController controller."""
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import time

if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    

    class Data:
        timestep = 64
        maxSpeed = 6.28
        numSide = 4
        lengthSide = 1
        wheelRadius = 0.1
        wheelDistance = 0.46

    data = Data()

    #created motor instances
    redLed = robot.getDevice('led')
    LeftMotor = robot.getDevice('left_motor')
    RightMotor = robot.getDevice('right_motor')
    
    LeftMotor.setPosition(float('inf'))
    LeftMotor.setVelocity(0.0)
    
    RightMotor.setPosition(float('inf'))
    RightMotor.setVelocity(0.0)
    
    linearVelocity = data.wheelRadius * data.maxSpeed
    
    durationSide = data.lengthSide/linearVelocity
    
    startTime = robot.getTime()
    
    angleOfRotation = 6.28/data.numSide

    rateOfRotation = (2 * linearVelocity)/data.wheelDistance
    durationTurn = angleOfRotation/rateOfRotation
    
    
    rotStartTime = startTime + durationSide
    rotEndTime = rotStartTime + durationTurn
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(data.timestep) != -1:
        
        currentTime = robot.getTime()
        
        leftSpeed = data.maxSpeed
        rightSpeed = data.maxSpeed
        
        
        if rotStartTime < currentTime < rotEndTime:
            leftSpeed = -data.maxSpeed
            rightSpeed = data.maxSpeed
            redLed.set(1)
            
        elif currentTime > rotEndTime:
            rotStartTime = currentTime + durationSide
            rotEndTime = rotStartTime + durationTurn
            redLed.set(0)

        LeftMotor.setVelocity(leftSpeed)
        RightMotor.setVelocity(rightSpeed)
         
    
    # Enter here exit cleanup code.
