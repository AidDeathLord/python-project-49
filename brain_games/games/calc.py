# functions for 'brain-calc'
from random import randint, choice
import operator


RANGE_START_NUM = 10
RANGE_END_NUM = 30
RULE = 'What is the result of the expression?'


get_operator = {'+': operator.add, '-': operator.sub,
                '*': operator.mul, '/': operator.truediv, }.get


# function calculator
def calc(first_num, second_num, operator):
    op = get_operator(operator)
    return op(first_num, second_num)


def get_question_and_answer():
    # create two random numbers for the task and a random sign
    first_num = randint(RANGE_START_NUM, RANGE_END_NUM)

    second_num = randint(RANGE_START_NUM, RANGE_END_NUM)

    operator = choice(['+', '-', '*'])

    question = (f'{first_num} {operator} {second_num}')
    answer = calc(first_num, second_num, operator)
    return (question, str(answer))
