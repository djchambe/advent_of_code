from time import perf_counter

VOWELS = ['a', 'e', 'i', 'o', 'u']
BAD_PAIRS = ['ab', 'cd', 'pq', 'xy']

def handler():
    start_time = perf_counter()
    strings = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            strings.append(clean_line)

    answer = 0

    for string in strings:
        vowel_count = 0
        double_letter = False
        no_bad_pair = True
        for index, character in enumerate(string):
            if character in VOWELS:
                vowel_count += 1
            if index > 0:
                if character == string[index-1]:
                    double_letter = True
                if string[index-1:index+1] in BAD_PAIRS:
                    no_bad_pair = False
                    break
        if vowel_count > 2 and double_letter and no_bad_pair:
            answer += 1

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()