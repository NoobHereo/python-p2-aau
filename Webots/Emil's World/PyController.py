"""PyController controller."""
# Import modules
from controller import Robot
import PyLib

parts = PyLib.Parts()
data = PyLib.Data()

if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
  
    parts.leftMotor.setPosition(float('inf')); parts.leftMotor.setVelocity(0.0)
    
    parts.rightMotor.setPosition(float('inf')); parts.rightMotor.setVelocity(0.0)
    
    linearVelocity = data.wheelRadius * data.maxSpeed
    
    durationSide = data.lengthSide/linearVelocity
    
    startTime = robot.getTime()
    
    angleOfRotation = 6.28/data.numSide
    rateOfRotation = (2 * linearVelocity)/data.wheelDistance
    durationTurn = angleOfRotation/rateOfRotation
    
    # Rotation start and end time calculations
    rotStartTime = startTime + durationSide; rotEndTime = rotStartTime + durationTurn
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(data.timestep) != -1:
        currentTime = robot.getTime()
        PyLib.Right()

        if rotStartTime < currentTime < rotEndTime:
            PyLib.Left()        
        elif currentTime > rotEndTime:
            rotStartTime = currentTime + durationSide
            rotEndTime = rotStartTime + durationTurn
            parts.redLed.set(0)

        PyLib.Forward()