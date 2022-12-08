#!/usr/bin/env python3
# запуск игры четное - нечетное
from brain_games.games.start_game import start_game
from brain_games.games.even \
    import brain_even_rule, brain_even_task, check_brain_even


def main():
    start_game(brain_even_rule, brain_even_task, check_brain_even)


if __name__ == '__main__':
    main()
