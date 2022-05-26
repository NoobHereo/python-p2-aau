from controller import Robot
robot = Robot()

class Data:
    timestep = 64
    maxSpeed = 6.28
    numSide = 4
    lengthSide = 1
    wheelRadius = 0.1
    wheelDistance = 0.46

    linearVelocity = wheelRadius * maxSpeed
    angleOfRotation = 6.28/numSide
    rateOfRotation = (2 * linearVelocity)/wheelDistance
    durationTurn = angleOfRotation/rateOfRotation
    
    durationSide = lengthSide/linearVelocity
    rotStartTime = robot.getTime() + durationSide; rotEndTime = rotStartTime + durationTurn

    def setSpeed(speed):
        maxSpeed = speed

data = Data()

class Parts:
        # LED shows whparts is used, ie. the brush component or laser component
        redLed = robot.getDevice('led')
        leftMotor = robot.getDevice('left_motor')
        rightMotor = robot.getDevice('right_motor')
        # brush = robot.getDevice('brush')
        # laser = robot.getDevice('laser') 

parts = Parts()

# Using the brush component
class Brushing:
    def setState(state): # state should be an int. 0 = off, 1 = on.
        parts.redLed.set(state)
    
# Using the laser component
class Eradicate:
    def setState(state): # state should be an int. 0 = off, 1 = on.
        parts.redLed.set(state)

# Drive forward
class Forward:
    leftSpeed = data.maxSpeed
    rightSpeed = data.maxSpeed 

# Drive Left
class Left:
    leftSpeed = -data.maxSpeed
    rightSpeed = data.maxSpeed
    parts.redLed.set(0)   

# Drive Right
class Right:
    leftSpeed = data.maxSpeed
    rightSpeed = -data.maxSpeed
    parts.redLed.set(0)

class Drive:
    def __init__(drive, leftSpeed, rightSpeed, rotEndTime, rotStartTime):
        drive.currentTime = robot.getTime()
        Right()
        
        if rotStartTime < robot.getTime() < rotEndTime:
            Left()
        elif drive.currentTime > rotEndTime:
            rotStartTime = robot.getTime() + data.durationSide; rotEndTime = rotStartTime + data.durationTurn
            parts.redLed.set(0)
        
        Forward()
        Brushing()