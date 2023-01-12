#!/usr/bin/env python3
# script for start game 'brain-gcd'
from brain_games.start_game import start_game
from brain_games.games import gcd


def main():
    start_game(gcd)


if __name__ == '__main__':
    main()
