import random as rnd
from datetime import datetime as dt
from calculator import get_time_result
from Exercise_Linear_equation import LinearEquationBase
from FruitPicking import FruitPicking

SHOW_ANSWERS = True
NUMBER_OF_EXERCISE = 1
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


def give_an_exercise_console(include_text_question=False, just_divide=False, console=True):
    rnd_text_or_equation = rnd.randrange(0, 3, 1)
    check = 0
    count = 0

    if include_text_question is True:
        if rnd_text_or_equation == 1:
            exercise = LinearEquationBase(just_divide=just_divide, show_answer=SHOW_ANSWERS)
            question_text = exercise.generate_exercise_scales_and_fruits_string()
        elif rnd_text_or_equation == 0:
            exercise = LinearEquationBase(just_divide=just_divide, show_answer=SHOW_ANSWERS)
            question_text = exercise.generate_exercise_linear_equation_single()
        else:
            exercise = FruitPicking(show_answer=SHOW_ANSWERS)
            question_text = exercise.generate_question_string()

    else:
        exercise = LinearEquationBase(just_divide=just_divide, show_answer=SHOW_ANSWERS)
        question_text = exercise.generate_exercise_linear_equation_single()

    while check == 0:
        print(question_text)
        exercise.get_answer_console()
        check = exercise.check_answer()
        count = count + 1
        if console is True:
            if check == 0:
                print("Ошибка, проверь еще раз.")
                print("\n")
            else:
                print("Правильно! Ура!")
                print("\n")

    return count


class ExerciseCheck:
    def __init__(self, number):
        self.questions_max_count = number
        self.questions_count = 0
        self.try_count = 0
        self.question_count = 0
        self.answers_row = []
        self.start_time = dt.now()
        self.end_time = dt.now()

    def doing_exercise_console(self, include_text_questions=False, only_divide=False):
        while self.questions_count < self.questions_max_count:
            print("Пример №" + str(self.questions_count + 1))
            trys = give_an_exercise_console(include_text_question=include_text_questions,
                                            just_divide=only_divide)
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


if __name__ == '__main__':
    ExerciseCheck(NUMBER_OF_EXERCISE).doing_exercise_console(include_text_questions=INCLUDE_TEXT_QUESTION,
                                                             only_divide=ONLY_DIVIDE)

