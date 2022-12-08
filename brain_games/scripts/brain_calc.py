#!/usr/bin/env python3
# запуск игры - калькулятор
from brain_games.games.start_game import start_game
from brain_games.games.calc \
    import brain_calc_rule, brain_calc_task, check_brain_calc


def main():
    start_game(brain_calc_rule, brain_calc_task, check_brain_calc)


if __name__ == '__main__':
    main()
