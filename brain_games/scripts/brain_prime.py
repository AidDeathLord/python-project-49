#!/usr/bin/env python3
# запуск игры простые числа
from brain_games.games.start_game import start_game
from brain_games.games.prime \
    import brain_prime_rule, brain_prime_task, check_brain_prime


def main():
    start_game(brain_prime_rule, brain_prime_task, check_brain_prime)


if __name__ == '__main__':
    main()
