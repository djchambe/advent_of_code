from datetime import datetime
from collections import deque
from copy import deepcopy
from statistics import mode

def get_max_distance(scanner_positions):
    max_distance = 0
    for i in range(len(scanner_positions)):
        for j in range(i+1, len(scanner_positions), 1):
            distance = (abs(scanner_positions[i][0] - scanner_positions[j][0]) +
                abs(scanner_positions[i][1] - scanner_positions[j][1]) +
                abs(scanner_positions[i][2] - scanner_positions[j][2]))
            if distance > max_distance:
                max_distance = distance
    
    return max_distance

def count_beacons(scanners):
    beacon_list = []
    for scanner, scanner_data in scanners.items():
        scanner_beacons = scanner_data['beacons']
        for beacon in scanner_beacons:
            if beacon not in beacon_list:
                beacon_list.append(beacon)
    
    return len(beacon_list)

def apply_adjustments(scanners, adjustments, unknown_scanner, diff_lookup):
    movements = adjustments['movements']
    negations = adjustments['negations']
    translations = adjustments['translations']
    beacons = scanners[unknown_scanner]['beacons']
    differences = scanners[unknown_scanner]['differences']
    for beacon_pair, difference in differences.items():
        differences[beacon_pair] = apply_movements(movements, difference)
    for index, beacon in enumerate(beacons):
        new_beacon = deque()
        for i in range(len(beacon)):
            new_beacon.append(beacon[movements[i]])
            if negations[i] == '1':
                new_beacon[i] *= -1
            new_beacon[i] += translations[i]
        beacons[index] = new_beacon
    scanners[unknown_scanner]['position'] = translations

    return scanners

def apply_test_negation(test_negation, control_known_coordinates,
        control_unknown_coordinates, test_coordinates):
        altered_test_coordinates = test_coordinates
        translations = []
        for index, i in enumerate(test_negation):
            if i == '1':
                altered_test_coordinates[index] *= -1
                control_unknown_coordinates[index] *= -1
            translations.append(control_known_coordinates[index] - control_unknown_coordinates[index])
            altered_test_coordinates[index] = test_coordinates[index] + translations[index]

        return altered_test_coordinates, translations

def apply_movements(movements, coordinates):
    new_coordinates = deque(maxlen=3)
    for index in range(3):
        new_coordinates.append(coordinates[movements[index]])
    
    return new_coordinates

def get_negations_and_translations(scanners, adjustments, known_scanner,
        unknown_scanner, control_known_beacon, control_unknown_beacon,
        test_known_beacon, test_unknown_beacon):
    control_known_beacon_coordinates = scanners[known_scanner]['beacons'][control_known_beacon]
    control_unknown_beacon_coordinates = scanners[unknown_scanner]['beacons'][control_unknown_beacon]
    test_known_beacon_coordinates = scanners[known_scanner]['beacons'][test_known_beacon]
    test_unknown_beacon_coordinates = scanners[unknown_scanner]['beacons'][test_unknown_beacon]
    movements = adjustments['movements']
    moved_control_unknown_beacon_coordinates = apply_movements(movements, control_unknown_beacon_coordinates)
    moved_test_unknown_beacon_coordinates = apply_movements(movements, test_unknown_beacon_coordinates)
    for negation in range(8):
        test_negation = bin(negation)[2:].zfill(3)
        test_coordinates, translations = apply_test_negation(
            test_negation, control_known_beacon_coordinates,
            deepcopy(moved_control_unknown_beacon_coordinates),
            deepcopy(moved_test_unknown_beacon_coordinates))
        if test_coordinates == test_known_beacon_coordinates:
            adjustments['negations'] = test_negation
            adjustments['translations'] = translations
            break
    
    if not adjustments.get('negations', ''):
        print('Did not find negations, please interrupt program')

    return adjustments

def get_movements(scanners, diff_to_evaluate, known_scanner,
        known_scanner_index, unknown_scanner, unknown_scanner_index):
    movements = {}
    known_diff_key = diff_to_evaluate[known_scanner_index]
    unknown_diff_key = diff_to_evaluate[unknown_scanner_index]
    known_diff = scanners[known_scanner]['differences'][known_diff_key]
    unknown_diff = scanners[unknown_scanner]['differences'][unknown_diff_key]
    for index, axis_diff in enumerate(known_diff):
        for index_2, axis_diff_2 in enumerate(unknown_diff):
            if axis_diff == axis_diff_2:
                movements[index] = index_2
    if len(movements) != 3:
        print('Diff was not the same, please interrupt program')

    return movements

def get_adjustments(scanners, diff_to_evaluate, pair_beacon_matches,
        known_scanner, known_scanner_index, unknown_scanner,
        unknown_scanner_index):
    adjustments = {}
    control_known_beacon = diff_to_evaluate[known_scanner_index][0]
    test_known_beacon = diff_to_evaluate[known_scanner_index][1]
    for match in pair_beacon_matches:
        if match[known_scanner_index] == control_known_beacon:
            control_unknown_beacon = match[unknown_scanner_index]
        elif match[known_scanner_index] == test_known_beacon:
            test_unknown_beacon = match[unknown_scanner_index]
    if (control_unknown_beacon not in diff_to_evaluate[unknown_scanner_index] or
        test_unknown_beacon not in diff_to_evaluate[unknown_scanner_index]):
        print('Found wrong beacon match, please interrupt program')
    adjustments['movements'] = get_movements(
        scanners, diff_to_evaluate, known_scanner, known_scanner_index,
        unknown_scanner, unknown_scanner_index)
    adjustments = get_negations_and_translations(
        scanners, adjustments, known_scanner, unknown_scanner,
        control_known_beacon, control_unknown_beacon,
        test_known_beacon, test_unknown_beacon)

    return adjustments

def evaluate_diff(scanners, known_scanner, known_scanner_index, diff_to_evaluate):
    known_scanner_diff = scanners[known_scanner]['differences'][diff_to_evaluate[known_scanner_index]]
    for diff in known_scanner_diff:
        if known_scanner_diff.count(diff) > 1:
            return False

    return True

def find_scanner_positions(scanners, overlap_scanners, matching_beacons):
    scanner_positions = {0: [0, 0, 0]}
    while len(scanner_positions) < len(scanners):
        for scanner_pair, same_diff_beacons in overlap_scanners.items():
            if (scanner_pair[0] in scanner_positions and
                scanner_pair[1] not in scanner_positions):
                known_scanner = scanner_pair[0]
                known_scanner_index = 0
                unknown_scanner = scanner_pair[1]
                unknown_scanner_index = 1
            elif (scanner_pair[1] in scanner_positions and
                scanner_pair[0] not in scanner_positions):
                unknown_scanner = scanner_pair[0]
                unknown_scanner_index = 0
                known_scanner = scanner_pair[1]
                known_scanner_index = 1
            else:
                continue
            found_good_diff = False
            diff_index = -1
            while found_good_diff == False:
                diff_index += 1
                diff_to_evaluate = same_diff_beacons[diff_index]
                found_good_diff = evaluate_diff(
                    scanners, known_scanner, known_scanner_index, diff_to_evaluate)
            pair_beacon_matches = matching_beacons[scanner_pair]
            adjustments = get_adjustments(
                scanners, diff_to_evaluate, pair_beacon_matches, known_scanner,
                known_scanner_index, unknown_scanner, unknown_scanner_index)
            diff_lookup = diff_to_evaluate[unknown_scanner_index]
            scanners = apply_adjustments(scanners, adjustments, unknown_scanner, diff_lookup)
            scanner_positions[unknown_scanner] = scanners[unknown_scanner]['position']

    return scanners, scanner_positions

def find_matching_beacons(overlap_scanners):
    matching_beacons = {}
    for scanner_pair, same_diff_beacons in overlap_scanners.items():
        matching_beacons[scanner_pair] = []
        occurrences = {}
        for beacons_pair in same_diff_beacons:
            scanner_1_pair = beacons_pair[0]
            scanner_2_pair = beacons_pair[1]
            for beacon in scanner_1_pair:
                if beacon in occurrences:
                    occurrences[beacon].extend(scanner_2_pair)
                else:
                    occurrences[beacon] = [scanner_2_pair[0], scanner_2_pair[1]]
        for beacon, possibilities in occurrences.items():
            matching_beacons[scanner_pair].append((beacon, mode(possibilities)))
    
    return matching_beacons

def find_overlap_scanners(scanners):
    overlap_scanners = {}
    searched_scanners = []
    for number_1, scanner_1 in scanners.items():
        for number_2, scanner_2 in scanners.items():
            if ([number_1, number_2] in searched_scanners or
                [number_2, number_1] in searched_scanners or
                number_1 == number_2):
                continue
            same_diffs = []
            diffs_1 = scanner_1['differences']
            diffs_2 = scanner_2['differences']
            for pair_1, diff_1 in diffs_1.items():
                for pair_2, diff_2 in diffs_2.items():
                    if diff_1[0] in diff_2 and diff_1[1] in diff_2 and diff_1[2] in diff_2:
                        same_diffs.append((pair_1, pair_2))
            if len(same_diffs) >= 66:
                overlap_scanners[(number_1, number_2)] = same_diffs
            searched_scanners.append([number_1, number_2])

    return overlap_scanners

def get_beacon_differences(scanners):
    for scanner in scanners.values():
        scanner['differences'] = {}
        beacons = scanner['beacons']
        for i in range(len(beacons)):
            for j in range(i+1, len(beacons), 1):
                difference = deque()
                for k in range(len(beacons[i])):
                    difference.append(abs(beacons[i][k] - beacons[j][k]))
                scanner['differences'][(i, j)] = difference
    
    return scanners

def handler():
    print(f'Start: {datetime.now()}')
    scanners = {}
    count = -1
    with open('input.txt') as input_file:
    # with open('test_input.txt') as input_file:
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
    
    scanners = get_beacon_differences(scanners)
    overlap_scanners = find_overlap_scanners(scanners)
    matching_beacons = find_matching_beacons(overlap_scanners)
    scanners, scanner_positions = find_scanner_positions(scanners, overlap_scanners, matching_beacons)
    answer_1 = count_beacons(scanners)
    answer_2 = get_max_distance(scanner_positions)
    
    print(f'The part 1 answer is {answer_1}')
    print(f'The part 2 answer is {answer_2}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
