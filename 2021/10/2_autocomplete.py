from statistics import median

CHARACTER_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

EXPECTED_CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def handler():
    score_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            input_list = list(line.strip())
            openers = []
            corrupted = False
            for character in input_list:
                if character in EXPECTED_CLOSE:
                    openers.append(character)
                else:
                    try:
                        opener = openers.pop()
                    except:
                        corrupted = True
                        break                        
                    if character != EXPECTED_CLOSE[opener]:
                        corrupted = True
                        break
            if not corrupted and openers:
                score = 0
                while openers:
                    opener = openers.pop()
                    score *= 5
                    score += CHARACTER_POINTS[EXPECTED_CLOSE[opener]]
                score_list.append(score)
    
    answer = median(score_list)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()