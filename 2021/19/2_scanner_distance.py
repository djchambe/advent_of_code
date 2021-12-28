from datetime import datetime
from collections import deque
from copy import deepcopy

def calculate_manhattan_distance(position_1, position_2):
    manhattan_distance = 0
    for i in range(len(position_1[1])):
        manhattan_distance += abs(position_1[1][i] - position_2[1][i])
    
    return manhattan_distance

def get_largest_manhattan_distance(positions):
    max_distance = 0
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i == j:
                continue
            distance = calculate_manhattan_distance(positions[i], positions[j])
            if distance > max_distance:
                max_distance = distance
    
    return max_distance

def get_same_beacons_count(beacons_1, beacons_2):
    same = 0
    for beacon_1 in beacons_1:
        for beacon_2 in beacons_2:
            if beacon_1 == beacon_2:
                same += 1
                break
    
    return same

def get_shifted_beacons(beacons, known_position, adjustments):
    shifted_beacons = []
    unknown_position = adjustments['position']
    for beacon in deepcopy(beacons):
        updated_beacon = deque(maxlen=3)
        for i in range(len(known_position)):
            updated_beacon.append(unknown_position[i] - known_position[i] + beacon[i])
        shifted_beacons.append(updated_beacon)

    return shifted_beacons

def get_unknown_beacons(unknown_beacons, adjustments):
    unknown_beacons_adjusted = []
    negations = adjustments['negations']
    rotations = adjustments['rotations']
    switch = adjustments['switch']
    for beacon in deepcopy(unknown_beacons):
        if negations:
            for i in negations:
                beacon[i] *= -1
        if rotations:
            beacon.rotate(rotations)
        elif switch:
            beacon = apply_switch(beacon, switch)
        unknown_beacons_adjusted.append(beacon)

    return unknown_beacons_adjusted

def get_unknown_position(known_beacon, unknown_beacon, known_position):
    position = []
    for i in range(len(known_position)):
        position.append(known_beacon[i] - unknown_beacon[i] + known_position[i])
    
    return position

def apply_switch(beacon, switch):
    temp = beacon[switch[0]]
    beacon[switch[0]] = beacon[switch[1]]
    beacon[switch[1]] = temp

    return beacon

def get_adjustments(
        known_beacon, unknown_beacon, known_position, negation, alteration):
    adjustments = {
        'position': [],
        'negations': [],
        'rotations': 0,
        'switch': []
    }
    unknown_beacon_copy = deepcopy(unknown_beacon)
    binary_negation = bin(negation)[2:].zfill(3)
    for index, digit in enumerate(binary_negation):
        if digit == '1':
            unknown_beacon_copy[index] *= -1
            adjustments['negations'].append(index)
    if alteration < 3:
        unknown_beacon_copy.rotate(alteration)
        adjustments['rotations'] = alteration
    elif alteration == 3:
        switch = [0, 1]
        unknown_beacon_copy = apply_switch(unknown_beacon_copy, switch)
        adjustments['switch'] = switch
    elif alteration == 4:
        switch = [0, 2]
        unknown_beacon_copy = apply_switch(unknown_beacon_copy, switch)
        adjustments['switch'] = switch
    elif alteration == 5:
        switch = [1, 2]
        unknown_beacon_copy = apply_switch(unknown_beacon_copy, switch)
        adjustments['switch'] = switch
    adjustments['position'] = get_unknown_position(
        known_beacon, unknown_beacon_copy, known_position)

    return adjustments

def try_to_find_scanner(scanners, known_scanner_number, unknown_scanner_number):
    known_beacons = scanners[known_scanner_number]['beacons']
    known_position = scanners[known_scanner_number]['position']
    unknown_beacons = deepcopy(scanners[unknown_scanner_number]['beacons'])
    for unknown_beacon in unknown_beacons:
        for known_beacon in known_beacons:
            for i in range(8):
                for j in range(6):
                    adjustments = get_adjustments(
                        known_beacon, unknown_beacon, known_position, i, j)
                    unknown_beacons_adjusted = get_unknown_beacons(
                        unknown_beacons, adjustments)
                    unknown_beacons_shifted = get_shifted_beacons(
                        unknown_beacons_adjusted, known_position, adjustments)
                    same_beacons_count = get_same_beacons_count(
                        known_beacons, unknown_beacons_shifted)
                    if same_beacons_count >= 12:
                        scanners[unknown_scanner_number]['position'] = adjustments['position']
                        scanners[unknown_scanner_number]['adjustments'] = adjustments
                        scanners[unknown_scanner_number]['beacons'] = unknown_beacons_adjusted
                        return scanners, True

    return scanners, False

def find_unknown_scanners(scanners, positions, compares):
    for position in positions:
        known_scanner_number = position[0]
        known_scanner_position = position[1]
        for scanner_number, scanner_data in deepcopy(scanners).items():
            if scanner_data['position'] is None:
                if [known_scanner_number, scanner_number] not in compares:
                    scanners, found = try_to_find_scanner(scanners, known_scanner_number, scanner_number)
                    compares.append([known_scanner_number, scanner_number])
                    if found:
                        break
    
    return scanners, compares

def get_positions(scanners):
    positions = []
    for scanner_number, scanner_data in scanners.items():
        scanner_position = scanner_data['position']
        if scanner_position is not None:
            positions.append([scanner_number, scanner_position])
    
    return positions

def find_largest_manhattan_distance(scanners):
    positions = get_positions(scanners)
    compares = []
    while len(positions) < len(scanners):
        scanners, compares = find_unknown_scanners(scanners, positions, compares)
        positions = get_positions(scanners)
    
    return get_largest_manhattan_distance(positions)

def handler():
    print(f'Start: {datetime.now()}')
    scanners = {}
    count = -1
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.rstrip()
            if 'scanner' in clean_line:
                count += 1
                scanners[count] = {}
                scanners[count]['beacons'] = []
                scanners[count]['position'] = None if count else [0, 0, 0]
            elif clean_line:
                beacon_coordinates = clean_line.split(',')
                scanners[count]['beacons'].append(deque([int(coordinate) for coordinate in beacon_coordinates], maxlen=3))
    
    answer = find_largest_manhattan_distance(scanners)
    
    print(f'The answer is {answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
