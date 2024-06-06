def solution(data):
    return sum(list(filter(lambda x: x % 2 == 1, data)))
