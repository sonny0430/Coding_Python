def solution(keyinput, board):
    result = [0, 0]
    for i in keyinput:
        if i == 'left' and result[0] != (board[0] // 2) * (-1):
            result[0] -= 1
        elif i == 'right' and result[0] != (board[0] // 2):
            result[0] += 1
        elif i == 'up' and result[1] != (board[1] // 2):
            result[1] += 1
        elif i == 'down' and result[1] != (board[1] // 2) * (-1):
            result[1] -= 1
    
    return result
