def solution(num_list):
    temp_list = list(map(lambda x: x % 2 == 0, num_list))
    return [sum(temp_list), len(temp_list)-sum(temp_list)]