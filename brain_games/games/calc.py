# функции для игры калькулятор
from random import randint, choice
import operator


RANGE_START_FIRST_NUM = 10
RANGE_END_FIRST_NUM = 30
RANGE_START_SECOND_NUM = 1
RANGE_END_SECOND_NUM = 10
RULE = 'What is the result of the expression?'


get_operator = {'+': operator.add, '-': operator.sub,
                '*': operator.mul, '/': operator.truediv, }.get


# функция калькулятор
def calc(first_num, second_num, operator):
    op = get_operator(operator)
    return op(first_num, second_num)


# задание
def get_question_and_answer():
    # создаем два рандомных числа для задания и рандомный знак
    first_num = randint(RANGE_START_FIRST_NUM, RANGE_END_FIRST_NUM)

    second_num = randint(RANGE_START_SECOND_NUM, RANGE_END_SECOND_NUM)

    operator = choice(['+', '-', '*'])

    question = (f'{first_num} {operator} {second_num}')
    answer = calc(first_num, second_num, operator)
    return (question, str(answer))
