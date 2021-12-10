def get_basins(height_map, low_points):
    height = len(height_map)
    width = len(height_map[0])

    basin_sizes = []

    for point in low_points:
        unexplored = [point]
        explored = []
        while unexplored:
            coordinates = unexplored.pop()
            i = coordinates[0]
            j = coordinates[1]
            if i > 0:
                if height_map[i-1][j] != '9':
                    if [i-1, j] not in unexplored and [i-1, j] not in explored:
                        unexplored.append([i-1, j])
            if i < height - 1:
                if height_map[i+1][j] != '9':
                    if [i+1, j] not in unexplored and [i+1, j] not in explored:
                        unexplored.append([i+1, j])
            if j > 0:
                if height_map[i][j-1] != '9':
                    if [i, j-1] not in unexplored and [i, j-1] not in explored:
                        unexplored.append([i, j-1])
            if j < width - 1:
                if height_map[i][j+1] != '9':
                    if [i, j+1] not in unexplored and [i, j+1] not in explored:
                        unexplored.append([i, j+1])
            explored.append(coordinates)

        basin_sizes.append(len(explored))
    
    print(basin_sizes)
    basins = []
    for k in range(3):
        maximum = max(basin_sizes)
        basins.append(maximum)
        basin_sizes.remove(maximum)
    print(basins)
    return basins

def get_low_points(height_map):
    height = len(height_map)
    width = len(height_map[0])

    low_points = []

    for i in range(height):
        for j in range(width):
            if i > 0:
                if height_map[i][j] >= height_map[i-1][j]:
                    continue
            if i < height - 1:
                if height_map[i][j] >= height_map[i+1][j]:
                    continue
            if j > 0:
                if height_map[i][j] >= height_map[i][j-1]:
                    continue
            if j < width - 1:
                if height_map[i][j] >= height_map[i][j+1]:
                    continue
            low_points.append([i, j])

    return low_points

def handler():
    height_map = []
    with open('input.txt') as input_file:
        for line in input_file:
            height_map.append(list(line.strip()))
    
    low_points = get_low_points(height_map)
    basins = get_basins(height_map, low_points)

    answer = 1
    for basin in basins:
        answer *= basin

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()