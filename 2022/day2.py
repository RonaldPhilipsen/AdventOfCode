from advent_of_code import get_input

"""do the rock_paper scissors exercise """
I_ROCK = 'A'
I_PAPER = 'B'
I_SCISSORS = 'C'

O_ROCK_LOSE = 'X'
O_PAPER_DRAW = 'Y'
O_SCISSORS_WIN = 'Z'

SCORE_ROCK = 1
SCORE_PAPER = 2
SCORE_SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

scores_map = {
    f'{I_ROCK} {O_ROCK_LOSE}': [(SCORE_ROCK + DRAW), (SCORE_SCISSORS + LOSS)],
    f'{I_ROCK} {O_PAPER_DRAW}': [(SCORE_PAPER + WIN), (SCORE_ROCK + DRAW)],
    f'{I_ROCK} {O_SCISSORS_WIN}': [(SCORE_SCISSORS + LOSS), (SCORE_PAPER + WIN)],
    f'{I_PAPER} {O_ROCK_LOSE}': [(SCORE_ROCK + LOSS), (SCORE_ROCK + LOSS)],
    f'{I_PAPER} {O_PAPER_DRAW}': [(SCORE_PAPER + DRAW), (SCORE_PAPER + DRAW)],
    f'{I_PAPER} {O_SCISSORS_WIN}': [(SCORE_SCISSORS + WIN), (SCORE_SCISSORS + WIN)],
    f'{I_SCISSORS} {O_ROCK_LOSE}': [(SCORE_ROCK + WIN), (SCORE_PAPER + LOSS)],
    f'{I_SCISSORS} {O_PAPER_DRAW}': [(SCORE_PAPER + LOSS), (SCORE_SCISSORS + DRAW)],
    f'{I_SCISSORS} {O_SCISSORS_WIN}': [(SCORE_SCISSORS + DRAW), (SCORE_ROCK + WIN)],
}

if __name__ == "__main __":
    input_str = get_input(2).strip()
    input_list = input_str.split('\n')

    scores_part1 = [scores_map[i][0] for i in input_list if i]
    scores_part2 = [scores_map[i][1] for i in input_list if i]
    print(f'Total: {sum(scores_part1)}')
    print(f'Total: {sum(scores_part2)}')
