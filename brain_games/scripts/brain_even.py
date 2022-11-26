#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        ramdom_numb = randint(1,20)
        print(f"Question: {ramdom_numb}")
        answer = prompt.string('Your answer: ')
        if ramdom_numb % 2 == 0 and answer == 'yes':
            print('Correct!')
            continue
        elif ramdom_numb % 2 == 1 and answer == 'no':
            print('Correct!')
            continue
        elif ramdom_numb % 2 == 0 and answer != 'yes':
            return (print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!"))
        else:
            return (print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"))
    return (print(f"Congratulations, {name}"))    


if __name__ == '__main__':
    main()