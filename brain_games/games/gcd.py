# функции для игры НОД
from random import randint
from math import gcd

# условие победы
def rule():
    return ('Find the greatest common divisor of given numbers.')


# задание
def get_question_and_answer():
    # задаем для задания два рандомных числа
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = (f'{first_num} {second_num}')

    # вычисляем правильный ответ
    answer = gcd(first_num, second_num)
    return (question, str(answer))
