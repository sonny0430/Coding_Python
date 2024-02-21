def solution(n, control):
    ctrl = {'w' : 1,
     'a' : -10,
     's' : -1,
     'd' : 10
     }
    
    for i in control:
        n += ctrl[i]
        print (i)
        
    return n