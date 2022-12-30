# функции для игры простые числа
from random import randint

START_RANGE_QUESTION_NUM = 2
END_RANGE_QUESTION_NUM = 100
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# определяем четность
def is_prime(number):
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


# задание
def get_question_and_answer():
    question = randint(START_RANGE_QUESTION_NUM, END_RANGE_QUESTION_NUM)

    # вычисление правильного ответа
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
