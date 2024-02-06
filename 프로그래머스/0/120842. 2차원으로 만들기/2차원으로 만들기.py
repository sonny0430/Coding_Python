def solution(num_list, n):
    two_dim = []
    one_dim = []
    for i in range(0,len(num_list)):
        if (i+1) % n == 0:
            one_dim.append(num_list[i])
            two_dim.append(one_dim)
            one_dim = []
        else:
            one_dim.append(num_list[i])
    return two_dim