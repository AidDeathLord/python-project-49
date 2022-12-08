# функции для игры калькулятор
from random import randint, choice


# условие победы
def brain_calc_rule():
    return ('What is the result of the expression?')


# задание
def brain_calc_task():
    first_num = randint(10, 30)
    second_num = randint(1, 10)
    sumbol = choice(['+', '-', '*'])
    return (f'{first_num} {sumbol} {second_num}')


# проверка ответа игрока
def check_brain_calc(task, user_answer):
    split_task = task.split()
    if str(split_task[1]) == '+':
        correct_answer = int(split_task[0]) + int(split_task[2])
    if str(split_task[1]) == '-':
        correct_answer = int(split_task[0]) - int(split_task[2])
    if str(split_task[1]) == '*':
        correct_answer = int(split_task[0]) * int(split_task[2])
    if correct_answer == int(user_answer):
        return (True, correct_answer)
    if correct_answer != int(user_answer):
        return (False, correct_answer)