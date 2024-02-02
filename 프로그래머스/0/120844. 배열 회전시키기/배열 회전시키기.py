def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers.pop())
    else:
        numbers.insert(len(numbers)-1, numbers.pop(0))
    return numbers