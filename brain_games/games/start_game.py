# логика игр brain-games
import prompt
from brain_games.games.welcome_user import welcome_user


def start_game(rule, task, check_user_answer):
    # приветствие, запрос имени игрока и вывод правила игры
    gamer_name = welcome_user()  # запоминаем имя игрока
    print(f'Hello, {gamer_name}!')
    print(rule())

    # запуск цикла игры
    for i in range(3):
        # вывод вопроса
        form_task = task()
        print(f'Question: {form_task}')
        user_answer = prompt.string('Your answer: ')

        # запуск проверки
        check_result, correct_answer = check_user_answer(form_task, user_answer)
        if check_result:
            print('Correct!')
            continue
        return (print(f"'{user_answer}' is wrong answer ;(. Correct answer \
was '{correct_answer}'.\nLet's try again, {gamer_name}!"))
    return (print(f"Congratulations, {gamer_name}!"))
