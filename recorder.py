import pyaudio
import wave
import numpy as np


def record():
    # Set the audio parameters
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    THRESHOLD = 1000
    SILENCE_TIME = 1 # time in seconds

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a new stream to record audio
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Start recording
    print("אני מקשיב...")
    frames = []
    silence_counter = 0
    recording = False
    while True:
        data = stream.read(CHUNK)
        audio_data = np.fromstring(data, np.int16)
        peak = np.average(np.abs(audio_data))*2
        if peak > THRESHOLD:
            recording = True
            silence_counter = 0
            frames.append(data)
        elif recording:
            silence_counter += 1
            if silence_counter > (SILENCE_TIME * RATE / CHUNK):
                break

    # Stop recording
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a WAV file
    wf = wave.open("recorded.wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()



