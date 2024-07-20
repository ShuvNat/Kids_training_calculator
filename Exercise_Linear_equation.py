import random as rnd

variable_list = ["x", "y", "z", "t", "m"]
fruit_name_list = [["яблоко", "яблока", "яблок"], ["груша", "груши", "груш"], ["апельсин", "апельсина", "апельсинов"],
                   ["слива", "сливы", "слив"], ["персик", "персика", "персиков"]]
NUMBER_OF_EXERCISE = 3
ONLY_DIVIDE = False
INCLUDE_TEXT_QUESTION = False
A_RANGE = 10
X_RANGE = 100

def get_variable(v_list):
    return v_list[rnd.randrange(0, len(v_list), 1)]


class LinearEquationBase:
    def __init__(self, show_answer=False, just_divide=False, a_range=10, x_range=100):
        self.a = int(rnd.randrange(1, a_range, 1))
        self.x = int(rnd.randrange(3, x_range, 1))
        self.multiply = self.a * self.x
        self.variable = get_variable(variable_list)
        if just_divide is True:
            self.b = 0
        else:
            tmp_cff = int(rnd.randrange(1, self.multiply, 1))
            self.b = int(rnd.randrange(-tmp_cff, tmp_cff, 1))

        self.c = self.multiply + self.b
        if self.b > 0:
            self.token = rnd.randrange(0, 2, 1)
        else:
            self.token = 1
        self.answer = 0
        self.show_answer_marker = show_answer

    def generate_question_string_base(self, variable):
        if self.b < 0:
            sign = " - "
        elif self.b > 0:
            sign = " + "
        else:
            sign = ""

        if self.token == 1:
            string = str(self.a) + "*" + str(variable) + sign + str(abs(self.b)) + " = " + str(self.c)
        else:
            string = str(self.b) + " + " + str(self.a) + "*" + str(variable) + " = " + str(self.c)

        if self.b == 0:
            string = str(self.a) + "*" + str(variable) + " = " + str(self.c)

        return string

    def generate_exercise_scales_and_fruits_string(self):
        tmp_number = rnd.randrange(0, len(fruit_name_list), 1)
        if self.a == 1:
            self.variable = fruit_name_list[tmp_number][0]
        elif self.a in range(2, 5):
            self.variable = fruit_name_list[tmp_number][1]
        else:
            self.variable = fruit_name_list[tmp_number][2]

        self.x = int(rnd.randrange(50, 120, 1))
        self.multiply = self.a * self.x
        self.b = int(rnd.randrange(0, 1000, 10))
        self.c = self.multiply + self.b

        if tmp_number in [0, 2, 4]:
            odin_word = "одного " + str(fruit_name_list[tmp_number][1])
        elif tmp_number == 1:
            odin_word = "одной " + str(fruit_name_list[tmp_number][1])
        else:
            odin_word = "одной " + str(fruit_name_list[tmp_number][1])

        question_string = "На весах с одной стороны лежит " + str(self.a) + " " + str(self.variable) + \
                           " и гири общей массой " + str(self.b) + " грамм. А на другой чаше весов лежат гири массой " \
                           + str(self.c) + " грамм. \nКакова масса " + str(odin_word) + "? "
        return question_string

    def generate_exercise_scales_and_fruits_console(self):
        self.answer = input(self.generate_exercise_scales_and_fruits_string())

    def generate_question_string(self):
        return self.generate_question_string_base(self.variable)

    def generate_exercise_linear_equation_single(self):
        if self.show_answer_marker is True:
            print(self.x)
        print(self.generate_question_string())
        question_string = "Чему равно " + str(self.variable) + ": "
        return question_string

    def generate_exercise_linear_equation_single_console(self):
        self.answer = input(self.generate_exercise_linear_equation_single())

    def check_answer(self):
        if str(self.answer) == str(self.x):
            return 1
        else:
            return 0


def single_exercise_linear_equation_console(include_text_question=False, just_divide=False, console=True):
    rnd_text_or_equation = rnd.randrange(0, 2, 1)
    check = 0
    count = 0
    exercise = LinearEquationBase(just_divide=just_divide, a_range=A_RANGE, x_range=X_RANGE)
    while check == 0:
        if include_text_question is True:
            if rnd_text_or_equation == 1:
                exercise.generate_exercise_scales_and_fruits_console()
            else:
                exercise.generate_exercise_linear_equation_single_console()
        else:
            exercise.generate_exercise_linear_equation_single_console()

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


class LinearEquationCheck:
    def __init__(self, number):
        self.questions_max_count = number
        self.questions_count = 0
        self.try_count = 0
        self.question_count = 0
        self.answers_row = []

    def doing_exercise_console(self, include_text_questions=False, only_divide=False):
        while self.questions_count < self.questions_max_count:
            print("Пример №" + str(self.questions_count + 1))
            trys = single_exercise_linear_equation_console(include_text_question=include_text_questions,
                                                           just_divide=only_divide)
            self.answers_row.append([self.questions_count + 1, trys])
            self.try_count = self.try_count + trys
            self.questions_count = self.questions_count + 1

        print("Решено: " + str(self.questions_max_count) + " примеров. Всего ушло: " + str(self.try_count) + " попыток")
        print(self.answers_row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    LinearEquationCheck(NUMBER_OF_EXERCISE).doing_exercise_console(include_text_questions=INCLUDE_TEXT_QUESTION,
                                                                   only_divide=ONLY_DIVIDE)
