import sys

# read in numbers
nums = list(map(int, sys.stdin.readline().strip().split(',')))

# read in boards
boards = []
i=-1
for line in ''.join(sys.stdin.readlines()).split('\n'):
    if line == '':
        boards.append([])
        i+=1
    else: 
        boards[i].append(list(map(int, line.split())))
boards.pop()

def cross_num(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = '*'
    return board

def check_bingo(board):
    # check cols
    for i in range(5):
        c = 0
        for j in range(5):
            if board[i][j] == '*':
                c += 1
        if c == 5:
            return True

    # check cols
    for j in range(5):
        c = 0
        for i in range(5):
            if board[i][j] == '*':
                c += 1
        if c == 5:
            return True
    return False

def sum_over_values(board):
    s = 0
    for i in range(5):
        for j in range(5):
            if type(board[i][j]) == int:
                s+= board[i][j]
    return s

def play_game(nums, boards):
    not_yet_won = set(range(len(boards)))

    for num in nums:
        for i in range(len(boards)):
            if i in not_yet_won:
                cross_num(boards[i], num)
                if check_bingo(boards[i]):
                    not_yet_won.remove(i)
                    if len(not_yet_won) == 0:
                        return sum_over_values(boards[i]) * num

print(play_game(nums, boards))
