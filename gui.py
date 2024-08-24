from datetime import datetime
import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from executor import Exercise

config_filename = 'config.cfg'


class MainWindow(QMainWindow, Exercise):

    def __init__(self):
        QMainWindow.__init__(self)
        Exercise.__init__(self)

        self.setWindowTitle("Математический тренажер")

        self.get_cfg_from_file(config_filename)
        self.task_name = self.task_name_num()

        if self.is_simple is not True:
            self.setFixedWidth(530)
            self.setFixedHeight(200)

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()

        self.task_label = QLabel(f'Реши {self.nouns_declension(self.task_name, 1)} номер {self.task_number}')
        self.question_label = QLabel('')
        self.answer_input = QLineEdit()
        self.answer_input.returnPressed.connect(self.check_answer_gui)
        self.check_label = QLabel('')
        self.count_douwn_label = QLabel('')
        self.button = QPushButton('Проверить ответ')
        self.button.clicked.connect(self.check_answer_gui)

        if self.is_simple is True:
            layout2.addWidget(self.question_label)
            layout2.addWidget(self.answer_input)
            layout1.addWidget(self.task_label)
            layout1.addLayout(layout2)
        else:
            layout1.addWidget(self.task_label)
            layout1.addWidget(self.question_label)
            layout1.addWidget(self.answer_input)
        layout1.addWidget(self.check_label)
        layout1.addWidget(self.count_douwn_label)
        layout1.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

        self.start_time = datetime.now()
        self.execute_in_gui()

    def execute_in_gui(self):
        if self.task_number > self.number_of_tasks:
            self.end_time = datetime.now()
            time = self.end_time - self.start_time
            result_time = self.get_time_result(time)
            self.check_label.setText(f'Время решения: {result_time}Количество ошибок {sum(self.mistake_couter.values())}')
            self.count_douwn_label.setText('')
            self.logging(self.mistake_couter, result_time)
            self.answer_input.returnPressed.disconnect()
            self.button.setEnabled(False)
            return

        self.current_task = self.get_task()
        self.task_label.setText(f'Реши {self.nouns_declension(self.task_name, 1)} номер {self.task_number}')
        if self.show_answer is True:
            self.question_label.setText(f'{self.current_task.question} {self.current_task.answer}')
        else:
            self.question_label.setText(self.current_task.question)
        self.answer_input.clear()
        self.check_label.setText('')
        self.count_douwn_label.setText('')
        self.button.setText('Проверить ответ')
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.check_answer_gui)
        self.answer_input.setFocus()

    def check_answer_gui(self):
        answer = self.answer_input.text()
        if not answer.isdigit() or int(answer) != self.current_task.answer:
            self.try_counter += 1
            self.answer_input.clear()
            self.check_label.setText('Неправильно. Попробуй еще раз.')
        else:
            remain = self.number_of_tasks - self.task_number
            self.check_label.setText('Правильно! Молодец!')
            self.count_douwn_label.setText(f'Осталось решить {remain} {self.nouns_declension(self.task_name, remain)}')
            if self.try_counter != 0:
                self.mistake_couter[self.task_number] = self.mistake_couter.get(self.task_number, 0) + self.try_counter
            self.task_number += 1
            self.try_counter = 0
            if self.task_number > self.number_of_tasks:
                self.button.setText('Посмотреть результат')
            else:
                if self.is_simple is True:
                    self.button.setText('Следующий пример')
                else:
                    self.button.setText('Следующая задача')
            self.button.setDefault(True)
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.execute_in_gui)
            self.button.setFocus()

    def closeEvent(self, event):
        if self.task_number <= self.number_of_tasks and self.task_number != 1:
            self.end_time = datetime.now()
            time = self.end_time - self.start_time
            result_time = self.get_time_result(time)
            self.logging(self.mistake_couter, result_time)
        event.accept()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
