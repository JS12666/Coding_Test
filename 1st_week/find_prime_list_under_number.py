input = 20
#소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
def find_prime_list_under_number(number):
    # 입력값보다 작은 값들 중에서 소수 찾기
    # 1~20이 있는데 반복문을 이용해서 곱한 값들 다 array에 추가하고, 거기서 빈도수 0인값이 소수
    array = [0] * (number + 1)

    # 0과 1은 소수가 아니니까 미리 1로 표시해서 제외하기
    array[0] = array[1] = 1

    # 2부터 시작하는 두 수를 곱해서 나오는 모든 수는 '소수가 아님'
    for i in range(2, number+ 1) :
        for j in range(2, number + 1):
            print(i, j, i*j)
            if i * j <= number:
                array[i * j] = 1  # 곱해서 만들 수 있으니 소수 탈락!
            else:
                break  # 곱이 number를 넘어가면 더 볼 필요 없음

    result = []
    for i in range(2, number + 1):
        if array[i] == 0:
            result.append(i)

    return result
result = find_prime_list_under_number(input)
print(result)

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
#[2, 3, 5, 7, 11, 13, 17, 19]
#[2, 3, 5, 7, 11, 13, 17, 19]