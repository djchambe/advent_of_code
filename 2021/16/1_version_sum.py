def evaluate_operator(bin_string, versions):
    length_type = bin_string[0]
    if int(length_type):
        sub_packets = int(bin_string[1:12], 2)
        bin_string = bin_string[12:]
        for _ in range(sub_packets):
            bin_string, versions = evaluate_packet(bin_string, versions)
    else:
        bits = int(bin_string[1:16], 2)
        new_string = bin_string[16:16 + bits]
        while new_string and int(new_string, 2):
            new_string, versions = evaluate_packet(new_string, versions)
        bin_string = bin_string[16 + bits:]

    return bin_string, versions

def evaluate_literal(bin_string):
    continuation = 1
    value = ''
    while int(continuation):
        continuation = bin_string[0]
        value += bin_string[1:5]
        bin_string = bin_string[5:]

    return bin_string

def evaluate_packet(bin_string, versions):
    if not bin_string or not int(bin_string, 2):
        return bin_string, versions
    packet_version = bin_string[:3]
    versions.append(int(packet_version, 2))
    type_id = bin_string[3:6]
    if type_id == '100':
        bin_string = evaluate_literal(bin_string[6:])
    else:
        bin_string, versions = evaluate_operator(bin_string[6:], versions)

    return bin_string, versions

def handler():
    with open('input.txt') as input_file:
        for line in input_file:
            hex_string = line.strip()
    
    bin_string = bin(int(hex_string, 16))[2:].zfill(len(hex_string)*4)

    versions = []
    _, versions = evaluate_packet(bin_string, versions)
    answer = sum(versions)
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()