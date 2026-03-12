def solution(lottos, win_nums):
    lottos_temp = lottos.copy()

    for num in lottos:
        if (num in win_nums) == True:
            lottos_temp.remove(num)
            print(lottos_temp)
    
    lottos_temp.count(0)
    best = 1 + len(lottos_temp) - lottos_temp.count(0)
    worst = 1 + len(lottos_temp)
    best = 6 if best==7 else best
    worst = 6 if worst==7 else worst
    answer = [best, worst]
    return answer
