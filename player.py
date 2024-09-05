import sounddevice as sd
import soundfile as sf

sound_start = 'start.wav'
sound_success = 'success.mp3'
sound_fail = 'fail1.wav'
sound_karius = 'karius.mp3'
sound_alert = 'alert.wav'
sound_note = 'note.wav'
AMP = 1.5


def play(sound):
    data, fs = sf.read(sound, dtype='float32')
    sd.play(data * AMP, fs)
