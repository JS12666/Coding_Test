input = "abadabac"

def find_not_repeating_first_character(string):
    #반복횟수 먼저찾기
    array = [0] * 26

    for char in string:
        array[ord(char) - ord('a')] += 1

    #반복횟수가 1인 값 중 가장 먼저 나타나는 것 찾기
    alpha_array = []
    for index in range(len(array)):
        if array[index] == 1:
            alpha_array.append(chr(index + ord('a')))

    for s in string:
        if s in alpha_array:
            return s

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))