def solution(angle):
    if 90 > angle and angle > 0:
        return 1
    elif angle == 90:
        return 2
    elif 180 > angle and angle > 90:
        return 3
    elif angle == 180:
        return 4
    else :
        return
  
# def solution(angle):
#     answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
#     return answer