import serial
import time

# Set up serial connection
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.reset_input_buffer()

# Define movement commands
forward_command = b'f\n'
backward_command = b'b\n'
left_command = b'l\n'
right_command = b'r\n'
stop_command = b's\n'

def stop_moving(duration=None):
    if duration == None:
        ser.write(stop_command)
    else:
        ser.write(stop_command)
        time.sleep(duration)

def move_forward(duration=None):
    if duration == None:
        ser.write(forward_command)
    else:
        ser.write(forward_command)
        time.sleep(duration)
        stop_moving()
    
def move_backward(duration=None):
    if duration == None:
        ser.write(backward_command)
    else:
        ser.write(backward_command)
        time.sleep(duration)
        stop_moving()

def turn_left(duration=None):
    if duration == None:
        ser.write(left_command)
    else:
        ser.write(left_command)
        time.sleep(duration)
        stop_moving()

def turn_right(duration=None):
    if duration == None:
        ser.write(right_command)
    else:
        ser.write(right_command)
        time.sleep(duration)
        stop_moving()

# Test movement commands
# while True:
#     print("Press:")
#     print("f - Move forward")
#     print("b - Move backward")
#     print("l - Turn left")
#     print("r - Turn right")
#     print("s - Stop moving")
#     command = input("Enter command: ")
#     if command == 'f':
#         move_forward()
#         time.sleep(1)
#         stop_moving()
#     elif command == 'b':
#         move_backward()
#         time.sleep(3)
#         stop_moving()
#     elif command == 'l':
#         turn_left()
#         time.sleep(1)
#         stop_moving()
#     elif command == 'r':
#         turn_right()
#         time.sleep(1)
#         stop_moving()
#     elif command == 's':
#         stop_moving()
    