#!/usr/bin/env python3
# запуск игры прогрессия
from brain_games.games.start_game import start_game
from brain_games.games.progression \
    import brain_progres_rule, brain_progres_task, check_brain_progres


def main():
    start_game(brain_progres_rule, brain_progres_task, check_brain_progres)


if __name__ == '__main__':
    main()
