# functions for brain-progression
from random import randint

START_RANGE_PROGRES_LENGTH = 4
END_RANGE_PROGRES_LENGTH = 9
START_RANGE_PROGRES = 1
END_RANGE_PROGRES = 10
START_RANGE_PRGRES_START = 1
END_RANGE_PRGRES_START = 20
RULE = 'What number is missing in the progression?'


def create_progression(lenght, progres, start_num):
    result = [start_num]
    for i in range(lenght):
        result.append(result[-1] + progres)
    return result


def get_question_and_answer():
    progres_lenght = randint(START_RANGE_PROGRES_LENGTH,
                             END_RANGE_PROGRES_LENGTH)

    progres = randint(START_RANGE_PROGRES, END_RANGE_PROGRES)

    progres_start = randint(START_RANGE_PRGRES_START, END_RANGE_PRGRES_START)

    progression = create_progression(progres_lenght, progres, progres_start)

    # remove random value
    null_value = randint(0, progres_lenght)
    answer = progression[null_value]  # assign the correct answer
    progression[null_value] = '..'

    # rewrite the question
    question = ''
    for i in progression:
        question = question + str(i) + ' '
    return (question, str(answer))
