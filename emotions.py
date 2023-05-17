import json

import skills.word_master as wm


class Emotions:
    """
        Эмоции Теи
        Отвечает за распознование эмоций слов собеседника и запуска своих эмоций
    """

    def __init__(self, old_config):
        self.weight_list = old_config  # DICT Хранит в себе веса

        # Подключение словарей
        with open('docs/angry_word.json', 'r') as fangryword:  # Загрузка списка Гнева
            self.angry_word_list = json.load(fangryword)

        with open('docs/sadness_word.json', 'r') as fsadnessword:  # Загрузка списка Печали
            self.sadness_word_list = json.load(fsadnessword)

        with open('docs/happy_word.json', 'r') as fhappyword:  # Загрузка списка Радости
            self.happy_word_list = json.load(fhappyword)

        with open('docs/fear_word.json', 'r') as ffearword:  # Загрузка списка Страха
            self.fear_word_list = json.load(ffearword)

    def update_emotions(self, phrase):

        drop_phrase = phrase.split()

        for user_word in drop_phrase:

            # Гнев
            for angry_word in self.angry_word_list:
                similarity = wm.word_to_word(user_word, angry_word['word'])

                print(user_word + " " + angry_word['word'] + " - " + str(similarity))

                if float(similarity) > 0.5:
                    print(user_word + " - is Angry")
                    self.weight_list['angry'] += angry_word['width']

            # Печаль
            for sadness_word in self.sadness_word_list:
                similarity = wm.word_to_word(user_word, sadness_word['word'])

                print(user_word + " " + sadness_word['word'] + " - " + str(similarity))

                if float(similarity) > 0.5:
                    print(user_word + " - is Sadness")
                    self.weight_list['sadness'] += sadness_word['width']

            # Радость
            for happy_word in self.happy_word_list:
                similarity = wm.word_to_word(user_word, happy_word['word'])

                print(user_word + " " + happy_word['word'] + " - " + str(similarity))

                if float(similarity) > 0.5:
                    print(user_word + " - is Happy")
                    self.weight_list['happy'] += happy_word['width']

            # Страх
            for fear_word in self.fear_word_list:
                similarity = wm.word_to_word(user_word, fear_word['word'])

                print(user_word + " " + fear_word['word'] + " - " + str(similarity))

                if float(similarity) > 0.5:
                    print(user_word + " - is Fear")
                    self.weight_list['fear'] += fear_word['width']


