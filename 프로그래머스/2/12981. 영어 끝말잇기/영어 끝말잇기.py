def solution(n, word):
    result = []
    word_list = [word[0]]
            
    for i in range(1, len(word)):
        if word[i] in word_list or word[i-1][-1] != word[i][0]:
            result.append(i % n + 1)
            result.append(i // n + 1)
            
            return result
        
        else:
            word_list.append(word[i])

    return [0, 0]