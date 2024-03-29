def solution(numbers, k):
    result = 0
    for i in range(1, k):
        result += 2
        
        if result == len(numbers):
            result = 0
        elif result == (len(numbers) + 1):
            result = 1
        else:
            pass

    return numbers[result]