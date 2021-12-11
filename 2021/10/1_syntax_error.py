CHARACTER_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

EXPECTED_CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def handler():
    with open('input.txt') as input_file:
        answer = 0
        for line in input_file:
            input_list = list(line.strip())
            openers = []
            for character in input_list:
                if character in EXPECTED_CLOSE:
                    openers.append(character)
                else:
                    try:
                        opener = openers.pop()
                    except:
                        answer += CHARACTER_POINTS[character]
                        break                        
                    if character != EXPECTED_CLOSE[opener]:
                        answer += CHARACTER_POINTS[character]
                        break

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()