#ASR FILE

import os
import pocketsphinx
from pocketsphinx import  Decoder, get_model_path
from pocketsphinx import LiveSpeech
import player

model_path = get_model_path()+'\\en-us'
config = pocketsphinx.Config()
config.set_string('-hmm', os.path.join(model_path, 'en-us'))
config.set_string('-lm', os.path.join(model_path, 'en-us.lm.bin'))

# Add the keyphrases to the dictionary
keyphrase_dict = os.path.join(model_path, 'cmudict-en-us.dict')
config.set_string('-dict', keyphrase_dict)
data_path = os.getcwd()

# Create a LiveSpeech object with the keyphrases
def kariusDetector():
    print("...")
    speech = LiveSpeech(lm=False, kws="C:\\Users\\Ayal\\PycharmProjects\\spacy test\\key.list.txt", kws_threshold=1e-10)
    for phrase in speech:
        print("אני כאן! איך אפשר לעזור?")
        player.play(player.sound_karius)
        return True




