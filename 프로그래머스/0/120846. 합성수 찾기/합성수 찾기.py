def solution(n):
    temp_list = []
    count = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
            if count >= 3:
                temp_list.append(i)
                break
        count = 0

    return len(temp_list)
