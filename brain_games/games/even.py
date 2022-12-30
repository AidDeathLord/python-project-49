# функции для игры четное-нечетное
from random import randint

START_RANGE_QUESTION_NUM = 1
END_RANGE_QUESTION_NUM = 20
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


# задание
def get_question_and_answer():
    # присваиваем для задания рандомное число от 1 до 20
    question = randint(START_RANGE_QUESTION_NUM, END_RANGE_QUESTION_NUM)

    # ищем правильный ответ
    answer = 'no'
    if question % 2 == 0:
        answer = 'yes'
    return (question, answer)
