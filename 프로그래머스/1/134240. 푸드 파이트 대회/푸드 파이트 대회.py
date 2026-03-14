def solution(food):
    front = ''
    back = ''

    for idx in range(0, len(food)-1):
        front = front + (f'{idx+1}')*(food[idx+1]//2)
        back = (f'{idx+1}')*(food[idx+1]//2) + back
    
    answer = front + '0' + back
    return answer