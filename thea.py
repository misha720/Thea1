'''
	Thea 1
	Powered by Zero
'''

#	IMPORTS
import asyncio
import json
import os
import datetime

#	CONNECT THEA MODULS
from emotions import Emotions


class Logger:
    '''
        Logger
    '''

    def __init__(self, saving=False):
        self.saving = saving

    def new_session(self):
        self.session_active = {
            "data": str(datetime.datetime.now()),
            "chat": []
        }

    def add_phrase(self, speaker, content):
        phrase = {
            "speaker": speaker,
            "content": content
        }
        self.session_active['chat'].append(phrase)  # Add Phrase

    def save_session(self):
        with open('sessions/' + str(datetime.datetime.now()) + ".json", 'w') as fsession:  # Config
            json.dump(self.session_active, fsession)


#	ENGINE
class Engine:
    """
        Сердце Теи
        Реализует включение всех необходимых модулей и контроль функций и классов
    """

    def __init__(self):
        with open('config.json', 'r') as fconfig:  # Config
            self.config = json.load(fconfig)

        # SETTINGS
        self.logger = Logger(saving=True)  # Logger
        self.emotion = Emotions(self.config['emotions'])

        self.experience = 0  # Count Experience

    def loop(self):
        """
            One Session
        """
        self.logger.new_session()

        while True:
            # LOOP
            user_phrase = input("You: ").lower()
            self.logger.add_phrase("User", user_phrase)

            #print(self.emotion.weight_list)

            # Command
            if user_phrase == "/stop":  # Stop
                self.logger.save_session()
                return

            # Обработка фразы
            self.emotion.update_emotions(user_phrase)
            #print(self.emotion.weight_list)

#	RUN
if __name__ == '__main__':
    engine = Engine()
    engine.loop()
