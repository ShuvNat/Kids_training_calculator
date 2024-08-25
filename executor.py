from datetime import datetime
import locale
from advancedmath import AdvancedTasks
from simplemath import SimpleTasks

NUMBER_OF_TASKS = 5
SHOW_ANSWER = True
IS_SIMPLE = False
WORDS_LIST = [['пример', 'примера', 'примеров'],
              ['задачу', 'задачи', 'задач'],
              ['час', 'часа', 'часов'],
              ['минута', 'минуты', 'минут'],
              ['секунда', 'секунды', 'секнуд']]


class Exercise:
    def __init__(self, show_answer=SHOW_ANSWER, is_simple=IS_SIMPLE, cfg_file=None):

        self.number_of_tasks = NUMBER_OF_TASKS
        self.task_number = 0
        self.current_task = None
        self.start_time = None
        self.end_time = None
        self.mistake_couter = {}
        self.try_counter = 0
        self.show_answer = show_answer
        self.is_simple = is_simple
        if cfg_file is not None:
            self.get_cfg_from_file(cfg_file)
        self.task_name = self.task_name_num()

    def get_task(self):
        if self.is_simple is True:
            task = SimpleTasks()
        else:
            task = AdvancedTasks()
        func = task.get_random_func()
        func()
        return task

    def check_answer(self, answer):
        if answer is None or not answer.isdigit() or int(answer) != self.current_task.answer:
            self.try_counter += 1
            return False
        return True

    def nouns_declension(self, word_num, count):
        if count in (11, 12, 13, 14) or count % 10 in (0, 5, 6, 7, 8, 9):
            word = WORDS_LIST[word_num][2]
        elif count % 10 == 1:
            word = WORDS_LIST[word_num][0]
        else:
            word = WORDS_LIST[word_num][1]
        return word

    def task_name_num(self):
        if self.is_simple is True:
            return 0
        else:
            return 1

    def get_time_result(self, time):
        seconds = time.seconds % 60
        minutes = (time.seconds // 60) % 60
        hours = time.seconds // 3600

        inf_sec = self.nouns_declension(4, seconds)
        inf_min = self.nouns_declension(3, minutes)
        inf_hours = self.nouns_declension(2, hours)

        if hours > 0:
            result_time = f'{hours} {inf_hours} {minutes} {inf_min} {seconds} {inf_sec}\n'
        else:
            result_time = f'{minutes} {inf_min} {seconds} {inf_sec}\n'
        return result_time

    def logging(self, result, result_time):
        file = open('Математический тренажер, статистика.txt', 'a')
        locale.setlocale(locale.LC_ALL, '')
        date = datetime.now().strftime('%d.%m.%Y, %A, %H:%M')
        file.write(f'{date}\n')
        file.write(f'Решено {self.task_number} {self.nouns_declension(self.task_name, self. number_of_tasks)}. ')
        file.write(f'Время решения: {result_time}')
        file.write(f'Ошибок: {str(sum(result.values()))}\n\n')
        file.close()

    def execute_in_console(self):
        self.start_time = datetime.now()
        for i in range(self.number_of_tasks):
            self.current_task = self.get_task()
            print(f'Реши {self.nouns_declension(self.task_name, 1)} номер {self.task_number+1}')
            if self.show_answer is True:
                answer = input(f'{self.current_task.question} {self.current_task.answer}')
            else:
                answer = input(self.current_task.question)
            while not self.check_answer(answer):
                print()
                print('Неправильно, попробуй еще раз')
                answer = input(self.current_task.question)
            remain = self.number_of_tasks - self.task_number - 1
            print('Правильно! Молодец!')
            print(f'Осталось решить {remain} {self.nouns_declension(self.task_name, remain)}')
            print()
            if self.try_counter != 0:
                self.mistake_couter[self.task_number+1] = self.mistake_couter.get(self.task_number+1, 0) + self.try_counter
            self.task_number += 1
            self.try_counter = 0
        self.end_time = datetime.now()
        time = self.end_time - self.start_time
        result_time = self.get_time_result(time)
        print(f'Время решения: {result_time}')
        if self.mistake_couter:
            print(f'Номер {self.nouns_declension(self.task_name, 2)}\tКоличество ошибок')
            for r in self.mistake_couter.items():
                print(*r, sep='\t\t')
        else:
            self.mistake_couter = {0: 0}
            print('Молодец! Ни одной ошибки!')
        self.logging(self.mistake_couter, result_time)

    def get_cfg_from_file(self, cfg_filename):

        try:
            file = open(cfg_filename, "r")

            for line in file:
                fields = line.strip().split()
                if fields[0] in "Number":
                    number = fields[1]
                    self.number_of_tasks = int(number)
                if fields[0] in "Answers":
                    if fields[1] in "True":
                        self.show_answer = True
                    else:
                        self.show_answer = False
                if fields[0] in "Simple":
                    if fields[1] in "True":
                        self.is_simple = True
                    else:
                        self.is_simple = False
        except IOError:
            self.number_of_tasks = NUMBER_OF_TASKS
            self.show_answer = SHOW_ANSWER
            self.is_simple = IS_SIMPLE


if __name__ == '__main__':
    filename = "config.cfg"
    Exercise(cfg_file=filename).execute_in_console()
