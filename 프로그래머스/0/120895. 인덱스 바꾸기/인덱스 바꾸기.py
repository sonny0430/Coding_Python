def solution(my_string, num1, num2):
    result = ''
    idx = 0
    for i in my_string:
        if idx == num1:
            result += my_string[num2]
        elif idx == num2:
            result += my_string[num1]
        else:
            result += i
        idx += 1
    return result