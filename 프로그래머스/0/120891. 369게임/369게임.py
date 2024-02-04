def solution(order):
    data = list(str(order))
    return (data.count('3')+data.count('6')+data.count('9'))