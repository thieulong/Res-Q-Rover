import cv2
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from movement_control import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.engine_flag = 0

        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("Res-Q-Rover Control Terminal")
        self.setGeometry(250, 30, 600, 700)
        self.UiComponents()
        self.update()
        self.show()

    def UiComponents(self):
        # Title
        title = QLabel("Res-Q-Rover", self)
        title.setFont(QFont('Arial', 30))
        title.setGeometry(180, 0, 500, 100)

        # Webcam View
        self.webcam_view = QLabel(self)
        self.webcam_view.setGeometry(100, 100, 400, 300)
        self.webcam_view.setFrameShape(QFrame.Box)
        self.webcam_view.setLineWidth(1)

        # Buttons
        button_up = QPushButton(self)
        button_down = QPushButton(self)
        button_left = QPushButton(self)
        button_right = QPushButton(self)
        button_stop = QPushButton(self)
        button_exit = QPushButton("Exit", self)  # Exit button

        # Geometry
        button_up.setGeometry(250, 400, 100, 100)
        button_down.setGeometry(250, 600, 100, 100)
        button_left.setGeometry(150, 500, 100, 100)
        button_right.setGeometry(350, 500, 100, 100)
        button_stop.setGeometry(250, 500, 100, 100)
        button_exit.setGeometry(500, 620, 50, 50)  # Position and size of the exit button

        # Connect to function
        button_up.clicked.connect(self.move_forward)
        button_down.clicked.connect(self.move_backward)
        button_left.clicked.connect(self.turn_left)
        button_right.clicked.connect(self.turn_right)
        button_stop.clicked.connect(self.stop)
        button_exit.clicked.connect(QApplication.instance().quit)  # Connect exit button to quit slot

        # Button image
        button_up.setStyleSheet("background-image: url(interface-images/up-arrow.png); border-image: url(interface-images/up-arrow.png)")
        button_down.setStyleSheet("background-image: url(interface-images/down-arrow.png); border-image: url(interface-images/down-arrow.png)")
        button_left.setStyleSheet("background-image: url(interface-images/left-arrow.png); border-image: url(interface-images/left-arrow.png)")
        button_right.setStyleSheet("background-image: url(interface-images/right-arrow.png); border-image: url(interface-images/right-arrow.png)")
        button_stop.setStyleSheet("background-image: url(interface-images/stop_button.jpg); border-image: url(interface-images/stop_button.jpg)")

        # Start webcam
        self.start_webcam()

    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_webcam_view)
        self.timer.start(30)  # Update every 30 milliseconds

    def update_webcam_view(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            pixmap = pixmap.scaled(self.webcam_view.width(), self.webcam_view.height(), Qt.KeepAspectRatio)
            self.webcam_view.setPixmap(pixmap)

    def stop(self):
        print("Stopped moving")
        stop_moving()

    def move_forward(self):
        print("Moving forward")
        move_forward()

    def move_backward(self):
        print("Moving backward")
        move_backward()

    def turn_left(self):
        print("Turning left")
        turn_left()

    def turn_right(self):
        print("Turning right")
        turn_right()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
