#!/usr/bin/env python3
# запуск игры простые числа
from brain_games.games.start_game import start_game
from brain_games.games import prime


def main():
    start_game(prime)


if __name__ == '__main__':
    main()
