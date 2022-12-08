# функции для игры простые числа
from random import randint


# условие победы
def brain_prime_rule():
    return ('Answer "yes" if given number is prime. Otherwise answer "no".')


# задание
def brain_prime_task():
    return (randint(2, 100))


# проверка ответа игрока
def check_brain_prime(task, user_answer):
    correct_answer = 'yes'
    for i in range(2, int(task) - 1):
        if int(task) % i == 0:
            correct_answer = 'no'
    if correct_answer == user_answer:
        return (True, correct_answer)
    return (False, correct_answer)
