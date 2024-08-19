from random import choice, randint


class SimpleTasks:

    def __init__(self):
        self.question = ''
        self.answer = 0
        self.a = randint(2, 9)
        self.b = randint(2, 9)

    def multi_add(self):
        c = randint(1, 100-self.a*self.b)
        self.question = f'{self.a} * {self.b} + {c} = '
        self.answer = self.a * self.b + c

    def add_multi(self):
        c = randint(1, 100-self.a*self.b)
        self.question = f'{c} + {self.a} * {self.b} = '
        self.answer = self.a * self.b + c

    def multi_sub(self):
        c = randint(1, self.a*self.b)
        self.question = f'{self.a} * {self.b} - {c} = '
        self.answer = self.a * self.b - c

    def sub_multi(self):
        c = randint(self.a*self.b, 100)
        self.question = f'{c} - {self.a} * {self.b} = '
        self.answer = c - self.a * self.b

    def div_add(self):
        c = randint(1, 100-self.a)
        self.question = f'{self.a*self.b} : {self.b} + {c} = '
        self.answer = self.a + c

    def add_div(self):
        c = randint(1, 100-self.a)
        self.question = f'{c} + {self.a*self.b} : {self.b} = '
        self.answer = self.a + c

    def div_sub(self):
        c = randint(1, self.a-1)
        self.question = f'{self.a*self.b} : {self.b} - {c} = '
        self.answer = self.a - c

    def sub_div(self):
        c = randint(self.a, 100)
        self.question = f'{c} - {self.a*self.b} : {self.b} = '
        self.answer = c - self.a

    def get_random_func(self):
        return choice(
            [self.multi_add,
             self.add_multi,
             self.multi_sub,
             self.sub_multi,
             self.div_add,
             self.add_div,
             self.div_sub,
             self.sub_div]
        )