# functions for brain-prime
from random import randint

START_RANGE_QUESTION_NUM = 2
END_RANGE_QUESTION_NUM = 100
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# determine if a number is prime
def is_prime(number):
    if number <= 1:  # because prime numbers start with 2
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(START_RANGE_QUESTION_NUM, END_RANGE_QUESTION_NUM)

    # check correct answer
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
