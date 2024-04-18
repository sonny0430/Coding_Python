def solution(chicken):
    tmp = chicken
    result = 0

    while tmp // 10 >= 1:
        result += tmp // 10
        tmp = tmp % 10 + tmp // 10
        
    return result