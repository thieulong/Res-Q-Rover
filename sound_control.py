import serial
import time

# Set up serial connection
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.reset_input_buffer()

# Define sound commands
sound_command = b'h\n'

def beep():
    time.sleep(1)
    ser.write(sound_command)




