def solution(n_str):
    result = []
    for s in n_str:
        result.append(s)

    for s in n_str:
        if s == '0':
            result.pop(0)
        else:
            break

    return ''.join(result)