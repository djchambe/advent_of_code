from time import perf_counter

def find_best_cookie(ingredients):
    best_score = 0
    i_cap = ingredients[0][0]
    i_dur = ingredients[0][1]
    i_fla = ingredients[0][2]
    i_tex = ingredients[0][3]
    i_cal = ingredients[0][4]
    j_cap = ingredients[1][0]
    j_dur = ingredients[1][1]
    j_fla = ingredients[1][2]
    j_tex = ingredients[1][3]
    j_cal = ingredients[1][4]
    k_cap = ingredients[2][0]
    k_dur = ingredients[2][1]
    k_fla = ingredients[2][2]
    k_tex = ingredients[2][3]
    k_cal = ingredients[2][4]
    l_cap = ingredients[3][0]
    l_dur = ingredients[3][1]
    l_fla = ingredients[3][2]
    l_tex = ingredients[3][3]
    l_cal = ingredients[3][4]
    for i in range(101):
        for j in range(0, 101-i, 1):
            for k in range(0, 101-i-j, 1):
                cal = i_cal * i + j_cal * j + k_cal * k + l_cal * (100-i-j-k)
                if cal != 500:
                    continue
                cap = i_cap * i + j_cap * j + k_cap * k + l_cap * (100-i-j-k)
                dur = i_dur * i + j_dur * j + k_dur * k + l_dur * (100-i-j-k)
                fla = i_fla * i + j_fla * j + k_fla * k + l_fla * (100-i-j-k)
                tex = i_tex * i + j_tex * j + k_tex * k + l_tex * (100-i-j-k)
                if cap < 0 or dur < 0 or fla < 0 or tex < 0:
                    continue
                score = cap * dur * fla * tex
                if score > best_score:
                    best_score = score
                    best_cookie = [i, j, k, 100-i-j-k]
    
    return best_score, best_cookie

def handler():
    start_time = perf_counter()
    ingredients = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip().rstrip('.')
            list_line = clean_line.split(' ')
            capacity = int(list_line[2].rstrip(','))
            durability = int(list_line[4].rstrip(','))
            flavor = int(list_line[6].rstrip(','))
            texture = int(list_line[8].rstrip(','))
            calories = int(list_line[-1])
            ingredients.append([capacity, durability, flavor, texture, calories])

    answer = find_best_cookie(ingredients)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
