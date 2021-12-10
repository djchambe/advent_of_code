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
            low_points.append(int(height_map[i][j]))
    return low_points

def handler():
    height_map = []
    with open('input.txt') as input_file:
        for line in input_file:
            height_map.append(list(line.strip()))
    
    low_points = get_low_points(height_map)

    answer = 0
    for point in low_points:
        answer += point + 1

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()