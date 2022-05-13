#!/bin/usr/env python3

import numpy as np
from scipy.fftpack import fft, fftfreq, ifft
from scipy.io import wavfile as wav
from matplotlib import pyplot as plt


class DigitalSignal:

    def __init__(self, audio_data, samp_freq):
        self.audio_data = audio_data
        self.samp_freq = samp_freq

        self.max_freq = self.samp_freq / 2
        self.start = 0
        self.end = (len(self.audio_data)-1)/self.samp_freq  # end time including the current start val

        self.bound_low = 0
        self.bound_high = self.max_freq  # "nyquist frequency"

    @staticmethod  # decorator
    def from_wav(filename):
        samp_freq, audio_data = wav.read(str(filename))
        signal = DigitalSignal(audio_data, samp_freq)
        return signal

    def set_time(self, start=None, end=None):
        if start is None:
            self.start = 0
        else:
            self.start = start
        if end is None:
            self.end = (len(self.audio_data)-1)/self.samp_freq
        else:
            self.end = end
        return self.start, self.end

    def set_frequency_bounds(self, low=None, high=None):
        if low is None:
            self.bound_low = 0
        else:
            self.bound_low = low
        if high is None:
            self.bound_high = self.max_freq
        else:
            self.bound_high = high
        return self.bound_low, self.bound_high

    def bandpass(self):
        data_for_filter = self.audio_data

        freqs_series = fftfreq(data_for_filter.size, 1/self.samp_freq)
        fftaudio = fft(data_for_filter)

        cut_audio = fftaudio.copy()
        cut_audio[(abs(freqs_series) < self.bound_low)] = 0
        cut_audio[(abs(freqs_series) > self.bound_high)] = 0

        filtered_signal = ifft(cut_audio)

        time_dex = np.arange(0, len(self.audio_data)/self.samp_freq, 1 / self.samp_freq)
        output = filtered_signal[(self.start < time_dex) & (time_dex < self.end)]
        return output.astype(np.int16)

    def save_wav(self, filename):
        wav.write(filename, self.samp_freq, self.bandpass())


if __name__ == '__main__':
    wav_file = 'starwars.wav'
    my_signal = DigitalSignal.from_wav(wav_file)  # returns samp_freq, audio_data

    plt.figure(1)
    plt.plot(my_signal.audio_data)
    my_signal.set_time(end=15)
    my_signal.set_frequency_bounds(low=3000, high=10000)
    my_signal.save_wav("filtered_Starwars1.wav")
    plt.plot(my_signal.bandpass())

    plt.show()

