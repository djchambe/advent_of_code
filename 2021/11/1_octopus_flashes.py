def increase_point(octopuses, point, flash_list, flashed_list, height, width):
    i = point[0]
    j = point[1]
    if i < 0 or i > height - 1 or j < 0 or j > width - 1:
        return octopuses, flash_list
    octopuses[i][j] += 1
    if (octopuses[i][j] > 9 and 
            point not in flash_list and 
            point not in flashed_list):
        flash_list.append(point)
    return octopuses, flash_list

def step_forward(octopuses, flashes):
    height = len(octopuses)
    width = len(octopuses[0])
    flash_list = []
    flashed_list = []
    for i in range(height):
        for j in range(width):
            octopuses, flash_list = increase_point(octopuses, [i, j],
                flash_list, flashed_list, height, width)
    while flash_list:
        point = flash_list.pop()
        flashed_list.append(point)
        flashes += 1
        i = point[0]
        j = point[1]
        octopuses, flash_list = increase_point(octopuses, [i-1, j],
            flash_list, flashed_list, height, width)
        octopuses, flash_list = increase_point(octopuses, [i-1, j-1],
            flash_list, flashed_list, height, width)
        octopuses, flash_list = increase_point(octopuses, [i-1, j+1],
            flash_list, flashed_list, height, width)
        octopuses, flash_list = increase_point(octopuses, [i, j-1],
            flash_list, flashed_list, height, width)
        octopuses, flash_list = increase_point(octopuses, [i, j+1],
            flash_list, flashed_list, height, width)
        octopuses, flash_list = increase_point(octopuses, [i+1, j],
            flash_list, flashed_list, height, width)
        octopuses, flash_list = increase_point(octopuses, [i+1, j-1],
            flash_list, flashed_list, height, width)
        octopuses, flash_list = increase_point(octopuses, [i+1, j+1],
            flash_list, flashed_list, height, width)
    for i in range(height):
        for j in range(width):
            if octopuses[i][j] > 9:
                octopuses[i][j] = 0
    return octopuses, flashes

def handler():
    octopuses = []
    with open('input.txt') as input_file:
        for line in input_file:
            input_list = list(line.strip())
            octopuses.append([int(x) for x in input_list])
    
    answer = 0

    for _ in range(100):
        octopuses, answer = step_forward(octopuses, answer)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()