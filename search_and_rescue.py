#! /usr/bin/python
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import ultrasonic_sensor
import movement_control
import light_control
import sound_control
import telegram_message
import imutils
import pickle
import random
import time
import json
import cv2

with open('info.json') as file:
    info = json.load(file)

print("[!] Res-Q-Rover: Starting up ...")
search_people = info["person_name"]
searching = True
face_encodings = "encodings.pickle"

print("[!] Loading face encodings data ...")
face_data = pickle.loads(open(face_encodings, "rb").read())
print("[!] Face encodings data loaded successfully!")

print("[!] Booting up camera ...")
camera = VideoStream(src=0,framerate=10).start()
time.sleep(2)
print("[!] Camera is ready!")
print("[!] Res-Q-Rover is in action!")

while searching:
    frame = camera.read()
    frame = imutils.resize(frame, width=500)

    face_locations = face_recognition.face_locations(frame)
    print("[!] Face detected: {}".format(len(face_locations)))
    if len(face_locations) > 0:
        movement_control.stop_moving(duration=3)
        detected_encodings = face_recognition.face_encodings(frame, face_locations)

        for encoding in detected_encodings:
            matches = face_recognition.compare_faces(face_data["encodings"],encoding, tolerance=0.35)

            if True in matches:
                cv2.imwrite("found.jpg", frame)
                print("[!] {} is found!".format(search_people))

                movement_control.stop_moving()
                sound_control.beep()
                light_control.green_light(duration = 3)

                camera.stop()

                telegram_message.send_image()
                telegram_message.send_location()

                searching = False

            else:
                continue

    if len(face_locations) == 0:
        time.sleep(0.5)
        dist = ultrasonic_sensor.measure_distance()
        print("[!] Distance ahead: {}".format(dist))

        if dist < 50:
            light_control.red_light(duration=0.5)
            movement_control.move_backward(duration=2)
            direction = random.randint(1,2)
            turn_duration = random.uniform(1,3)

            if direction == 1:
                light_control.blue_light(duration=0.5)
                movement_control.turn_left(duration=turn_duration)

            elif direction == 2:
                light_control.blue_light(duration=0.5)
                movement_control.turn_right(duration=turn_duration)

        elif dist > 50:
            light_control.light_off()
            movement_control.move_forward()

print("[!] Res-Q-Rover search mission accomplished")