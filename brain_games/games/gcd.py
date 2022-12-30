# функции для игры НОД
from random import randint
from math import gcd

START_RANGE_QUESTION_NUMS = 1
END_RANGE_QUESTION_NUMS = 100
RULE = 'Find the greatest common divisor of given numbers.'


# задание
def get_question_and_answer():
    # задаем для задания два рандомных числа
    first_num = randint(START_RANGE_QUESTION_NUMS, END_RANGE_QUESTION_NUMS)
    second_num = randint(START_RANGE_QUESTION_NUMS, END_RANGE_QUESTION_NUMS)
    question = (f'{first_num} {second_num}')

    # вычисляем правильный ответ
    answer = gcd(first_num, second_num)
    return (question, str(answer))
