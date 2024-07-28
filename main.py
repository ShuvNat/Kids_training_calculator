import random as rnd
from datetime import datetime as dt
from calculator import get_time_result
from Exercise_Linear_equation import LinearEquationBase, ScalesAndFruits
from FruitPicking import FruitPicking

SHOW_ANSWERS = False
NUMBER_OF_EXERCISE = 20
ONLY_DIVIDE = False
INCLUDE_TEXT_QUESTION = True


def word_after_try_number(n):
    if n in (11, 12, 13, 14):
        result = 'попыток'
    elif n % 10 == 1:
        result = 'попытка'
    elif n % 10 in (2, 3, 4):
        result = 'попытки'
    else:
        result = 'попыток'
    return result


class OneTask:
    def __init__(self, include_text_question=False, just_divide=False, console=True, show_answers=SHOW_ANSWERS):
        self.show_answers = show_answers
        self.include_text_question = include_text_question
        self.just_divide = just_divide
        self.console = console
        self.check = 0
        self.try_count = 0
        self.task_type = rnd.randrange(0, 3, 1)
        self.task = self.create_task()
        self.question_text = self.task_question()

    def create_task(self):
        if self.include_text_question is True:
            if self.task_type == 0:
                self.task = ScalesAndFruits()

            elif self.task_type == 1:
                self.task = FruitPicking()

            else:
                self.task = LinearEquationBase(just_divide=self.just_divide)

        else:
            self.task = LinearEquationBase(just_divide=self.just_divide)
        return self.task

    def task_question(self):
        question_text = self.task.generate_question_string()

        if self.show_answers is True:
            question_text = question_text + " Ответ: " + str(self.task.right_answer)

        return question_text

    def give_an_exercise_console(self):
        check = 0
        while check == 0:
            print(self.question_text)
            self.task.get_answer_console()
            check = self.task.check_answer()
            self.try_count = self.try_count + 1
            if check == 0:
                print("Ошибка, проверь еще раз.")
                print("\n")
            else:
                print("Правильно! Ура!")
                print("\n")
        return self.try_count


class ExerciseCheck:
    def __init__(self, number=NUMBER_OF_EXERCISE, cfg_file=None):
        self.questions_max_count = number
        self.show_answers = SHOW_ANSWERS

        if cfg_file is not None:
            self.get_cfg_from_file(cfg_file)
        self.questions_count = 0
        self.try_count = 0
        self.question_count = 0
        self.answers_row = []
        self.start_time = dt.now()
        self.end_time = dt.now()

    def doing_exercise_console(self):
        while self.questions_count < self.questions_max_count:
            print("Пример №" + str(self.questions_count + 1))
            trys = OneTask(include_text_question=INCLUDE_TEXT_QUESTION, just_divide=ONLY_DIVIDE,
                           show_answers=self.show_answers).give_an_exercise_console()
            self.answers_row.append([self.questions_count + 1, trys])
            self.try_count = self.try_count + trys
            self.questions_count = self.questions_count + 1

        print("Решено: " + str(self.questions_max_count) + " примеров. Всего ушло: " + str(self.try_count) + " " +
              str(word_after_try_number(self.try_count)))
        print(self.answers_row)
        self.end_time = dt.now()
        print(f'Сегодня твое время {get_time_result(self.end_time - self.start_time)}')
        print()

        return 0

    def get_cfg_from_file(self, cfg_filename):

        try:
            file = open(cfg_filename, "r")

            for line in file:
                fields = line.strip().split()
                if fields[0] in "Number":
                    number = fields[1]
                    self.questions_max_count = int(number)
                if fields[0] in "Answers":
                    if fields[1] in "True":
                        self.show_answers = True
                    else:
                        self.show_answers = False
        except IOError:
            self.questions_max_count = NUMBER_OF_EXERCISE
            self.show_answers = SHOW_ANSWERS


if __name__ == '__main__':

    filename = "config1.cfg"
    ExerciseCheck(cfg_file=filename).doing_exercise_console()

