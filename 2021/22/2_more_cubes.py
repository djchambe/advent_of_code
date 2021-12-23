from copy import deepcopy

def get_total_on_cubes(cubes_on):
    total = 0
    for on_section in cubes_on:
        x_length = on_section[0][1] - on_section[0][0] + 1
        y_length = on_section[1][1] - on_section[1][0] + 1
        z_length = on_section[2][1] - on_section[2][0] + 1
        total += x_length * y_length * z_length
    
    return total

def remove_overlaps(on_list, overlap):
    new_on_list = []
    for on_coordinates in on_list:
        current_overlaps = evaluate_overlaps(overlap, on_coordinates)
        if current_overlaps:
            if on_coordinates == current_overlaps:
                continue
            x_on = on_coordinates[0]
            x_on_low = x_on[0]
            x_on_high = x_on[1]
            y_on = on_coordinates[1]
            y_on_low = y_on[0]
            y_on_high = y_on[1]
            z_on = on_coordinates[2]
            z_on_low = z_on[0]
            z_on_high = z_on[1]
            x_overlap = current_overlaps[0]
            x_overlap_low = x_overlap[0]
            x_overlap_high = x_overlap[1]
            y_overlap = current_overlaps[1]
            y_overlap_low = y_overlap[0]
            y_overlap_high = y_overlap[1]
            z_overlap = current_overlaps[2]
            z_overlap_low = z_overlap[0]
            z_overlap_high = z_overlap[1]
            if z_overlap_low > z_on_low:
                new_on_list.append([x_on, y_on, [z_on_low, z_overlap_low - 1]])
            if z_overlap_high < z_on_high:
                new_on_list.append([x_on, y_on, [z_overlap_high + 1, z_on_high]])
            if y_overlap_low > y_on_low:
                new_on_list.append([x_on, [y_on_low, y_overlap_low - 1], z_overlap])
            if y_overlap_high < y_on_high:
                new_on_list.append([x_on, [y_overlap_high + 1, y_on_high], z_overlap])
            if x_overlap_low > x_on_low:
                new_on_list.append([[x_on_low, x_overlap_low - 1], y_overlap, z_overlap])
            if x_overlap_high < x_on_high:
                new_on_list.append([[x_overlap_high + 1, x_on_high], y_overlap, z_overlap])
        else:
            new_on_list.append(on_coordinates)
    
    return new_on_list

def turn_off_overlaps(cubes_on, overlaps):
    indices = []
    for index, overlap in overlaps.items():
        indices.append(index)
        on_section = [cubes_on[index]]
        overlap_copy = deepcopy(overlap)
        cubes_on.extend(remove_overlaps(on_section, overlap_copy))
    indices.sort(reverse=True)
    for index in indices:
        cubes_on.pop(index)
    
    return cubes_on

def turn_on_with_overlaps(cubes_on, overlaps, coordinates_list):
    temp_on = [deepcopy(coordinates_list)]
    for overlap in overlaps.values():
        overlap_copy = deepcopy(overlap)
        temp_on = remove_overlaps(temp_on, overlap_copy)
    cubes_on.extend(temp_on)

    return cubes_on

def evaluate_overlap(coordinates, on_section):
    low_coordinate = coordinates[0]
    high_coordinate = coordinates[1]
    low_on = on_section[0]
    high_on = on_section[1]
    if low_coordinate > high_on or high_coordinate < low_on:
        return []
    if low_coordinate > low_on:
        if high_coordinate < high_on:
            return [low_coordinate, high_coordinate]
        else:
            return [low_coordinate, high_on]
    if high_coordinate < high_on:
        return [low_on, high_coordinate]
    else:
        return [low_on, high_on]

def evaluate_overlaps(new_coordinates, on_coordinates):
    x_overlap = evaluate_overlap(new_coordinates[0], on_coordinates[0])
    if not x_overlap:
        return []
    y_overlap = evaluate_overlap(new_coordinates[1], on_coordinates[1])
    if not y_overlap:
        return []
    z_overlap = evaluate_overlap(new_coordinates[2], on_coordinates[2])
    if not z_overlap:
        return []

    return [x_overlap, y_overlap, z_overlap]

def update_cubes(cubes_on, instruction, coordinates):
    overlap_dict = {}
    coordinates_list = [coordinates['x'], coordinates['y'], coordinates['z']]
    for index, on_section in enumerate(cubes_on):
        overlaps = evaluate_overlaps(coordinates_list, on_section)
        if overlaps:
            overlap_dict[index] = overlaps
    if instruction == 'on':
        if overlap_dict:
            return turn_on_with_overlaps(cubes_on, overlap_dict, coordinates_list)
        else:
            cubes_on.append(coordinates_list)
    if instruction == 'off' and overlap_dict:
        return turn_off_overlaps(cubes_on, overlap_dict)

    return cubes_on

def handler():
    coordinates_dict = {}
    cubes_on = []
    count = 0
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            clean_list = clean_line.split(' ')
            instruction = clean_list[0]
            coordinates_list = clean_list[1].split(',')
            for dimension in coordinates_list:
                dimension_list = dimension.split('=')
                axis = dimension_list[0]
                coordinate_list = dimension_list[1].split('..')
                coordinates_dict[axis] = [int(coordinate) for coordinate in coordinate_list]
            cubes_on = update_cubes(cubes_on, instruction, coordinates_dict)
            
    answer = get_total_on_cubes(cubes_on)
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()
