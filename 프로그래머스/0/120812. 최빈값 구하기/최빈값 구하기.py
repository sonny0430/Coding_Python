def solution(array):
    no_duplication_array = list(set(array))
    count_list = []
    print(no_duplication_array)

    for i in range(0, len(no_duplication_array)):
        count_list.append(array.count(no_duplication_array[i]))
    
    if count_list.count(max(count_list)) == 1:
        return no_duplication_array[count_list.index(max(count_list))]
    else:
        return -1
    
# 딕셔너리 활용법, enumerate 활용법도 찾아보면 좋아보자