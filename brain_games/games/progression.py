# функции для игры прогрессия
from random import randint


# условие победы
def brain_progres_rule():
    return ('What number is missing in the progression?')


# задание
def brain_progres_task():
    progres_lenght = randint(4, 9)  # длина прогрессии
    progres = randint(1, 10)  # на сколько увеличивается прогрессия
    progres_start = randint(1, 20)  # стартовое значение прогрессии
    result = str(progres_start)

    # создаем рандомную прогрессию
    for i in range(progres_lenght):
        result = result + ' ' + str(progres_start + progres)
        progres_start += progres

    # убираем рандомное значение
    result_split = result.split()
    result_split[randint(0, progres_lenght)] = '..'

    # приводим к правильному выводу
    result = ''
    for i in result_split:
        result = result + i + ' '
    return result


# проверка ответа игрока
def check_brain_progres(task, user_answer):
    task_split = task.split()
    if task_split[0] == '..':
        progres = int(task_split[2]) - int(task_split[1])
        correct_result = int(task_split[1]) - progres
    elif task_split[-1] == '..':
        progres = int(task_split[-2]) - int(task_split[-3])
        correct_result = int(task_split[-2]) + progres
    else:
        for index, i in enumerate(task_split):
            if i == '..':
                progres = int((int(task_split[index + 1]) - int
                                  (task_split[index - 1])) / 2)
                correct_result = int(task_split[index + 1]) - progres
    if correct_result == int(user_answer):
        return (True, correct_result)
    return (False, correct_result)
