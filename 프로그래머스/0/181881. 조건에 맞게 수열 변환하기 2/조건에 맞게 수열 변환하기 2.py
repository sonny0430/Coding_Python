def solution(arr):
    result = []
    temp = arr
    temp2 = []

    def sol(temp):
        for i in range(len(temp)):
            if (temp[i] >= 50) and (temp[i] % 2 == 0):
                temp2.append(temp[i] // 2)
        
            elif (temp[i] < 50) and (temp[i] % 2 == 1):
                temp2.append(temp[i] * 2 + 1)
            else:
                temp2.append(temp[i])
        result.append(temp)

    for k in range(100):
        sol(temp)        
        
        if (len(result) >= 2) and (result[k] == result[k-1]):
            return k-1
        
        temp = temp2
        temp2 = []   