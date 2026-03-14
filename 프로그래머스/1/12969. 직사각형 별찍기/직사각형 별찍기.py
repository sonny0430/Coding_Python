a, b = map(int, input().strip().split(' '))
answer = '*' * a
for i in range(b-1):
    
    answer = answer + "\n" + '*' * a

print(answer)