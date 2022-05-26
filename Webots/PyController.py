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
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(data.timestep) != -1:
        PyLib.Drive()