#!/usr/bin/env python3


from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import *
from slider import SliderDisplay


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Problem 3: Lots of Sliders')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # A layout
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # System Parameter Sliders
        self.sys_params = QLabel('System Parameters')
        self.mass = SliderDisplay("Mass", 0, 10)
        self.spring = SliderDisplay("Spring", 0, 10)
        self.damper = SliderDisplay("Damper", 0, 10)

        # Simulation Parameter Sliders
        self.sim_params = QLabel('Simulation Parameters')
        self.Time = SliderDisplay("Time (s)", 0, 100)
        self.step = SliderDisplay("Time Step (s)", 0.001, 0.1)

        # Interface buttons
        simulate_button = QPushButton('Simulate System')
        simulate_button.clicked.connect(self.simulate)
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # Widget Layouts
        layout.addWidget(self.sys_params)
        layout.addWidget(self.mass)
        layout.addWidget(self.spring)
        layout.addWidget(self.damper)
        layout.addWidget(self.sim_params)
        layout.addWidget(self.Time)
        layout.addWidget(self.step)
        layout.addWidget(simulate_button)
        layout.addWidget(quit_button)

    def simulate(self):
        print("Mass: ", self.mass.value)
        print("Spring: ", self.spring.value)
        print("Damper: ", self.damper.value)
        print("Time: ", self.Time.value)
        print("Time Step: ", self.step.value)

    # def value(self):



if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()
