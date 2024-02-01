def solution(hp):
    result = 0
    temp_hp = hp
    for i in range(hp):
        if temp_hp >= 5:
            result += temp_hp // 5
            temp_hp = temp_hp % 5
        elif temp_hp >= 3:
            result += temp_hp // 3
            temp_hp = temp_hp % 3
        elif temp_hp >= 1:
            result += temp_hp // 1
            temp_hp = temp_hp % 1
        else:
            break
    return result

# if문 안써도 되는 문제.. 다시 풀어볼 것