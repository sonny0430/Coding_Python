def solution(my_string, letter):
    answer = list(filter(lambda x: x != letter, my_string))
    return ''.join(answer)