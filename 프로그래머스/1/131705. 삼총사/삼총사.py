def solution(number):
    cases = []
    result = 0

    for i in range(0, len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                cases.append([number[i], number[j], number[k]])

    for c in cases:
        if sum(c) == 0:
            result += 1       
    
    return result