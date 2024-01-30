def solution(slice, n):
    temp_data = slice

    for i in range(1, n+1):
        if temp_data >= n:
            return i
        else: 
            temp_data = slice * (i+1)   