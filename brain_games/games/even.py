# функции для игры четное-нечетное
from random import randint


# условие победы
def brain_even_rule():
    return ('Answer "yes" if the number is even, otherwise answer "no".')


# задание
def brain_even_task():
    return (randint(1, 20))


# проверка ответа игрока
def check_brain_even(task, user_answer):
    correct_answer = 'no'
    if task % 2 == 0:
        correct_answer = 'yes'
    if correct_answer == user_answer:
        return (True, correct_answer)
    return (False, correct_answer)
