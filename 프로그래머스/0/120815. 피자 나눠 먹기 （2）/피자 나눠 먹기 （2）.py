def solution(n):
    a = n
    for i in range(2, max(n, 6)+1):
        if (a % 6 == 0):
            break
        else:
            a = n * i
    return a // 6

    # 최소공배수
