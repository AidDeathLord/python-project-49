#!/usr/bin/env python3
# script for start game 'brain-calc'
from brain_games.start_game import start_game
from brain_games.games import calc


def main():
    start_game(calc)


if __name__ == '__main__':
    main()
