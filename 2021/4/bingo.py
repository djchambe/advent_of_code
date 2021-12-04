import copy

def mark_bingo_boards(number, bingo_boards):
    for key, board in bingo_boards.items():
        for index, row in enumerate(board):
            if number in row:
                marked_row = ['x' if row_number == number else row_number for row_number in board[index]]
                bingo_boards[key][index] = marked_row
                break
    return bingo_boards

def evaluate_bingo_boards(bingo_boards):
    for _, board in bingo_boards.items():
        for row in board:
            bingo = True
            for item in row:
                if item != 'x':
                    bingo = False
                    break
            if bingo:
                return bingo, board
        for column_number in range(len(board[0])):
            bingo = True
            for row in board:
                if row[column_number] != 'x':
                    bingo = False
            if bingo:
                return bingo, board
    return False, []

def get_board_sum(board):
    board_sum = 0
    for row in board:
        for item in row:
            if item.isnumeric():
                board_sum += int(item)
    return board_sum

def handler():
    header = True
    board_count = 0
    bingo_boards = {}
    blank_board = [[], [], [], [], []]
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            if header:
                bingo_numbers = clean_line.split(',')
                header = False
            elif not clean_line:
                if bingo_boards.get(board_count, 'error') != 'error':
                    board_count += 1
                bingo_boards[board_count] = blank_board.copy()
            else:
                for index, row in enumerate(bingo_boards[board_count]):
                    if not row:
                        bingo_boards[board_count][index] = clean_line.split(' ')
                        while '' in bingo_boards[board_count][index]:
                            bingo_boards[board_count][index].remove('')
                        break
    
    for number in bingo_numbers:
        bingo_boards = mark_bingo_boards(number, bingo_boards)
        winner, board = evaluate_bingo_boards(bingo_boards)
        if winner:
            print(f'Winner is {board}, winning number is {number}')
            board_sum = get_board_sum(board)
            break
    
    bingo_number = int(number)

    answer = board_sum * bingo_number
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()