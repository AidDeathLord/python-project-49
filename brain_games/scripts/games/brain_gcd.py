#!/usr/bin/env python3
# файл с игрой НОД
from brain_games.scripts.start_game import start_game
from random import randint


# условие победы
def brain_gcd_rule():
    return ('Find the greatest common divisor of given numbers.')


# задание
def brain_gcd_task():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    return (f"{first_num} {second_num}")


# проверка ответа игрока
def check_brain_gcd(task, user_answer):
    split_task = task.split()
    first_num = int(split_task[0])
    second_num = int(split_task[1])
    for i in range(1, min(first_num, second_num)):
        if first_num % i == 0 and second_num % i == 0:
            correct_answer = i
    if correct_answer == int(user_answer):
        return (True, correct_answer)
    return (False, correct_answer)


def main():
    start_game(brain_gcd_rule, brain_gcd_task, check_brain_gcd)


if __name__ == '__main__':
    main()
