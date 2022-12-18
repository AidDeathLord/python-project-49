# логика игр brain-games
import prompt
from brain_games.games.welcome_user import welcome_user


def start_game(game):
    game_loops = 3  # количество игровых циклов

    # приветствие, запрос имени игрока и вывод правила игры
    gamer_name = welcome_user()  # запоминаем имя игрока
    print(f'Hello, {gamer_name}!')
    print(game.rule())

    # запуск цикла игры
    for i in range(game_loops):
        # генерируем вопрос и правильный ответ
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        # проверка
        if answer == user_answer:
            print('Correct!')
            continue
        # вы написали что надо убрать return
        # но если его убрать цикл for не будет прекращаться,
        # если ввести неверное значение
        return (print(f"'{user_answer}' is wrong answer ;(. Correct answer was\
'{answer}'. \nLet's try again, {gamer_name}!"))
    print(f"Congratulations, {gamer_name}!")
