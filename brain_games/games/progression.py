# функции для игры прогрессия
from random import randint


# условие победы
def rule():
    return ('What number is missing in the progression?')


# задание
def get_question_and_answer():
    min_progres_lenght = 4
    max_progres_lenght = 9
    progres_lenght = randint(min_progres_lenght, max_progres_lenght)

    min_progres = 1
    max_progres = 10
    progres = randint(min_progres, max_progres)

    min_progres_start = 1
    max_progres_start = 20
    progres_start = randint(min_progres_start, max_progres_start)

    # создаем рандомную прогрессию
    result = [progres_start]
    for i in range(progres_lenght):
        result.append(progres_start + progres)
        progres_start += progres

    # убираем рандомное значение
    null_value = randint(0, progres_lenght)
    answer = result[null_value]  # присваиваем правильный ответ
    result[null_value] = '..'

    # переписываем правильно вопрос
    question = ''
    for i in result:
        question = question + str(i) + ' '
    return (question, str(answer))
