"""mavic2pro controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import InertialUnit
from controller import Gyro
from controller import Motor
import math

def clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

# create the Robot instance.
delivery_drone = Robot()

# get the time step of the current world.
timestep = int(delivery_drone.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
imu = delivery_drone.getInertialUnit('inertial unit')
gyro = delivery_drone.getGyro('gyro')

imu.enable(timestep)
gyro.enable(timestep)

front_left_motor = delivery_drone.getMotor("front left propeller")
front_right_motor = delivery_drone.getMotor("front right propeller")
rear_left_motor = delivery_drone.getMotor("rear left propeller")
rear_right_motor = delivery_drone.getMotor("rear right propeller")
motors = [front_left_motor, front_right_motor, rear_left_motor, rear_right_motor]
for motor in motors:
    motor.setPosition(float('inf'))
    motor.setVelocity(1.0)
      
k_vertical_thrust = 68.5;  # with this thrust, the drone lifts.
k_vertical_offset = 0.6;   # Vertical offset where the robot actually targets to stabilize itself.
k_vertical_p = 3.0;        # P constant of the vertical PID.
k_roll_p = 50.0;           # P constant of the roll PID.
k_pitch_p = 30.0;          # P constant of the pitch PID.

target_altitude = 1.0

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while delivery_drone.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    
    time = delivery_drone.getTime()
    
    imu_roll_pitch_yaw = imu.getRollPitchYaw()
    
    roll = imu_roll_pitch_yaw[0] + math.pi / 2.0
    pitch = imu_roll_pitch_yaw[1]
    
    gyro_x_y_z = gyro.getValues()

    roll_acceleration = gyro_x_y_z[0]
    pitch_acceleration = gyro_x_y_z[1]
    
    roll_disturbance = 0.0;
    pitch_disturbance = 0.0;
    yaw_disturbance = 0.0;
    
    altitude = 0.9

    # Process sensor data here.
    
    roll_input = k_roll_p * clamp(roll, -1.0, 1.0) + roll_acceleration + roll_disturbance
    pitch_input = k_pitch_p * clamp(pitch, -1.0, 1.0) - pitch_acceleration + pitch_disturbance
    yaw_input = yaw_disturbance
    clamped_difference_altitude = clamp(target_altitude - altitude + k_vertical_offset, -1.0, 1.0)
    vertical_input = k_vertical_p * pow(clamped_difference_altitude, 3.0)

    # Actuate the motors taking into consideration all the computed inputs.
    
    front_left_motor_input = k_vertical_thrust + vertical_input - roll_input - pitch_input + yaw_input;
    front_right_motor_input = k_vertical_thrust + vertical_input + roll_input - pitch_input - yaw_input;
    rear_left_motor_input = k_vertical_thrust + vertical_input - roll_input + pitch_input - yaw_input;
    rear_right_motor_input = k_vertical_thrust + vertical_input + roll_input + pitch_input + yaw_input;
    
    front_left_motor.setVelocity(front_left_motor_input)
    front_right_motor.setVelocity(-front_right_motor_input)
    rear_left_motor.setVelocity(-rear_left_motor_input)
    rear_right_motor.setVelocity(rear_right_motor_input)
    
    pass

# Enter here exit cleanup code.






