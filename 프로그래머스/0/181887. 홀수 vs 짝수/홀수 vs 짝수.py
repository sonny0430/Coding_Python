def solution(num_list):
    result_a = 0
    result_b = 0
    for i in range(len(num_list)):
        if i % 2 == 1:
            result_a += num_list[i]
        else:
            result_b += num_list[i]
    return (result_a if result_a >= result_b else result_b)