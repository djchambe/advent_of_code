def execute_y_fold(position, paper):
    y_length = len(paper)
    for i in range(y_length-1, position-1, -1):
        for j in range(len(paper[0])):
            fold_spot = position - (i - position)
            if fold_spot >= 0:
                paper[fold_spot][j] += paper[i][j]
        paper.pop()
    return paper

def execute_x_fold(position, paper):
    x_length = len(paper[0])
    for i in range(len(paper)):
        for j in range(x_length-1, position-1, -1):
            fold_spot = position - (j - position)
            if fold_spot >=0:
                paper[i][fold_spot] += paper[i][j]
            paper[i].pop()
    return paper

def execute_fold(instructions, paper):
    axis = instructions[0]
    position = int(instructions[1])
    if axis == 'x' and position < len(paper[0]):
        paper = execute_x_fold(position, paper)
    elif axis == 'y' and position < len(paper):
        paper = execute_y_fold(position, paper)
    else:
        print(f'Axis {axis} with position {position} is not supported')
    return paper

def get_starting_paper(max_x, max_y, points):
    paper = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
    for point in points:
        paper[point[1]][point[0]] = 1
    return paper

def handler():
    points = []
    folds = []
    max_x = 0
    max_y = 0
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            if clean_line:
                point_list = clean_line.split(',')
                fold_list = clean_line.split('=')
                if len(point_list) == 2:
                    int_list = [int(position) for position in point_list]
                    if int_list[0] > max_x:
                        max_x = int_list[0]
                    if int_list[1] > max_y:
                        max_y = int_list[1]
                    points.append(int_list)
                else:
                    fold_list[0] = list(fold_list[0])[-1]
                    folds.append(fold_list)

    paper = get_starting_paper(max_x, max_y, points)
    for fold in folds:
        paper = execute_fold(fold, paper)
    
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] > 0:
                paper[i][j] = '#'
            else:
                paper[i][j] = ' '
    for line in paper:
        print(*line)

if __name__ == '__main__':
    handler()