def solution(s, n):
    result = ''
    temp = s
    for j in temp:
        temp2 = 0
        if j.isalpha():
            if ((ord(j)+n)> 122) or ((ord(j) <= 90)and (ord(j)+n) > 90):
                temp2 = ord(j) + n - 26
                result += chr(temp2)
            else:
                temp2 = ord(j) + n
                result += chr(temp2)
        else:
            result += j
    return result