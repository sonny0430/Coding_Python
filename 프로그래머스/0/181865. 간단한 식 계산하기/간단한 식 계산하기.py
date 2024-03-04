def solution(binomial):
    temp_data = binomial.split(' ')
    result = 0
    if temp_data[1] == '+':
        result = int(temp_data[0]) + int(temp_data[2])
    elif temp_data[1] == '-':
        result = int(temp_data[0]) - int(temp_data[2])
    elif temp_data[1] == '*':
        result = int(temp_data[0]) * int(temp_data[2])
    
    return result