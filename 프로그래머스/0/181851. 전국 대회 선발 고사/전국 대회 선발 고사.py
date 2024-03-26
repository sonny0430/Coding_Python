def solution(rank, attendance):
    tmp = []

    for i in range(len(rank)):
        if attendance[i] == False:
            rank[i] = 0

    tmp = sorted(filter(lambda x: x != 0, rank))

    return (10000*rank.index(tmp[0]) + 100*rank.index(tmp[1]) + rank.index(tmp[2]))