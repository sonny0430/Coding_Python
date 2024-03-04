def solution(arr, idx):
    for i in range(idx,len(arr)):
        print(i)
        if arr[i] == 1:
            return i        
    return -1