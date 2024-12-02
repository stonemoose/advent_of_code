num_list = [int(n) for n in open("input").readlines()]
for i in range(0, len(num_list) - 1):
    for j in range(i + 1, len(num_list)):
        if num_list[i] + num_list[j] == 2020:
            print(num_list[i] * num_list[j])
        # b
        for k in range(j + 1, len(num_list)):
            if num_list[i] + num_list[j] + num_list[k] == 2020:
                print(num_list[i] * num_list[j] * num_list[k])
