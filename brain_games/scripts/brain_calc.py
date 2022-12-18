#!/usr/bin/env python3
# запуск игры - калькулятор
from brain_games.games.start_game import start_game
from brain_games.games import calc


def main():
    start_game(calc)


if __name__ == '__main__':
    main()
