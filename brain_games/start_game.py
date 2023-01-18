# logics for brain-games
import prompt
from brain_games.games.welcome_user import welcome_user

LOOPS_COUNT = 3  # games loops count


def start_game(game):
    # greeting, requesting the player's name and print the game rule
    gamer_name = welcome_user()  # save gammer name
    print(f'Hello, {gamer_name}!')
    print(game.RULE)

    # start game
    for i in range(LOOPS_COUNT):
        # generating a question and a correct answer
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        # check
        if correct_answer != user_answer:
            print(f'\'{user_answer}\' is wrong answer ;(.')
            print(f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {gamer_name}!')
            return
        print('Correct!')
        continue

    print(f'Congratulations, {gamer_name}!')
