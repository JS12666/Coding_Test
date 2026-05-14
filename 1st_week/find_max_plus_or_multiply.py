def find_max_plus_or_multiply(array):
    num = 0

    # 0 혹은 1일때는 더하기
    for i in range(len(array)):
        if array[i] == 0:
            continue
        elif array[i] == 1:
            num += array[i]
        else :
            # 앞 숫자가 0이면 더하기
            if num == 0 :
                num += array[i]
            else :
                num *= array[i]

    return num
result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))


def find_max_plus_or_multiply(array):
    sum = 0
    for number in array:
        if number <= 1 or sum <= 1:
            sum += number
        else:
            sum *= number
    return sum