def solution(sides):
    result = []
    for i in range(1, 2000):
        if (min(sides) + i) > max(sides) and max(sides) >= i :
            result.append(i)
        elif ((sides[0] + sides[1]) > i) and i > max(sides):
            result.append(i)
        elif i > max(sides) * 2:
            break        

    return len(result)