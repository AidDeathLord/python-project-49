# функции для игры четное-нечетное
from random import randint


# условие победы
def rule():
    return ('Answer "yes" if the number is even, otherwise answer "no".')


# задание
def get_question_and_answer():
    # присваиваем для задания рандомное число от 1 до 20
    min_question_num = 1
    max_question_num = 20
    question = randint(min_question_num, max_question_num)

    # ищем правильный ответ
    answer = 'no'
    if question % 2 == 0:
        answer = 'yes'
    return (question, answer)
