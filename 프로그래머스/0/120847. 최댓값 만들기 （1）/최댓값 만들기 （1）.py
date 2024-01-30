def solution(numbers):
    sort_numbers = sorted(numbers, reverse = True)
    return sort_numbers[0] * sort_numbers[1]