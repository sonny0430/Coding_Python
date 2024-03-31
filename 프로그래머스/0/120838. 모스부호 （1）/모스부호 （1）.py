def solution(letter):
    dic = {".-" : 'a',
           "-..." : 'b',
           "-.-." : 'c',
           "-.." : 'd',
           "." : 'e',
           "..-." : 'f',
           "--." : "g",
           "...." : 'h',
           ".." : 'i',
           ".---" : 'j',
           "-.-" : 'k',
           ".-.." : 'l',
           "--" : 'm',
           "-." : 'n',
           "---" : 'o',
           ".--." : 'p',
           "--.-" : 'q',
           ".-." : 'r',
           "..." : 's',
           "-" : 't',
           "..-" : 'u',
           "...-" : 'v',
           ".--" : 'w',
           "-..-" : 'x',
           "-.--" : 'y',
           "--.." : 'z'}
    
    result = ''
    tmp = ''

    for i in range(len(letter)):
        if letter[i] == ' ':
            result += dic[tmp]
            tmp = ''
        elif i == len(letter) - 1:
            tmp += letter[i]
            result += dic[tmp]
        else:
            tmp += letter[i]

    return result