def solution(a, b):
    str_ab = str(a) + str(b)
    str_ba = str(b) + str(a)
    if int(str_ab) >= int(str_ba):
        return int(str_ab)
    else:
        return int(str_ba)