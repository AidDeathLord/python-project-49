#!/usr/bin/env python3
# запуск игры прогрессия
from brain_games.games.start_game import start_game
from brain_games.games import progression


def main():
    start_game(progression)


if __name__ == '__main__':
    main()
