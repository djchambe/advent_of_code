from time import perf_counter

def handler():
    start_time = perf_counter()
    strings = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            strings.append(clean_line)

    answer = 0

    for string in strings:
        repeat_pair = False
        repeat_letter = False
        letter_pairs = []
        for index, character in enumerate(string):
            if index > 0:
                letter_pair = string[index-1:index+1]
                if letter_pair in letter_pairs:
                    if letter_pair != letter_pairs[-1]:
                        repeat_pair = True
                    elif letter_pairs.count(letter_pair) > 1:
                        repeat_pair = True
                letter_pairs.append(letter_pair)
            if index > 1:
                if character == string[index-2]:
                    repeat_letter = True
        if repeat_pair and repeat_letter:
            answer += 1

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()