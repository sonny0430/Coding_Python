def solution(a, b):
    data_c = int(str(a)+str(b))
    data_d = 2 * a * b

    return (data_c if data_c >= data_d else data_d)