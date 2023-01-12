# functions for 'brain-even'
from random import randint

START_RANGE_QUESTION_NUM = 1
END_RANGE_QUESTION_NUM = 20
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    # assign a random number from 1 to 20 for the task
    question = randint(START_RANGE_QUESTION_NUM, END_RANGE_QUESTION_NUM)

    # check correct answer
    answer = 'no'
    if question % 2 == 0:
        answer = 'yes'
    return (question, answer)
