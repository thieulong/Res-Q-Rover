import serial
import time

# Set up the serial connection
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

# Define some commands
move_forward_cmd = b'\xff\x55\x04\x00\x02\x7F\x00\x00'
move_backward_cmd = b'\xff\x55\x04\x00\x01\x7F\x00\x00'
turn_left_cmd = b'\xff\x55\x04\x00\x03\x00\x7F\x00'
turn_right_cmd = b'\xff\x55\x04\x00\x03\x7F\x00\x00'
stop_cmd = b'\xff\x55\x04\x00\x00\x00\x00\x00'

# Send a command to the robot
def send_command(command):
    ser.write(command)
    time.sleep(0.1)

# Move forward
def move_forward():
    send_command(move_forward_cmd)

# Move backward
def move_backward():
    send_command(move_backward_cmd)

# Turn left
def turn_left():
    send_command(turn_left_cmd)

# Turn right
def turn_right():
    send_command(turn_right_cmd)

# Stop
def stop():
    send_command(stop_cmd)

# Read sensor data
def read_sensors():
    ser.write(b'\xff\x55\x06\x00\x03\x01\x00\x00')
    time.sleep(0.1)
    response = ser.read(10)
    # Parse the response and return the sensor data
    return response

# Example usage
move_forward()
time.sleep(1)
turn_left()
time.sleep(0.5)
move_backward()
time.sleep(1)
turn_right()
time.sleep(0.5)
stop()
sensor_data = read_sensors()
print(sensor_data)
