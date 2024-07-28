import random as rnd
from BaseTask import BaseTask

fruit_name_list = [["яблоко", "яблока", "яблок"], ["груша", "груши", "груш"], ["апельсин", "апельсина", "апельсинов"],
                   ["слива", "сливы", "слив"], ["персик", "персика", "персиков"]]

A_RANGE = 15
X_RANGE = 100
SUMM_RANGE = 1000
SHOW_ANSWERS = True


class FruitPicking(BaseTask):
    def __init__(self, show_answer=SHOW_ANSWERS):
        super().__init__(show_answer)
        self.x = rnd.randint(0, X_RANGE)
        self.a = rnd.randint(2, A_RANGE)
        self.name_index_x = rnd.randint(0, len(fruit_name_list) - 1)
        self.name = fruit_name_list[self.name_index_x]
        self.less_or_more_index = rnd.randint(0, 2)
        self.summ = self.x + self.a * self.x
        self.answer = 0
        self.right_answer = self.summ
        self.show_answer_marker = show_answer

    def generate_question_string(self, show_answer_marker=False):

        if self.less_or_more_index == 0:
            less_more = "меньше"
            less_more1 = "больше"
        else:
            less_more = "больше"
            less_more1 = "меньше"

        base_string = "Во второй день собрали в " + str(self.a) + " раз " + less_more + " " + self.name[2] + \
                      " чем в первый. При этом оказалось, что в первый день собрали на " + \
                      str(self.summ - (2 * self.x)) + " " + less_more1 + " " + self.name[2] + " чем во второй. Сколько " \
                      + self.name[2] + " собрали за оба дня?"

        if show_answer_marker is True:
            base_string = base_string + " " + str(self.right_answer)

        return base_string


if __name__ == '__main__':
    task = FruitPicking()
    print(task.generate_question_string())
    task.get_answer_console()
    if task.check_answer() == 1:
        print("Ура")
