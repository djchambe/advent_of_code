from collections import deque

def apply_insertions(polymer, instructions):
    ending_polymer = []
    chain = deque(maxlen=2)
    for character in polymer:
        chain.append(character)
        if len(chain) == 2:
            ending_polymer.append(instructions[''.join(chain)])
        ending_polymer.append(character)
    return ending_polymer

def handler():
    polymer = []
    insertions = {}
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            if not clean_line:
                continue            
            elif not polymer:
                polymer = list(clean_line)
            else:
                insertion_list = clean_line.split(' -> ')
                insertions[insertion_list[0]] = insertion_list[1]
    
    for _ in range(10):
        polymer = apply_insertions(polymer, insertions)
    
    counts = []
    for character in list(set(polymer)):
        counts.append(polymer.count(character))

    answer = max(counts) - min(counts)
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()