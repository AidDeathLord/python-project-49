#!/usr/bin/env python3
# файл с игрой четное - нечетное
from brain_games.scripts.start_game import start_game
from random import randint


# условие победы
def brain_even_rule():
    return ('Answer "yes" if the number is even, otherwise answer "no".')


# задание
def brain_even_task():
    return (randint(1, 20))


# проверка ответа игрока
def check_brain_even(task, user_answer):
    if task % 2 == 0:
        correct_answer = 'yes'
    correct_answer = 'no'
    if correct_answer == user_answer:
        return (True, correct_answer)
    return (False, correct_answer)


def main():
    start_game(brain_even_rule, brain_even_task, check_brain_even)


if __name__ == '__main__':
    main()
