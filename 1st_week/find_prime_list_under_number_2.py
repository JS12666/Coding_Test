input = 20
#소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1): # 2~n
        for i in prime_list: #소수로만 비교
            # N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list
result = find_prime_list_under_number(input)
print(result)

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
#[2, 3, 5, 7, 11, 13, 17, 19]
#[2, 3, 5, 7, 11, 13, 17, 19]