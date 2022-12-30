# логика игр brain-games
import prompt
from brain_games.games.welcome_user import welcome_user

GAME_LOOPS = 3  # количество игровых циклов


def start_game(game):
    # приветствие, запрос имени игрока и вывод правила игры
    gamer_name = welcome_user()  # запоминаем имя игрока
    print(f'Hello, {gamer_name}!')
    print(game.RULE)

    # запуск цикла игры
    for i in range(GAME_LOOPS):
        # генерируем вопрос и правильный ответ
        question, ans = game.get_question_and_answer()
        print(f'Question: {question}')
        user_ans = prompt.string('Your answer: ')

        # проверка
        if ans == user_ans:
            print('Correct!')
            continue
        print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{ans}'.")
        print(f"Let's try again, {gamer_name}!")
        return
    print(f'Congratulations, {gamer_name}!')
