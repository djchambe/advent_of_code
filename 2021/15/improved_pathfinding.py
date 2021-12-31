from datetime import datetime
from heapq import heappop, heappush

CONNECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def pathfind(risks):
    height = len(risks)
    width = len(risks[0])
    visited = {(0, 0)}
    to_evaluate = [(0, 0, 0)]

    while to_evaluate:
        current_risk, y, x = heappop(to_evaluate)
        if y == height - 1 and x == width - 1:
            part_1_answer = current_risk
        if y == height * 5 - 1 and x == width * 5 - 1:
            return part_1_answer, current_risk
        for connection in CONNECTIONS:
            new_y = y + connection[0]
            new_x = x + connection[1]
            if (0 <= new_y < height * 5 and
                0 <= new_x < width * 5 and
                (new_y, new_x) not in visited):
                y_addition, y_lookup = divmod(new_y, height)
                x_addition, x_lookup = divmod(new_x, width)
                new_risk = risks[y_lookup][x_lookup] + y_addition + x_addition
                new_risk = (new_risk - 1) % 9 + 1
                heappush(to_evaluate, (current_risk + new_risk, new_y, new_x))
                visited.add((new_y, new_x))

def handler():
    print(f'Start: {datetime.now()}')
    risks = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            risks.append([int(risk) for risk in clean_line])

    part_1_answer, part_2_answer = pathfind(risks)
    
    print(f'The part 1 answer is {part_1_answer}')
    print(f'The part 2 answer is {part_2_answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()