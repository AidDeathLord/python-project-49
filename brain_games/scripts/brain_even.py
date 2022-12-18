#!/usr/bin/env python3
# запуск игры четное - нечетное
from brain_games.games.start_game import start_game
from brain_games.games import even


def main():
    start_game(even)


if __name__ == '__main__':
    main()
