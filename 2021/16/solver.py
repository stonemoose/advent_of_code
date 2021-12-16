import math


def num_packet(r_line, num_packets):
    total_line_num = 0
    total_version = 0
    total_num = []
    for i in range(num_packets):
        v, num, line_num = read_packets(r_line[total_line_num:])
        total_version += v
        total_num.append(num)
        total_line_num += line_num
    return total_version, total_num, total_line_num + 18


def len_packet(r_line, total_len):
    total_line_num = 0
    total_version = 0
    total_num = []
    while total_line_num < total_len:
        v, num, line_num = read_packets(r_line[total_line_num:])
        total_version += v
        total_num.append(num)
        total_line_num += line_num
    return total_version, total_num, total_line_num + 22


def read_packets(r_line):
    version = int(r_line[:3], 2)
    type_id = int(r_line[3:6], 2)

    if type_id == 4:
        num = ''
        line_num = 6
        while line_num < len(r_line):
            num += r_line[line_num+1:line_num+5]
            if r_line[line_num] == '0':
                break
            line_num += 5
        return version, int(num, 2), line_num+5

    else:
        op_type = int(r_line[6], 2)
        if op_type == 0:
            total_len = int(r_line[7:22], 2)
            vers, num, l_num = len_packet(r_line[22:], total_len)

        elif op_type == 1:
            num_packets = int(r_line[7:18], 2)
            vers, num, l_num = num_packet(r_line[18:], num_packets)

        if type_id == 0:
            num = sum(num)
        elif type_id == 1:
            num = math.prod(num)
        elif type_id == 2:
            num = min(num)
        elif type_id == 3:
            num = max(num)
        elif type_id == 5:
            num = int(num[0] > num[1])
        elif type_id == 6:
            num = int(num[0] < num[1])
        elif type_id == 7:
            num = int(num[0] == num[1])
        return vers + version, num, l_num


if __name__ == '__main__':
    with open('input') as f:
        line = f.read().strip()
        new_line = bin(int(line, 16))[2:].zfill(len(line)*4)

    version, number, _ = read_packets(new_line)
    print(f'Part 1: {version}')
    print(f'Part 2: {number}')
