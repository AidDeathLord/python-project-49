#!/usr/bin/env python3
# script for start game 'brain-even'
from brain_games.start_game import start_game
from brain_games.games import even


def main():
    start_game(even)


if __name__ == '__main__':
    main()
