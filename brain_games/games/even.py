# functions for 'brain-even'
from random import randint

RANGE_START_NUM = 1
RANGE_END_NUM = 20
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    # assign a random number from 1 to 20 for the task
    question = randint(RANGE_START_NUM, RANGE_END_NUM)

    # check correct answer
    answer = 'no'
    if question % 2 == 0:
        answer = 'yes'
    return (question, answer)
