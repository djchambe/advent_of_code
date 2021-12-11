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

def step_forward(octopuses):
    height = len(octopuses)
    width = len(octopuses[0])
    flash_list = []
    flashed_list = []
    all_flash = False
    for i in range(height):
        for j in range(width):
            octopuses, flash_list = increase_point(octopuses, [i, j],
                flash_list, flashed_list, height, width)
    while flash_list:
        point = flash_list.pop()
        flashed_list.append(point)
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
    if len(flashed_list) == height*width:
        all_flash = True
    return octopuses, all_flash

def handler():
    octopuses = []
    with open('input.txt') as input_file:
        for line in input_file:
            input_list = list(line.strip())
            octopuses.append([int(x) for x in input_list])

    all_flash = False
    answer = 0
    while not all_flash:
        answer += 1
        octopuses, all_flash = step_forward(octopuses)
        if all_flash:
            break

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()