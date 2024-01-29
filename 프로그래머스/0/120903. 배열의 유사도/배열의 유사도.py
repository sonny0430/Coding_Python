def solution(s1, s2):
    return len(s1 + s2) - len(set(s1 + s2))


# def solution(s1, s2):
#     count = 0
#     for i in range(len(s2)):
#         if s2[i] in s1:
#             count += 1
#     return count