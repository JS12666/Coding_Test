input = 20

def find_prime_list_under_number(number):
    prime_list = []

    for i in range(2, number + 1):
        for j in prime_list:
            if i % j == 0:
                break # 1이 아닌 수로 나뉘어지는 수가 있을 경우
        else: # for문에서 break가 없이 끝나면 호출
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)