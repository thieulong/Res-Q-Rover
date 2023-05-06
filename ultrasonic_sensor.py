import serial
import time

# Set up serial connection
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.reset_input_buffer()

#define ultrasonic sensor command
ultrasonic_sensor_command = b'd\n'
ser.write(ultrasonic_sensor_command)

def get_distance():
    ser.write(ultrasonic_sensor_command)

    ser.readline()
    if ser.in_waiting > 0:
        distance = ser.readline().decode('utf-8')
        print(distance)
        return distance
        

distance = get_distance()
print(distance)