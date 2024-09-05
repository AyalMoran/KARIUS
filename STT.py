import io
import os
from google.cloud import speech_v1p1beta1 as speech
import recorder as rec
from ASR import *

credential_path = "karius-374011-bbea05d61088.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


class STT_ft():
    def __init__(self):
        phrases = ["חור", "עששת", "שן", 'דלקת', 'טקסט חופשי', 'טקסט', 'חופשי', 'הערה', 'הערות', 'המטופל', 'פניצילין',
                   'דימום', "1", "2", "3",
                   "4", "5", "6", "7", "8", "9", "10",
                   "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                   "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]

        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="he-IL",
            enable_spoken_punctuation=True,
            speech_contexts=[{"phrases": phrases,
                              "boost": 10.0}],
            model='default'
        )
        self.client = speech.SpeechClient()

    def opensoundfile(self, file_name):
        with io.open(file_name, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)
        return audio

    def recognize(self, audio):
        try:
            response = self.client.recognize(config=self.config, audio=audio)
            return response
        except Exception as e:
            print('Something went wrong with recognition:', e)
            return None


class STT():
    def __init__(self):
        phrases = ["חור", "עששת", "שן", 'דלקת', 'טקסט חופשי', 'טקסט', 'חופשי', 'הערה', 'הערות', 'המטופל', 'פניצילין'
                                                                                                          "1", "2", "3",
                   "4", "5", "6", "7", "8", "9", "10",
                   "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                   "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]

        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="he-IL",
            enable_automatic_punctuation=True,
            speech_contexts=[{"phrases": phrases,
                              "boost": 10.0}],
            model='command_and_search'
        )
        self.client = speech.SpeechClient()

    def opensoundfile(self, file_name):
        with io.open(file_name, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)
        return audio

    def recognize(self, audio):
        try:
            response = self.client.recognize(config=self.config, audio=audio)
            return response
        except Exception as e:
            print('Something went wrong with recognition:', e)
            return None


def start(freetext):
    while True:
        if kariusDetector():
            rec.record()
            # The name of the audio file to transcribe
            file_name = "recorded.wav"
            confidence_thres = 0.7
            st = STT()
            audio = st.opensoundfile(file_name)
            response = st.recognize(audio)

            if response is None:
                print('Error with recognition')
            else:
                for result in response.results:
                    if result.alternatives[0].confidence < confidence_thres:
                        print("Transcript: {}".format(result.alternatives[0].transcript))
                        print('אבל רק נראה לי..')

                    else:
                        print("Transcript: {}".format(result.alternatives[0].transcript))
                        print('אני בטוח ב: {}'.format(result.alternatives[0].confidence))

                    string_set = set(result.alternatives[0].transcript.split())
                    list_set = set(['טקסט', 'חופשי', 'הערה', 'הערות'])
                    if list_set.intersection(string_set):
                        player.play(player.sound_note)
                        print("מה לרשום בהערות?")

                        rec.record()
                        stf = STT_ft()
                        audio1 = st.opensoundfile(file_name)
                        response1 = stf.recognize(audio1)
                        for result1 in response1.results:
                            if result1.alternatives[0].confidence < confidence_thres:
                                print("אמרת: {}".format(result1.alternatives[0].transcript))
                                print('אבל רק נראה לי..')
                            else:
                                print("אמרת: {}".format(result1.alternatives[0].transcript))
                                print('אני בטוח ב: {}'.format(result1.alternatives[0].confidence))

                        freetext = True
                        return result1.alternatives[0].transcript, freetext

                    return result.alternatives[0].transcript, freetext
