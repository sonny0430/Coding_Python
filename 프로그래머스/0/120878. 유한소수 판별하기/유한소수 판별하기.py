def solution(a, b):
    tmp = []
    result = []

    for i in range(2, b):
        if a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
            tmp.append(i)

    k = 2
    while b > 1:
        if b % k == 0:
            b = b // k
            result.append(k)
            k = 2           
        else:
            k += 1

    if list(filter(lambda x: x != 2 and x != 5, result)) == []:
        return 1
    else:
        return 2
