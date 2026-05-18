
# ( ( ( ) ) )
# ( ( ( ) ( ( ) ) ) )
# stack.append(" ( ")
# stack.pop() == (" ) ")


def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []
    is_correct = True
    for parenthesis in string:
        if parenthesis == "(" :
            stack.append(parenthesis)
        elif parenthesis == ")" :
            if not stack:
                is_correct = False
                break
            stack.pop()

    if stack :
        is_correct = False

    return is_correct


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))