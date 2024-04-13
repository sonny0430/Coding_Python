def solution(id_pw, db):
    result = []

    for i, j in db:
        if i == id_pw[0] and j == id_pw[1]:
            return 'login'
        elif i == id_pw[0]:
            result.append(1)
        else:
            result.append(0)
    
    if 1 in result:
        return 'wrong pw'
    else:
        return 'fail'