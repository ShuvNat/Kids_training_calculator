import datetime
import locale
import random

NUMBER_OF_TASKS = 5
TASK_CHOISE = {
    'Умножение со сложением': 'multi_add',
    'Умножение с вычитанием': 'multi_sub',
    'Деление со сложением': 'div_add',
    'Деление с вычитанием': 'div_sub'
}


class Tasks:

    def __init__(self):
        self.nums = []

    def get_nums(self):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        if (a, b) in self.nums:
            a = random.randint(2, 9)
            b = random.randint(2, 9)
        self.nums.append((a, b))
        return a, b

    def multi(self):
        a, b = self.get_nums()
        eque = f'{a} * {b} = '
        result = a * b
        return eque, result

    def multi_add(self):
        a, b = self.get_nums()
        c = random.randint(1, 100-a*b)
        eque = f'{a} * {b} + {c} = '
        result = a * b + c
        return eque, result

    def multi_sub(self):
        a, b = self.get_nums()
        c = random.randint(1, a*b)
        eque = f'{a} * {b} - {c} = '
        result = a * b - c
        return eque, result

    def div(self):
        a, b = self.get_nums()
        eque = f'{a*b} : {b} = '
        result = a
        return eque, result

    def div_add(self):
        a, b = self.get_nums()
        c = random.randint(1, 100-a)
        eque = f'{a*b} : {b} + {c} = '
        result = a + c
        return eque, result

    def div_sub(self):
        a, b = self.get_nums()
        c = random.randint(1, a-1)
        eque = f'{a*b} : {b} - {c} = '
        result = a - c
        return eque, result


class Stack:

    def __init__(self, max_size):
        self.__items = []
        self.__max_size = max_size

    def _is_empty(self):
        return len(self.__items) == 0

    def _is_full(self):
        return len(self.__items) == self.__max_size

    def push(self, item):
        if self._is_full():
            raise OverflowError('Стэк заполнен')
        self.__items.append(item)

    def pop(self):
        if self._is_empty():
            raise IndexError('Массив пуст')
        return self.__items.pop()

    def get_items(self):
        return self.__items


def get_tasks(size=NUMBER_OF_TASKS):
    tasks = Tasks()
    tasks_stack = Stack(size)
    choice = TASK_CHOISE
    for i in range(size):
        task_type = random.choice(list(choice.values()))
        try:
            tasks_stack.push(getattr(tasks, task_type)())
        except OverflowError:
            return
    return tasks_stack.get_items()


def get_answer():
    stack = get_tasks()
    mistakes = {}
    count = 1
    start_time = datetime.datetime.now()
    for task in stack:
        print(f'Реши пример номер {count}')
        answer = input(task[0])
        while answer is None or not answer.isdigit() or int(answer) != task[1]:
            print()
            print('Неправильно, попробуй еще раз')
            answer = input(task[0])
            mistakes[count] = mistakes.get(count, 0) + 1
        if count < len(stack):
            print(f'Правильно! Молодец! Осталось примеров: {len(stack)-count}')
        else:
            end_time = datetime.datetime.now()
            time = (end_time - start_time)

        print()
        count += 1
    return mistakes, time


def infinite(min_sec):
    if min_sec in (11, 12, 13, 14) or min_sec % 10 in (0, 5, 6, 7, 8, 9):
        infinitive = ''
    elif min_sec % 10 == 1:
        infinitive = 'а'
    else:
        infinitive = 'ы'
    return infinitive


def get_time_result(time):
    minutes = time.seconds//60
    seconds = time.seconds % 60
    inf_min = infinite(minutes)
    inf_sec = infinite(seconds)
    result_time = f'{minutes} минут{inf_min} {seconds} секнуд{inf_sec}\n'
    return result_time


def logging(result, result_time):
    file = open('Примеры статистика.txt', 'a')
    locale.setlocale(locale.LC_ALL, '')
    date = datetime.datetime.now().strftime('%d.%m.%Y, %A')
    file.write(f'{date}\n')
    file.write(f'Время решения: {result_time}')
    file.write(f'Ошибок: {str(sum(result.values()))}\n\n')
    file.close()


def main():
    result, time = get_answer()
    result_time = get_time_result(time)
    print(f'Сегодня твое время {result_time}')
    if result:
        print('Номер примера' + '\t' + 'Количество ошибок')
        for r in result.items():
            print(*r, sep='\t\t')
    else:
        result = {0: 0}
        print('Молодец! Ни одной ошибки!')
    logging(result, result_time)


if __name__ == '__main__':
    main()
