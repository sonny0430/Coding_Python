def solution(my_string):
    temp_string = sorted(filter(lambda x: x.isdigit(), my_string))
    for i in range(0, len(temp_string)):
        temp_string[i] = int(temp_string[i])
    return temp_string

# 컴프리헨션과 map 함수 체크하기
# sorted([int(c) for c in my_string if c.isdigit()])
# sorted(map(int, filter(lambda s: s.isdigit(), my_string)))