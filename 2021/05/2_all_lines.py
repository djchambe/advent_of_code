from collections import deque

def evaluate_vents(x1, y1, x2, y2, answer, vents):
    if x2 >= x1:
        x2 += 1
        x_step = 1
    else:
        x2 -= 1
        x_step = -1
    if y2 >= y1:
        y2 += 1
        y_step = 1
    else:
        y2 -= 1
        y_step = -1

    if abs(x2 - x1) == 1 or abs(y2 - y1) == 1:
        for i in range(x1, x2, x_step):
            for j in range(y1, y2, y_step):
                vents[i][j] += 1
                if vents[i][j] == 2:
                    answer += 1
    else:
        for i in range(0, x2-x1, x_step):
            vents[x1 + i][y1 + y_step*abs(i)] += 1
            if vents[x1 + i][y1 + y_step*abs(i)] == 2:
                answer += 1
    return answer, vents

def handler():
    coordinates = deque()
    maximum = 0
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            comma_line = clean_line.replace(' -> ', ',')
            line_list = comma_line.split(',')
            line_max = max(line_list)
            if int(line_max) > maximum:
                maximum = int(line_max)
            coordinates.extend(line_list)
    
    maximum += 1
    vents = [[0 for i in range(maximum)] for j in range(maximum)]
    answer = 0

    while len(coordinates) > 0:
        x1 = int(coordinates.popleft())
        y1 = int(coordinates.popleft())
        x2 = int(coordinates.popleft())
        y2 = int(coordinates.popleft())
        answer, vents = evaluate_vents(x1, y1, x2, y2, answer, vents)
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()