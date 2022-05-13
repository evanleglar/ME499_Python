#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from slider import SliderDisplay
from digital_signal import DigitalSignal


class AudioDisplay(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Audio Filtering GUI')

        # A widget and Layout
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()

        # initial values for max time and frequency before file is loaded
        self.max_time = 300  # initialize at 300 seconds
        self.max_freq = 20000  # hz
        self.audio_data = 0
        self.samp_freq = 25000
        self.wav_file = ""
        self.start = 0
        self.end = 10
        self.bound_low = 0
        self.bound_high = self.max_freq
        self.signal = 0

        # Time Sliders
        self.start_slider = SliderDisplay("Start (s)", 0, self.max_time)
        self.end_slider = SliderDisplay("End (s)", 0, self.max_time)

        # Frequency Sliders
        self.bound_low_slider = SliderDisplay("Low Cutoff (Hz)", 0, self.max_freq)
        self.bound_high_slider = SliderDisplay("High Cutoff (Hz)", 0, self.max_freq)

        # Load Lines
        load_label = QLabel('Load File')
        self.load_box = QLineEdit(self)
        self.load_button = QPushButton('Load')
        self.load_button.clicked.connect(self.load)
        self.load_button.clicked.connect(self.graph)

        # Save Lines
        save_label = QLabel('Save File')
        self.save_box = QLineEdit(self)
        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save)

        # Graph Display
        self.fig = Figure()
        self.disp = FigureCanvas(self.fig)
        self.fig.clear()

        # Widget Layouts
        row1.addWidget(self.start_slider)
        row1.addWidget(self.end_slider)
        row2.addWidget(self.bound_low_slider)
        row2.addWidget(self.bound_high_slider)
        row3.addWidget(load_label)
        row3.addWidget(self.load_box)
        row3.addWidget(self.load_button)
        row4.addWidget(save_label)
        row4.addWidget(self.save_box)
        row4.addWidget(self.save_button)

        layout.addWidget(self.disp)
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addLayout(row4)

    def load(self):

        try:
            self.wav_file = self.load_box.text()
            print(self.wav_file)
            self.signal = DigitalSignal.from_wav(str(self.wav_file))

            self.start = self.signal.start
            self.end = self.signal.end
            self.max_time = self.end
            self.max_freq = self.signal.max_freq
            self.bound_low = self.signal.bound_low
            self.bound_high = self.signal.bound_high
            self.audio_data = self.signal.audio_data
            self.samp_freq = self.signal.samp_freq

            print(self.bound_low)
            print(self.bound_high)
            print(self.start)
            print(self.end)

            self.update()

            print(self.bound_low)
            print(self.bound_high)
            print(self.start)
            print(self.end)

        except FileNotFoundError:
            self.load_box.setText("File not found in this directory")

        except ValueError:
            self.load_box.setText("File must be .wav format")

    def save(self):
        filename = self.save_box.text()
        self.start = self.start_slider.value
        self.end = self.end_slider.value
        self.bound_low = self.bound_low_slider.value
        self.bound_high = self.bound_high_slider.value
        self.signal.set_time(self.start, self.end)
        self.signal.set_frequency_bounds(self.bound_low, self.bound_high)
        self.signal.save_wav(filename)
        print(self.start)
        print(self.end)
        print(self.bound_low)
        print(self.bound_high)

    def graph(self):
        self.draw(self.audio_data)

    def draw(self, signal):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot(signal)
        ax.set_title(f"{self.wav_file}")
        ax.set_xlabel("Samples")
        ax.set_ylabel("Amplitude")
        self.disp.draw()

    # def update(self):


if __name__ == '__main__':
    app = QApplication([])

    interface = AudioDisplay()

    interface.show()

    app.exec_()
