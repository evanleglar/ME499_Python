#!/usr/bin/env python3

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSlider
from PyQt5.QtCore import *
import slider


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Problem 1: Slider GUI')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # A layout
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Problem 1 Label
        self.label_slider = QLabel()
        self.label_slider.setText('0')
        self.label_slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_slider.setAlignment(Qt.AlignCenter)

        # A button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # Problem 1 Slider
        self.slide_button = QSlider(Qt.Horizontal)
        self.slide_button.setTickPosition(QSlider.TicksBelow)
        self.slide_button.setMinimum(0)
        self.slide_button.setMaximum(10)
        self.slide_button.setTickInterval(0.1)
        self.slide_button.valueChanged.connect(self.value)

        # Widget Layouts
        layout.addWidget(self.label_slider)
        layout.addWidget(self.slide_button)
        layout.addWidget(quit_button)

        # Add other widgets to the layout here.  Possibly other layouts.
    def value(self):
        """Return the current value of the slider"""
        slider_value = self.slide_button.value()
        self.label_slider.setText(str(slider_value))


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

