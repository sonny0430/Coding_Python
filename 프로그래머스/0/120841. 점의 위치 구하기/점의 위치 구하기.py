def solution(dot):
    temp_list = list(map(lambda x: x > 0, dot))
    if temp_list == [True, True]:
        return 1
    elif temp_list == [False, True]:
        return 2
    elif temp_list == [False, False]:
        return 3
    else:
        return 4