# mavic2pro controller
# rewritten in Python from the original C sample source from webots (which is licensed under Apache 2.0)

# Import classes
from controller import Robot
from controller import InertialUnit
from controller import Gyro
from controller import Motor
import math
import time

#Function definitions
def clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

# create the Robot instance.
delivery_drone = Robot()

# get the time step of the current world.
timestep = int(delivery_drone.getBasicTimeStep())

# Initialise devices
imu = delivery_drone.getInertialUnit('inertial unit')
imu.enable(timestep)

gyro = delivery_drone.getGyro('gyro')
gyro.enable(timestep)

front_left_motor = delivery_drone.getMotor("front left propeller")
front_right_motor = delivery_drone.getMotor("front right propeller")
rear_left_motor = delivery_drone.getMotor("rear left propeller")
rear_right_motor = delivery_drone.getMotor("rear right propeller")
motors = [front_left_motor, front_right_motor, rear_left_motor, rear_right_motor]

for motor in motors:
    motor.setPosition(float('inf'))
    motor.setVelocity(1.0)
    
wait = int(delivery_drone.getTime())
while delivery_drone.step(timestep) != -1:
    if wait + 1 < int(delivery_drone.getTime()):
        break

# Main loop:
while delivery_drone.step(timestep) != -1:
    
    pass