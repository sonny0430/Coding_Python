def solution(board):
    result = len(board)**2
    tmp = []
    tmp2 = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                tmp.append([i, j])

    for i, j in tmp:
        tmp2 = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1],
        [i+1, j-1], [i+1, j], [i+1, j+1]] 

        for k in range(len(tmp2)):
            if tmp2[k][0] in [-1, len(board)] or tmp2[k][1] in [-1, len(board)]:
                pass
            else:
                board[tmp2[k][0]][tmp2[k][1]] = 1
        
    for i in range(len(board)):
        result -= sum(board[i])


    return result