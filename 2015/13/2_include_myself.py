from time import perf_counter
from itertools import permutations
from math import inf

def find_optimal_seating(preferences, people):
    happiness = -inf
    for arrangement in permutations(people):
        arrangement_happiness = 0
        for index, person in enumerate(arrangement):
            next_person_index = (index+1) % len(arrangement)
            arrangement_happiness += preferences.get(person, {}).get(arrangement[next_person_index], 0)
            arrangement_happiness += preferences.get(arrangement[next_person_index], {}).get(person, 0)
        if arrangement_happiness > happiness:
            happiness = arrangement_happiness
            best_arrangement = arrangement
    
    return happiness, best_arrangement

def handler():
    start_time = perf_counter()
    preferences = {}
    people = set()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip().rstrip('.')
            list_line = clean_line.split(' ')
            person_1 = list_line[0]
            impact = list_line[2]
            happiness = int(list_line[3])
            person_2 = list_line[-1]
            if impact == 'lose':
                happiness *= -1
            people.add(person_1)
            people.add(person_2)
            if preferences.get(person_1, ''):
                preferences[person_1][person_2] = happiness
            else:
                preferences[person_1] = {person_2: happiness}

    people.add('Host')
    answer = find_optimal_seating(preferences, people)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
