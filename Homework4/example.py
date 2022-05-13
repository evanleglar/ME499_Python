#!/usr/bin/env python3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as \
    FigureCanvas
from matplotlib.figure import Figure
from digital_signal import DigitalSignal as ds


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Audio Filter Visualizer')
        self.ticks = 1000

        # Start
        self.l_start = QLabel()
        self.l_start.setText('Start: {:.3f}s'.format(0))
        self.l_start.setAlignment(Qt.AlignCenter)
        self.s_start = QSlider(Qt.Horizontal)
        self.s_start.setMinimum(0)
        self.s_start.setMaximum(10*self.ticks)
        self.s_start.valueChanged.connect(self.vstart)

        # End
        self.l_end = QLabel()
        self.l_end.setText('End: {:.3f}s'.format(0))
        self.l_end.setAlignment(Qt.AlignCenter)
        self.s_end = QSlider(Qt.Horizontal)
        self.s_end.setMinimum(0)
        self.s_end.setMaximum(10*self.ticks)
        self.s_end.valueChanged.connect(self.vend)

        # Low
        self.l_low = QLabel()
        self.l_low.setText('Low: {:.3f}Hz'.format(0))
        self.l_low.setAlignment(Qt.AlignCenter)
        self.s_low = QSlider(Qt.Horizontal)
        self.s_low.setMinimum(0)
        self.s_low.setMaximum(100*self.ticks)
        self.s_low.valueChanged.connect(self.vlow)

        # High
        self.l_high = QLabel()
        self.l_high.setText('High: {:.3f}Hz'.format(0))
        self.l_high.setAlignment(Qt.AlignCenter)
        self.s_high = QSlider(Qt.Horizontal)
        self.s_high.setMinimum(0)
        self.s_high.setMaximum(12500*self.ticks)
        self.s_high.valueChanged.connect(self.vhigh)

        # Load
        self.l_load = QLabel('Load File:')
        self.l_load.setAlignment(Qt.AlignCenter)
        self.b_load = QPushButton('Load')
        self.b_load.clicked.connect(self.load)
        self.t_load = QLineEdit('starwars.wav')
        self.title = self.t_load.text()


        # Save
        self.l_save = QLabel('Save File')
        self.l_save.setAlignment(Qt.AlignCenter)
        self.b_save = QPushButton('Save')
        self.b_save.clicked.connect(self.save)
        self.t_save = QLineEdit()

        # Graph Display
        self.fig = Figure()
        self.disp = FigureCanvas(self.fig)
        self.fig.clear()

        # Interface Layout
        widget = QWidget()
        self.setCentralWidget(widget)
        tll = QVBoxLayout()
        widget.setLayout(tll)
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()

        # System Parameters
        row1.addWidget(self.l_start)
        row1.addWidget(self.s_start)
        row1.addWidget(self.s_end)
        row1.addWidget(self.l_end)
        row2.addWidget(self.l_low)
        row2.addWidget(self.s_low)
        row2.addWidget(self.s_high)
        row2.addWidget(self.l_high)
        row3.addWidget(self.l_load)
        row3.addWidget(self.t_load)
        row3.addWidget(self.b_load)
        row4.addWidget(self.l_save)
        row4.addWidget(self.t_save)
        row4.addWidget(self.b_save)
        tll.addWidget(self.disp)
        tll.addLayout(row1)
        tll.addLayout(row2)
        tll.addLayout(row3)
        tll.addLayout(row4)

    def load(self):
        """Load File"""
        try:
            ffs = ds.from_wav(self.title)
            self.s_start.setMaximum(ffs.end * self.ticks)
            self.s_start.setSliderPosition(ffs.start * self.ticks)
            self.s_end.setMaximum(ffs.end * self.ticks)
            self.s_end.setSliderPosition(ffs.end * self.ticks)
            self.s_low.setMaximum(ffs.bound_high * self.ticks)
            self.s_low.setSliderPosition(ffs.bound_low * self.ticks)
            self.s_high.setMaximum(ffs.bound_high * self.ticks)
            self.s_high.setSliderPosition(ffs.bound_high * self.ticks)
            self.update()
            self.graph()
        except FileNotFoundError:
            self.t_load.setText('File not found in directory')
        except TypeError:
            self.load_text.setText('File is not .wav format')

    def save(self):
        """Save File"""
        title = self.t_save.text()
        ffs = ds.from_wav(self.title)
        ffs.start, ffs.end, ffs.bound_low, ffs.bound_high = self.update()
        ffs.bandpass()
        ffs.save_wav(title)

    def update(self):
        """Update Graph With Slider Changes"""
        ffs = ds.from_wav(self.title)
        ffs.start = self.s_start.value() / self.ticks
        ffs.end = self.s_end.value() / self.ticks
        ffs.bound_low = self.s_low.value() / self.ticks
        ffs.bound_high = self.s_high.value() / self.ticks
        return ffs.start, ffs.end, ffs.bound_low, ffs.bound_high

    def graph(self):
        self.plot()

    def plot(self):
        """Import Bandpass Function and Plot"""
        self.fig.clear()
        file_name = self.title
        ffs = ds.from_wav(file_name)
        ffs.start, ffs.end, ffs.bound_low, ffs.bound_high = self.update()
        trm = ffs.bandpass()
        axes = self.fig.add_subplot(111)
        axes.plot(trm)
        axes.set_title('Adjusted Signal Profile of {}'.format(file_name))
        axes.set_xlabel('Discrete Points')
        axes.set_ylabel('Amplitude')
        self.disp.draw()

    def vstart(self):
        """Return the current value of the slider"""
        val = self.s_start.value()/self.ticks
        self.l_start.setText('Start: {:.3f}s'.format(val))
        if float(val) > (self.s_end.value() / self.ticks):
            self.s_end.setSliderPosition(float(val) * self.ticks)
        self.update()
        self.graph()

    def vend(self):
        """Return the current value of the slider"""
        val = self.s_end.value()/self.ticks
        self.l_end.setText('End: {:.3f}s'.format(val))
        if float(val) < (self.s_start.value() / self.ticks):
            self.s_start.setSliderPosition(float(val) * self.ticks)
        self.update()
        self.graph()

    def vlow(self):
        """Return the current value of the slider"""
        val = self.s_low.value()/self.ticks
        self.l_low.setText('Low: {:.3f}Hz'.format(val))
        if float(val) > (self.s_high.value()/self.ticks):
            self.s_high.setSliderPosition(float(val) * self.ticks)
        self.update()
        self.graph()

    def vhigh(self):
        """Return the current value of the slider"""
        val = self.s_high.value()/self.ticks
        self.l_high.setText('High: {:.3f}Hz'.format(val))
        if float(val) < (self.s_low.value()/self.ticks):
            self.s_low.setSliderPosition(float(val) * self.ticks)
        self.update()
        self.graph()



if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()