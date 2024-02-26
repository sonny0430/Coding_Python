def solution(num_list, n):
    result = []
    for i in range(n):
        result.append(num_list[0])
        num_list.pop(0)
    return num_list+result