import random as rnd
from BaseTask import BaseTask
variable_list = ["x", "y", "z", "t", "m"]
fruit_name_list = [["яблоко", "яблока", "яблок"], ["груша", "груши", "груш"], ["апельсин", "апельсина", "апельсинов"],
                   ["слива", "сливы", "слив"], ["персик", "персика", "персиков"]]
NUMBER_OF_EXERCISE = 20
ONLY_DIVIDE = False
INCLUDE_TEXT_QUESTION = True
A_RANGE = 15
X_RANGE = 100
SHOW_ANSWERS = True


def get_variable(v_list):
    return v_list[rnd.randrange(0, len(v_list), 1)]


class LinearEquationBase(BaseTask):
    def __init__(self, show_answer=False, just_divide=False, a_range=10, x_range=100):
        super().__init__(show_answer)
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
        self.right_answer = self.x
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

        string = string + '\nЧему равно ' + str(self.variable) + "?"
        return string

    def generate_question_string(self, show_answer_marker=False):
        question_string = self.generate_question_string_base(self.variable)
        if show_answer_marker is True:
            question_string = question_string + " " + str(self.right_answer)
        return question_string


class ScalesAndFruits(LinearEquationBase):

    def __init__(self, show_answer=SHOW_ANSWERS):
        super().__init__(show_answer=show_answer)

    def generate_question_string(self, show_answer_marker=False):
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
        self.right_answer = self.x

        if tmp_number in [0, 2, 4]:
            odin_word = "одного " + str(fruit_name_list[tmp_number][1])
        elif tmp_number == 1:
            odin_word = "одной " + str(fruit_name_list[tmp_number][1])
        else:
            odin_word = "одной " + str(fruit_name_list[tmp_number][1])

        question_string = "На весах с одной стороны лежит " + str(self.a) + " " + str(self.variable) + \
                          " и гири общей массой " + str(self.b) + " грамм. А на другой чаше весов лежат гири массой " \
                          + str(self.c) + " грамм. \nКакова масса " + str(odin_word) + "? "
        if show_answer_marker is True:
            question_string = question_string + str(self.right_answer)

        return question_string

