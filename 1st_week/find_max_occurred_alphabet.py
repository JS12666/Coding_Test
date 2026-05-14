def find_max_occurred_alphabet(string):
    array = [0] * 26 # 알파벳 개수 만큼 배열 선언 / 빈도수 만큼 업데이트
    for char in string :
        if not char.isalpha():
            continue
        array[(ord(char) - ord('a'))] += 1

    max = 0
    max_index = 0

    for index in range(len(array)):
        alphabet_occurrence = array[index]

        if alphabet_occurrence > max :
            max = alphabet_occurrence
            max_index = index


    return chr(max_index + ord('a')) # 'a' = 97 (ASCII 값)
result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

