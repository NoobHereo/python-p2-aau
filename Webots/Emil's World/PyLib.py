from controller import Robot
robot = Robot()

class Data:
    timestep = 64
    maxSpeed = 6.28
    numSide = 4
    lengthSide = 1
    wheelRadius = 0.1
    wheelDistance = 0.46

data = Data()

class Parts:
        # LED shows whparts is used, ie. the brush component or laser component
        redLed = robot.getDevice('led') 
        leftMotor = robot.getDevice('left_motor')
        rightMotor = robot.getDevice('right_motor')
        # brush = robot.getDevice('brush')
        # laser = robot.getDevice('laser')

parts = Parts()

class Forward:
    leftSpeed = data.maxSpeed
    rightSpeed = data.maxSpeed 

class Left:
    leftSpeed = -data.maxSpeed
    rightSpeed = data.maxSpeed
    parts.redLed.set(0)

class Brushing:
    parts.redLed.set(1)
    
class Eradicate:
    parts.redLed.set(1)
    

class Right:
    leftSpeed = data.maxSpeed
    rightSpeed = -data.maxSpeed
    parts.redLed.set(0)
