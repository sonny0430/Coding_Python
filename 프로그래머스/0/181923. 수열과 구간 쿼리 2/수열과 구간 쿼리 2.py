def solution(arr, queries):
    result = []
    for i in range(len(queries)):
        temp1 = arr[queries[i][0]:queries[i][1]+1]
        temp2 = (list(filter(lambda x: x > queries[i][2], temp1)))

        if temp2 == []:
            result.append(-1)
        else:
            result.append(min(temp2))

    return result