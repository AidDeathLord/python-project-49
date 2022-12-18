# функции для игры калькулятор
from random import randint, choice


# условие победы
def rule():
    return ('What is the result of the expression?')


# задание
def get_question_and_answer():
    # создаем два рандомных числа для задания и рандомный знак
    min_value_first_num = 10
    max_value_first_num = 30
    first_num = randint(min_value_first_num, max_value_first_num)

    min_value_second_num = 1
    max_value_second_num = 10
    second_num = randint(min_value_second_num, max_value_second_num)

    sumbol = choice(['+', '-', '*'])

    question = (f'{first_num} {sumbol} {second_num}')

    # вычисляем правильный ответ
    if sumbol == '+':
        answer = first_num + second_num
    if sumbol == '-':
        answer = first_num - second_num
    if sumbol == '*':
        answer = first_num * second_num
    return (question, str(answer))
