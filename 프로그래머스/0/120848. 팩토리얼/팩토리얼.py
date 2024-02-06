def solution(n):
    temp_data = 1
    for i in range(1, 12):
        if (temp_data * i) <= n:
            temp_data *= i
        else:
            return i-1