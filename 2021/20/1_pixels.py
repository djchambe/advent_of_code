def count_lit_pixels(image):
    count = 0
    for row in image:
        count += sum(row)
    
    return count

def get_bottom_row(image, enhancement, fill_bit):
    bottom_row = []
    total_rows = len(image)
    for j in range(len(image[0]) + 2):
        bottom_row.append(enhancement[get_lookup(total_rows, j-1, image, fill_bit)])
    return bottom_row

def get_top_row(image, enhancement, fill_bit):
    top_row = []
    for j in range(len(image[0]) + 2):
        top_row.append(enhancement[get_lookup(-1, j-1, image, fill_bit)])
    return top_row

def add_borders(output, image, enhancement, fill_bit):
    top_row = get_top_row(image, enhancement, fill_bit)
    bottom_row = get_bottom_row(image, enhancement, fill_bit)
    total_columns = len(image[0])
    for index in range(len(image)):
        first_entry = enhancement[get_lookup(index, -1, image, fill_bit)]
        last_entry = enhancement[get_lookup(index, total_columns, image, fill_bit)]
        output[index].insert(0, first_entry)
        output[index].append(last_entry)
    output.insert(0, top_row)
    output.append(bottom_row)
    
    return output

def get_lookup(i, j, image, fill_bit):
    binary_lookup = []
    columns = len(image[0])
    rows = len(image)
    for y in range(i-1, i+2, 1):
        for x in range(j-1, j+2, 1):
            if x < 0 or x >= columns or y < 0 or y >= rows:
                binary_lookup.append(fill_bit)
            else:
                binary_lookup.append(str(image[y][x]))
    return int(''.join(binary_lookup), 2)

def enhance_image_range(image, enhancement, fill_bit):
    output = []
    for i in range(len(image)):
        output.append([])
        for j in range(len(image[0])):
            output[i].append(enhancement[get_lookup(i, j, image, fill_bit)])
    
    return output

def apply_enhancement(image, enhancement, fill_bit):
    output_image = enhance_image_range(image, enhancement, fill_bit)
    return add_borders(output_image, image, enhancement, fill_bit)

def handler():
    enhancement = []
    input_image = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            if not enhancement:
                enhancement = [0 if x == '.' else 1 for x in clean_line]
            elif clean_line:
                input_image.append([0 if x == '.' else 1 for x in clean_line])

    for count in range(2):
        if count:
            fill_bit = '1'
        else:
            fill_bit = '0'
        input_image = apply_enhancement(input_image, enhancement, fill_bit)

    answer = count_lit_pixels(input_image)
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()
