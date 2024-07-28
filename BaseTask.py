import random as rnd

SHOW_ANSWERS = True


class BaseTask:
    def __init__(self, show_answer=SHOW_ANSWERS):
        self.answer = 0
        self.right_answer = "Укажите тут то, что должно быть правильным ответом"
        self.show_answer_marker = show_answer

    def generate_question_string(self):
        base_string = "Сформируйте свой вопрос здесь"

        if self.show_answer_marker is True:
            base_string = base_string + " " + str(self.right_answer)

        return base_string

    def get_answer_console(self):
        self.answer = input("Запишите ответ: ")

    def check_answer(self):
        if str(self.answer) == str(self.right_answer):
            return 1
        else:
            return 0