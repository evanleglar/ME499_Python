#!/bin/usr/env python3

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
from PyQt5.QtCore import *


class SliderDisplay(QWidget):
    def __init__(self, name, low, high, ticks=1000):
        QWidget.__init__(self)
        layout = QHBoxLayout()

        self.setLayout(layout)
        self.ticks = ticks

        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(low * self.ticks)
        self.slider.setMaximum(high * self.ticks)
        self.slider.valueChanged.connect(self.value)

        # Slider Label
        self.label_slider = QLabel()
        self.label_slider.setText(f'{name}:')

        # Slider Value
        self.slider_value = QLabel()
        self.slider_value.setText('0.000')

        # Widget Layouts
        layout.addWidget(self.label_slider)
        layout.addWidget(self.slider_value)
        layout.addWidget(self.slider)

    def value(self):
        """Return the current value of the slider"""
        self.value = self.slider.value() / self.ticks
        self.slider_value.setText('{0: .3f}'.format(self.value))
        return self.value


if __name__ == '__main__':
    app = QApplication([])

    slider = SliderDisplay('foo', 0, 1)

    slider.show()

    app.exec_()



