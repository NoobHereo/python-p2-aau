import time as time
from obis-laser-cotroller import ObisLaserController
# A library for a possible part

# Create the laser controller and connect to device
laserComp = ObisLaserController(PORT)
laserComp.connect()

# The class which handles all functions and variables related to the laser component and it's functions
class laser:
    watt = 0
    wavelength = 0
    focuspoint = 0

    # Emits a laser for a given time (0.5 seconds) and then turns it off again. This should be
    # called whenever the robot is on top of weed.
    def light(self, watt, wavelength, focuspoint):
        self.watt = watt
        self.wavelength = wavelength
        self.focuspoint = focuspoint

        laserComp.on(self.watt, self.wavelength, self.focuspoint)
        time.sleep(0.5)
        laserComp.off(0, 0, 0)

# The class which handles all functions and variables related to the brush component and it's functions
class brushing:
    torque = 0
    rpm = 0 # TODO: Define this later
    
    # Turns the brush component on with a given rpm(rotations per minute) and a force torque (newton meter)
    def brushOn(self, rpm, torque):  
        if self.rpm > 0 and self.torque > 0:
            self.rpm = rpm
            self.torque = torque
            brushComp.on(self.rpm, self.torque)
        
    # Turns the brush component off where it sets the brush variables to zero
    def brushOff(self):
        if self.rpm != 0:
            self.rpm = 0
        if self.torque != 0:
            self.torque = 0
        
        brushComp.off(self.rpm, self.torque)