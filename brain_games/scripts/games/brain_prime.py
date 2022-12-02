#!/usr/bin/env python3
# файл с игрой простое число
from brain_games.scripts.start_game import start_game
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


def main():
    start_game(brain_prime_rule, brain_prime_task, check_brain_prime)


if __name__ == '__main__':
    main()
