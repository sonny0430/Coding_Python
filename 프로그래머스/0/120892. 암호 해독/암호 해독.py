def solution(cipher, code):
    result = ''
    count = 1
    for i in cipher:
        if count % code == 0:
            result += i
        count += 1
    return result