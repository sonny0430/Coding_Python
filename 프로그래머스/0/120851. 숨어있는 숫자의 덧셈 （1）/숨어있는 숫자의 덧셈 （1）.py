def solution(my_string):
    temp_data = list(filter(lambda x: x.isdigit(), my_string))
    for i in range(len(temp_data)):
        temp_data[i] = int(temp_data[i])
    return sum(temp_data)    
