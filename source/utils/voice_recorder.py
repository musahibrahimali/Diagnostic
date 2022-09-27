import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.fftpack
import scipy.signal
import scipy.io.wavfile
from scipy.interpolate import griddata
import copy
import math
import sounddevice as sd
import soundfile as sf
from scipy.signal import medfilt
from glob import glob
from scipy import signal
import wave
import sys
from pydub import AudioSegment
from scipy.fftpack import hilbert
from scipy.integrate import simps
from scipy.interpolate import make_interp_spline, BSpline
from mutagen.mp3 import MP3


def open_audio(path: str, mp3: bool = True) -> any:
    audio = wave.open(path)

    # Get frame rate
    fs = audio.getframerate()
    print(f"Frame rate: {fs}")

    # The number of individual frames
    n_frames = audio.getnframes()
    print(f"Number of frames: {n_frames}")

    # Read all frames of audio
    sig = audio.readframes(n_frames)
    sig = np.frombuffer(sig, dtype=np.int16)

    # Audio length
    duration = n_frames / fs
    print(f"Audio duration(Sec): {duration}")

    time_range = np.linspace(0, duration, num=n_frames)

    return time_range, sig, fs, duration


def frequency_analysis(sig, fs) -> any:
    global time

    # Get values for fourier transform
    frq = np.arange(len(sig)) / (len(sig) / fs)
    freq_ranges = frq[range(len(sig) // 2)]
    power = np.fft.fft(sig) / len(sig)
    power = power[range(len(sig) // 2)]
    return freq_ranges, power


# %%
def get_envelopes(time_range, s, dmin=1, dmax=1, split=False, top_env=True, smoothening=1500) -> any:
    lmin = (np.diff(np.sign(np.diff(s))) > 0).nonzero()[0] + 1
    # locals max
    lmax = (np.diff(np.sign(np.diff(s))) < 0).nonzero()[0] + 1

    if split:
        s_mid = np.mean(s)
        lmin = lmin[s[lmin] < s_mid]
        lmax = lmax[s[lmax] > s_mid]

    # global max of dmax-chunks of locals max
    lmin = lmin[[i + np.argmin(s[lmin[i:i + dmin]]) for i in range(0, len(lmin), dmin)]]
    # global min of dmin-chunks of locals min
    lmax = lmax[[i + np.argmax(s[lmax[i:i + dmax]]) for i in range(0, len(lmax), dmax)]]

    if top_env:
        envelope_coords = lmin
    else:
        envelope_coords = lmax

    env_x, env_y = time_range[envelope_coords], s[envelope_coords]
    xnew = np.linspace(env_x.min(), env_x.max(), smoothening)
    spl = make_interp_spline(env_x, env_y, k=3)

    ynew = spl(xnew)

    # Filter positive part of the wave
    xnew = abs(xnew)
    ynew = abs(ynew)

    return xnew, ynew


def area_under_plot(f_data) -> any:
    return np.trapz(f_data, dx=1)


def flow_rate(f_data) -> any:
    return np.tranz(f_data, dx=1)


def Usg(f_data) -> any:
    return np.tranz(f_data, dx=1)


def Vol(f_data) -> any:
    return np.tranz(f_data, dx=1)


def butter_highpass(filtcut, fs, order=2) -> any:
    nyq = 0.5 * fs
    norm_cutoff = filtcut / nyq
    filtb, filta = signal.butter(order, norm_cutoff, btype='high')
    return filtb, filta


def butter_highpass_filter(sig, filtcut, fs, order=2) -> any:
    global fdata
    filtb, filta = butter_highpass(filtcut, fs, order)
    fdata = signal.filtfilt(filtb, filta, sig)
    return fdata


def record_audio() -> bool:
    fs = 44100
    duration = 25  # seconds
    my_recording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype=np.int16)
    print("Recording Audio")
    sd.wait()
    print("Audio recording complete ")
    sf.write("rec.wav", my_recording, fs)
    # Open Audio file
    time_range, sig, framerate, duration = open_audio("rec.wav", mp3=False)
    frequencies, power = frequency_analysis(sig, framerate)
    filtcut = 250
    butter_highpass_filter(sig, filtcut, framerate)

    # %%
    # Get envelope
    envelope_x, envelope_y = get_envelopes(time_range, fdata, dmin=200, dmax=200, top_env=True, smoothening=90)
    envelope_y_med_filter = medfilt(envelope_y, 3)
    envelope_x_med_filter = medfilt(envelope_x, 3)
    # Sound wave graph
    plt.figure(figsize=(12, 8))
    plt.plot(time_range, sig, label='signal')
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Sound Wave")
    plt.savefig("sound_wave.png")

    # Frequency Graph
    plt.figure(figsize=(12, 8))
    plt.plot(frequencies, abs(power), 'r-', lw=2)
    plt.title("Fourier Analysis")
    plt.xlabel("Frequency")
    plt.ylabel("Power")
    plt.savefig("frequency.png")

    # Envelope & Sound Wave
    plt.figure(figsize=(12, 8))
    plt.title("Sound & Enveloped graph")
    plt.plot(time_range, sig, 'b-', label='signal')
    plt.plot(envelope_x, envelope_y, 'g-', lw=3)
    plt.plot(envelope_x_med_filter, envelope_y_med_filter, '', lw=3)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.savefig("sound_envelope.png")

    # Envelope Only
    plt.figure(figsize=(12, 8))
    plt.title("Enveloped graph")
    plt.plot(envelope_x, envelope_y, 'g-', lw=3)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.savefig("envelope.png")
    # if the images were saved return true else false

    plt.figure(figsize=(12, 8))
    plt.plot(envelope_x_med_filter, envelope_y_med_filter, '', lw=3)
    plt.title("Medfilt graph")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.savefig("med_filter.png")

    # Calculate area under envelope
    area = area_under_plot(envelope_y_med_filter)

    voided_volume = 500 * area / 221996
    urine_flow_rate = voided_volume / duration
    _usg = 1 / voided_volume

    return duration, voided_volume, urine_flow_rate, _usg

