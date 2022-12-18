# функции для игры простые числа
from random import randint


# условие победы
def rule():
    return ('Answer "yes" if given number is prime. Otherwise answer "no".')


# задание
def get_question_and_answer():
    min_question_num = 2
    max_question_num = 100
    question = randint(min_question_num, max_question_num)

    # вычисление правильного ответа
    answer = 'yes'
    for i in range(2, question - 1):
        if question % i == 0:
            answer = 'no'
    return (question, answer)
