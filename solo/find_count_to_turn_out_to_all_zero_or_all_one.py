input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_all_to_zero = 0
    count_all_to_one = 0

    if string[0] == '0':
        count_all_to_one += 1
    elif string[0] == '1' :
        count_all_to_zero += 1

    for index in range(len(string) - 1):
        if string[index] != string[index+1]:
            if string[index] == '0':
                count_all_to_one += 1
            elif string[index] == '1':
                count_all_to_zero += 1

    return min(count_all_to_zero, count_all_to_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)