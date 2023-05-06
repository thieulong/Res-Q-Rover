import serial
import time

# Set up serial connection
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.reset_input_buffer()

# Define light commands
light_off_command = b'0\n'
light_green_command = b'1\n'
light_red_command = b'2\n'
light_blue_command = b'3\n'
rainbow_on_command = b'4\n'
rainbow_off_command = b'5\n'

def light_off():
    ser.write(light_off_command)

def green_light(duration=None):
    if duration == None:
        ser.write(light_green_command)
    else:
        ser.write(light_green_command)
        time.sleep(duration)
        light_off()

def red_light(duration=None):
    if duration == None:
        ser.write(light_red_command)
    else:
        ser.write(light_red_command)
        time.sleep(duration)
        light_off()

def blue_light(duration=None):
    if duration == None:
        ser.write(light_blue_command)
    else:
        ser.write(light_blue_command)
        time.sleep(duration)
        light_off()

def rainbow_on(duration=None):
    if duration == None:
        ser.write(rainbow_on_command)
    else:
        ser.write(rainbow_on_command)
        time.sleep(duration)
        light_off()

def rainbow_off(duration=None):
    if duration == None:
        ser.write(rainbow_off_command)
    else:
        ser.write(rainbow_off_command)
        time.sleep(duration)
        light_off()

# Test light commands
# while True:
#     print("Press:")
#     print("0 - All lights off")
#     print("1 - Green lights")
#     print("2 - Red lights")
#     print("3 - Blue lights")
#     print("4 - Rainbow effect")
#     command = input("Enter command: ")
#     if command == '0':
#         light_off()
#     elif command == '1':
#         green_light()
#         time.sleep(3)
#         light_off()
#     elif command == '2':
#         red_light()
#         time.sleep(3)
#         light_off()
#     elif command == '3':
#         blue_light()
#         time.sleep(3)
#         light_off()
#     elif command == '4':
#         rainbow_on()
#         time.sleep(2)
#         rainbow_off()