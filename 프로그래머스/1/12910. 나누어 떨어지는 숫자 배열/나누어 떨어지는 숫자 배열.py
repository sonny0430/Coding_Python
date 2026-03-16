def solution(arr, divisor):
    answer = sorted(list(filter(lambda x: x%divisor == 0, arr)))
    answer = [-1] if len(answer) == 0 else answer
    return answer