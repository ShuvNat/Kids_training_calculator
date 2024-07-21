from datetime import datetime as dt
import subprocess

SCRIPT = "Exercise_Linear_equation.py"


class Executor:
    def __init__(self, script):
        self.start_time = dt.now()
        try:
            subprocess.run(["python", script])
        except:
            print("Не удалось запустить скрипт: " + str(script))
        self.end_time = dt.now()
        print("Время работы" + str(self.end_time - self.start_time) + " с.")


if __name__ == '__main__':
    Executor(SCRIPT)
