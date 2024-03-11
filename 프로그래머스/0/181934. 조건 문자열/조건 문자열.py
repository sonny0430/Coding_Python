def solution(ineq, eq, n, m):
    result = 0
    if ineq == '>' and eq == '=':
        result = n >= m
    elif ineq == '<' and eq == '=':
        result = n <= m
    elif ineq == '>' and eq == '!':
        result = n > m
    elif ineq == '<' and eq == '!':
        result = n < m
    
    if result == True:
        return 1
    else:
        return 0
    