str = input()
result = []
for s in str:
    if ord(s) >= 65 and ord(s) < 97:
        result.append(s.lower())
    else:
        result.append(s.upper())
print(''.join(result))