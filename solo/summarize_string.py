# 1. 입력으로 소문자의 '알파벳 순'으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.
#
# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.

def summarize_string(input_str):
    count = 0
    result_str = ''

    for i in range(len(input_str) - 1) :
        if input_str[i] == input_str[i+1]:
            count += 1
        elif input_str[i] != input_str[i+1]:
            result_str += input_str[i] + str(count+1) + "/"
            count = 0

    #마지막 연속되는 문자
    result_str += input_str[i-1] + str(count+1)

    return result_str

input_str = "acccdeee"

print(summarize_string(input_str))