import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG_PIN = 23
ECHO_PIN = 24

def measure_distance():
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  
    distance = round(distance, 2)

    return distance

# try:
#     while True:
#         dist = measure_distance()
#         print("Distance: {} cm".format(dist))
#         time.sleep(1)

# except KeyboardInterrupt:
#     GPIO.cleanup()
