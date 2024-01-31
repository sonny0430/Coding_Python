def solution(sides):
    sorted_list = sorted(sides, reverse = True)
    return (1 if sorted_list[1] + sorted_list[2] > sorted_list[0] else 2)
