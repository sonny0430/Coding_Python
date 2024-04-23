def solution(num, total):
    tmp = list(range(-100, 500))

    for i in range(len(tmp)):
        if sum(tmp[i:(i+num)]) == total:
            return tmp[i:(i+num)]