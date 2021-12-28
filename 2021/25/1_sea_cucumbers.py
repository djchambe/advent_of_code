from datetime import datetime

def move_south(sea_map):
    moved = []
    for i in range(len(sea_map)):
        for j in range(len(sea_map[0])):
            if [i, j] in moved:
                continue
            if sea_map[i][j] == 'v':
                if i+1 == len(sea_map):
                    if sea_map[0][j] == '.' and [0, j] not in moved:
                        sea_map[0][j] = 'v'
                        sea_map[i][j] = '.'
                        moved.append([0, j])
                        moved.append([i, j])
                else:
                    if sea_map[i+1][j] == '.' and [i+1, j] not in moved:
                        sea_map[i+1][j] = 'v'
                        sea_map[i][j] = '.'
                        moved.append([i+1, j])
                        moved.append([i, j])
    
    return sea_map, moved

def move_east(sea_map):
    moved = []
    for i in range(len(sea_map)):
        for j in range(len(sea_map[0])):
            if [i, j] in moved:
                continue
            if sea_map[i][j] == '>':
                if j+1 == len(sea_map[0]):
                    if sea_map[i][0] == '.' and [i, 0] not in moved:
                        sea_map[i][0] = '>'
                        sea_map[i][j] = '.'
                        moved.append([i, 0])
                        moved.append([i, j])
                else:
                    if sea_map[i][j+1] == '.' and [i, j+1] not in moved:
                        sea_map[i][j+1] = '>'
                        sea_map[i][j] = '.'
                        moved.append([i, j+1])
                        moved.append([i, j])
    
    return sea_map, moved

def move_sea_cucumbers(sea_map):
    combined_moves = []
    sea_map, moved_east = move_east(sea_map)
    sea_map, moved_south = move_south(sea_map)
    combined_moves.extend(moved_east)
    combined_moves.extend(moved_south)

    return sea_map, combined_moves

def handler():
    print(f'Start: {datetime.now()}')
    sea_map = []
    with open('input.txt') as input_file:
    # with open('test_input.txt') as input_file:
        for line in input_file:
            clean_line = line.rstrip()
            sea_map.append(list(clean_line))

    answer = 0
    while True:
        answer += 1
        sea_map, moved = move_sea_cucumbers(sea_map)
        # print(answer)
        # for line in sea_map:
        #     print(*line)
        if not moved:
            break
    
    print(f'The answer is {answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
