def solution(arr, flag):
    result = []
    for i in range(len(arr)):
        if flag[i] == True:
            temp = []
            temp.append(arr[i])
            temp *= arr[i] * 2
            result.extend(temp)
        else:
            result = result[:len(result)-arr[i]]
            print(result)
    return result