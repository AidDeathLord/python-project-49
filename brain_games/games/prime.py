# функции для игры простые числа
from random import randint

START_RANGE_QUESTION_NUM = 2
END_RANGE_QUESTION_NUM = 100
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# определяем четность
def is_prime(number):
    if number % 2 == 0:
        return True
    else:
        return False


# задание
def get_question_and_answer():
    question = randint(START_RANGE_QUESTION_NUM, END_RANGE_QUESTION_NUM)

    # вычисление правильного ответа
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
