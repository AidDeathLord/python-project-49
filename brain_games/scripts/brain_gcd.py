#!/usr/bin/env python3
# запуск игры - НОД
from brain_games.games.start_game import start_game
from brain_games.games.gcd \
    import brain_gcd_rule, brain_gcd_task, check_brain_gcd


def main():
    start_game(brain_gcd_rule, brain_gcd_task, check_brain_gcd)


if __name__ == '__main__':
    main()
