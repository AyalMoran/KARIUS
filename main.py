import time
import requests
import json
import sys
import sounddevice as sd
import soundfile as sf
from PyQt5.QtCore import QThread, pyqtSignal
import NLU
import STT as stt
import KariusGUI as gui
import player
import logging

# Setting up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

class STTThread(QThread):
    def __init__(self, customer, window, parent=None):
        super().__init__(parent)
        self.customer = customer
        self.window = window

    def run(self):
        player.play(player.sound_start)
        while (True):
            freetext_flag = False
            text,freetext_flag = stt.start(freetext_flag)

            if freetext_flag:
                logging.info("Free text identified")
                if is_allergic(text, self.customer.allergies):
                    player.play(player.sound_alert)
                    print("שים לב! המטופל אלרגי ל-" + self.customer.allergies)
                else:
                    self.window.change_textbox_text(text)
                    player.play(player.sound_success)

            else:
                text = NLU.parse(text)
                if text != -1:
                    self.customer.add_tooth(text, self.window)
                else:
                    continue

class Customer:
    def __init__(self, name, age, patient_id, teeth=[], allergies=''):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.teeth = teeth
        self.allergies = allergies

    def add_tooth(self, new_teeth, window):
        if not new_teeth or not window:
            raise ValueError("Both new_teeth and window inputs are required.")

        self.teeth.append(new_teeth)
        try:
            symptoms = new_teeth[0][0][1]
            symptom = symptoms[0] if symptoms else None
            color = find_color(symptom) if symptom else None
        except:
            raise ValueError("Invalid format for new_teeth input.")

        tooth_num = new_teeth[0][0][0]
        other_text = new_teeth[0][0][2][0] if new_teeth[0][0][2] else ""

        window.click_checkbox(tooth_num, color)
        if other_text!='':
            window.enter_tooth_text(tooth_num, other_text)
        logging.info("Tooth %s added to the customer %s", tooth_num, self.name)


def is_allergic(medicine, allergies):
    return allergies in medicine


def find_color(i):
    colors = {'חור': 'green', 'עששת': 'yellow', 'דלקת': 'red', None: 'black'}
    return colors.get(i, i)


if __name__ == '__main__':
    customer = Customer("Yuri Yurchenko", '40', "12345678", [], 'פניצילין')

    app = gui.QApplication(sys.argv)
    window = gui.Karius()

    window.update_line_edits([customer.name, customer.age, customer.patient_id])
    window.show()

    stt_thread = STTThread(customer, window)
    stt_thread.start()
    app.exec_()
