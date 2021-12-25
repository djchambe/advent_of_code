from copy import deepcopy
from datetime import datetime

COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

FINAL_MAP = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', 'x', '.', 'x', '.', 'x', '.', 'x', '.', '.', '#'],
    ['#', '#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#', '#'],
    [' ', ' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#'],
    [' ', ' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#'],
    [' ', ' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#'],
    [' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

FINAL_SPOTS = {
    'A': [[2, 3], [3, 3], [4, 3], [5, 3]],
    'B': [[2, 5], [3, 5], [4, 5], [5, 5]],
    'C': [[2, 7], [3, 7], [4, 7], [5, 7]],
    'D': [[2, 9], [3, 9], [4, 9], [5, 9]]
}

POD_TYPES = ['A', 'B', 'C', 'D']

OPEN_INDICATORS = ['.', 'x']

def make_move(burrow_map, current_cost, move, minimum_cost):
    pod_type = move[0]
    start_y = move[1][0]
    start_x = move[1][1]
    end_y = move[2][0]
    end_x = move[2][1]
    burrow_map[end_y][end_x] = pod_type
    burrow_map[start_y][start_x] = '.'
    current_cost += (abs(start_y - end_y) + abs(start_x - end_x)) * COSTS[pod_type]

    return recursive_moves(burrow_map, current_cost, minimum_cost)

def open_path(burrow_map, start, end):
    start_y = start[0]
    start_x = start[1]
    end_y = end[0]
    end_x = end[1]
    if start_y == 1:
        if start_x > end_x:
            for j in range(start_x-1, end_x-1, -1):
                if burrow_map[start_y][j] not in OPEN_INDICATORS:
                    return False
        else:
            for j in range(start_x+1, end_x+1, 1):
                if burrow_map[start_y][j] not in OPEN_INDICATORS:
                    return False
        for i in range(start_y+1, end_y+1, 1):
            if burrow_map[i][end_x] not in OPEN_INDICATORS:
                return False
    else:
        for i in range(start_y-1, end_y-1, -1):
            if burrow_map[i][start_x] not in OPEN_INDICATORS:
                return False
        if start_x > end_x:
            for j in range(start_x-1, end_x-1, -1):
                if burrow_map[end_y][j] not in OPEN_INDICATORS:
                    return False
        else:
            for j in range(start_x+1, end_x+1, 1):
                if burrow_map[end_y][j] not in OPEN_INDICATORS:
                    return False
    
    return True

def find_open_hallway(burrow_map):
    open_hallway_spots = []
    for index, spot in enumerate(burrow_map[1]):
        if spot == '.':
            open_hallway_spots.append([1, index])

    return open_hallway_spots

def evaluate_moves_out(burrow_map):
    moves_out = []
    in_room = []
    completed_rooms = 0
    taken_indices = []
    open_hallway_spots = find_open_hallway(burrow_map)
    if not open_hallway_spots:
        return moves_out
    for index, space in enumerate(burrow_map[2]):
        if space in POD_TYPES:
            if [2, index] in FINAL_SPOTS[space]:
                if burrow_map[3][index] == space:
                    if burrow_map[4][index] == space:
                        if burrow_map[5][index] == space:
                            completed_rooms += 1
                            taken_indices.append(index)
                            continue
            in_room.append([space, [2, index]])
            taken_indices.append(index)
    if len(in_room) != 4 - completed_rooms:
        for index, space in enumerate(burrow_map[3]):
            if index not in taken_indices:
                if space in POD_TYPES:
                    if [3, index] in FINAL_SPOTS[space]:
                        if burrow_map[4][index] == space:
                            if burrow_map[5][index] == space:
                                taken_indices.append(index)
                                continue
                    in_room.append([space, [3, index]])
                    taken_indices.append(index)
    if len(in_room) != 4 - completed_rooms:
        for index, space in enumerate(burrow_map[4]):
            if index not in taken_indices:
                if space in POD_TYPES:
                    if [4, index] in FINAL_SPOTS[space]:
                        if burrow_map[5][index] == space:
                            taken_indices.append(index)
                            continue
                    in_room.append([space, [4, index]])
                    taken_indices.append(index)
    if len(in_room) != 4 - completed_rooms:
        for index, space in enumerate(burrow_map[5]):
            if index not in taken_indices:
                if space in POD_TYPES:
                    if [5, index] in FINAL_SPOTS[space]:
                            continue
                    in_room.append([space, [5, index]])
    for pod in in_room:
        for open_hallway_spot in open_hallway_spots:
            if open_path(burrow_map, pod[1], open_hallway_spot):
                pod_copy = deepcopy(pod)
                pod_copy.append(open_hallway_spot)
                moves_out.append(pod_copy)

    return moves_out

def find_open_room(burrow_map, pod):
    final_spots = FINAL_SPOTS[pod[0]]
    occupant_0 = burrow_map[final_spots[0][0]][final_spots[0][1]]
    occupant_1 = burrow_map[final_spots[1][0]][final_spots[1][1]]
    occupant_2 = burrow_map[final_spots[2][0]][final_spots[2][1]]
    occupant_3 = burrow_map[final_spots[3][0]][final_spots[3][1]]
    if occupant_0 == '.':
        if occupant_1 == '.':
            if occupant_2 == '.':
                if occupant_3 == '.':
                    return final_spots[3]
                if occupant_3 == pod[0]:
                    return final_spots[2]
                return []
            if occupant_2 == pod[0]:
                if occupant_3 == pod[0]:
                    return final_spots[1]
            return []
        if occupant_1 == pod[0]:
            if occupant_2 == pod[0]:
                if occupant_3 == pod[0]:
                    return final_spots[0]
    return []

def evaluate_moves_in(burrow_map):
    moves_in = []
    in_hallway = []
    for index, space in enumerate(burrow_map[1]):
        if space in POD_TYPES:
            in_hallway.append([space, [1, index]])
    for pod in in_hallway:
        open_room = find_open_room(burrow_map, pod[0])
        if open_room:
            if open_path(burrow_map, pod[1], open_room):
                pod.append(open_room)
                moves_in.append(pod)
    
    return moves_in

def recursive_moves(burrow_map, current_cost, minimum_cost):
    if current_cost > minimum_cost:
        return minimum_cost
    if burrow_map == FINAL_MAP:
        return current_cost
    moves_in = evaluate_moves_in(burrow_map)
    if moves_in:
        for move in moves_in:
            minimum_cost = make_move(deepcopy(burrow_map), current_cost, move, minimum_cost)
        return minimum_cost
    moves_out = evaluate_moves_out(burrow_map)
    if moves_out:
        for move in reversed(moves_out):
            minimum_cost = make_move(deepcopy(burrow_map), current_cost, move, minimum_cost)
        return minimum_cost

    return minimum_cost

def handler():
    print(f'Start: {datetime.now()}')
    burrow_map = []
    with open('2_input.txt') as input_file:
    # use when running debugger from project root
    # with open('./2021/23/2_input.txt') as input_file:
        for line in input_file:
            clean_line = line.rstrip()
            burrow_map.append(list(clean_line))

    for x in range(3, 10, 2):
        burrow_map[1][x] = 'x'

    answer = recursive_moves(burrow_map, 0, float('inf'))
    
    print(f'The answer is {answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
