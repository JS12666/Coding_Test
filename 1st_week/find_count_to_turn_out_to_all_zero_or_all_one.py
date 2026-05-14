input = "011110"

# 0에서 1을 마주쳤을 때 뒤집는다 -> 전체를 0으로 만들기 위한 작업
# 1에서 0을 마주쳤을 때 뒤집는다 -> 전체를 1으로 만들기 위한 작업

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_zero = 0 # 전체를 0으로 바꾸기
    count_one = 0  # 전체를 1로 바꾸기

    if string[0] == "0" :
        count_one += 1
    elif string[1] == "1" :
        count_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i+1] == "0":
                count_one += 1
            elif string[i+1] == '1' :
                count_zero += 1

    print(count_zero, count_one)

    return min(count_zero, count_one)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)