# 문제 1번

* 문제 레벨 : 0
* 문제 종류 : 요구사항 구현
* 문제 링크 : https://100.pyalgo.co.kr/?page=1
* 통과 여부 : Y

```python
def solution(data):
    return sum(list(filter(lambda x: x % 2 == 1, data)))    
```

# 문제 2번

* 문제 레벨 : 0
* 문제 종류 : 요구사항 구현
* 문제 링크 : https://100.pyalgo.co.kr/?page=2
* 통과 여부 : Y

```python
def solution(data):
    result = (0 if len(data) == 0 else 1)
    for i in data:
        result *= i       
    return result
```

# 문제 3번

* 문제 레벨 : 0
* 문제 종류 : 요구사항 구현
* 문제 링크 : https://100.pyalgo.co.kr/?page=3
* 통과 여부 : Y

```python
def solution(data):
    return sum(filter(lambda x: (x % 3 != 0) and (x % 5 != 0), data))
```

# 문제 4번

* 문제 레벨 : 0
* 문제 종류 : 요구사항 구현
* 문제 링크 : https://100.pyalgo.co.kr/?page=4
* 통과 여부 : Y

```python
def solution(data):
    result = 0
    for i, s in enumerate(data):
        result += int(s[-2]) * (i+1)
    return result        
```

# 문제 5번

* 문제 레벨 : 0
* 문제 종류 : 요구사항 구현
* 문제 링크 : https://100.pyalgo.co.kr/?page=5
* 통과 여부 : Y

```python
def solution(data):
    result = sum([str(i).count('1') for i in data])
    
    return (0 if len(data) == 0 else result)
```

# 문제 6번

* 문제 레벨 : 0
* 문제 종류 : 요구사항 구현
* 문제 링크 : https://100.pyalgo.co.kr/?page=6
* 통과 여부 : Y

```python
def solution(data):
    return sum([int(s) if s.isdigit() == True else 0 for s in data])
```

# 문제 7번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=7
* 통과 여부 : Y

```python
def solution(data):
    result = []
    temp = [data[i][1] for i in range(len(data))]    
    
    for j in sorted(temp):
        for k in range(len(data)):
            if j in data[k]:
                result.append(data[k][0])
    
    return result
```

# 문제 8번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=8
* 통과 여부 : Y

```python
def solution(data):
    result = []
    temp = 100

    for i in range(len(data)-1):
        if temp > (data[i+1] - data[i]):
            temp = (data[i+1] - data[i])
            result = [data[i], data[i+1]]

    return result
```

# 문제 9번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=9
* 통과 여부 : Y

```python
def solution(data):
    result = [i['수'] for i in data]
        
    return data[result.index(max(result))]['이름']    
```

# 문제 10번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=10
* 통과 여부 : Y

```python
def solution(data):        
    result = [i[0] for i in data if sum(i[1:])>=350]  
             
    return sorted(result)
```

# 문제 11번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=11
* 통과 여부 : Y

```python
def solution(data):
    result = [sum(i)//3 for i in data]
        
    return len(list(filter(lambda x: x >= 80, result)))
```

# 문제 12번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=12
* 통과 여부 : Y

```python
def solution(data):
    result = [0 for _ in range(len(data[0]))]
    
    split_data = [s.split(' ') for s in data[0]]
        
    sorted_dic = sorted(data[1].items(), key = lambda x: x[1])
    
    for s in split_data:
        for idx, k in enumerate(sorted_dic):
            if s[1] in k[0]:
                result[idx] = ' '.join(s)
    
    return result
```

# 문제 13번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=13
* 통과 여부 : Y

```python
def solution(data):
    temp = sorted(data[1].items(), key = lambda x: (x[1], x[0]))
    return [temp[i][0] for i in range(len(temp))]

```

# 문제 14번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=14
* 통과 여부 : Y

```python
def solution(data):
    temp = sorted(data.items(), key = lambda x: x[0])
    return [temp[i][1] for i in range(len(temp))]
```

# 문제 15번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=15
* 통과 여부 : Y

```python
def solution(data):
    result1 = []
    result2 = []

    for s in data:
        if s[:2] == '12' and 'AM' in s:
            result1.append('00'+s[2:])
        elif s[:2] == '12' and 'PM' in s:
            result1.append('00'+s[2:])
        else:
            result1.append(s)    
        
    sorted_time = sorted(result1, key = lambda x: ("AM" not in x, int(x[:2])))
    
    for s in sorted_time:
        if s[:2] == '00' and 'AM' in s:
            result2.append('12'+s[2:])
        elif s[:2] == '00' and 'PM' in s:
            result2.append('12'+s[2:])
        else:
            result2.append(s) 
    
    return result2
```

# 문제 16번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=16
* 통과 여부 : Y

```python
def solution(data):
    result = []
    for s in data:
        if '-' in s:
            result.append(s[-4:]+'/'+s[3:5]+'/'+s[:2])
        elif '/' in s:
            result.append(s[-4:]+'/'+s[:5])
        elif '.' in s:
            result.append(s.replace('.', '/'))
        else:
            None
        
    return sorted(result)
```

# 문제 17번

* 문제 레벨 : 0
* 문제 종류 : 정렬
* 문제 링크 : https://100.pyalgo.co.kr/?page=17
* 통과 여부 : Y

```python
def solution(data):
    result = []
    temp = []
    
    for l in data.values():
        temp.extend(l)
    temp = sorted(temp, reverse=True)[:3]
    
    for d in temp:
        for s in data.items():
            if d in s[1]:
                result.append(d[2:] + ' ' + s[0])
            
    return result
```

# 문제 18번

* 문제 레벨 : 0
* 문제 종류 : 분석
* 문제 링크 : https://100.pyalgo.co.kr/?page=18
* 통과 여부 : Y

```python
def solution(data):
    temp = sorted(data.items(), key = lambda x: (x[1]), reverse=True)[:3]
    result = []
    
    for s in temp:
        result.append(s[0][2:] + ': ' + str(s[1]))
      
    return result
```

# 문제 19번

* 문제 레벨 : 0
* 문제 종류 : 타입 확인
* 문제 링크 : https://100.pyalgo.co.kr/?page=19
* 통과 여부 : Y

```python
def solution(data):
    result = [str(type(l))[8:-2] for l in data]
    
    return result
```

# 문제 20번

* 문제 레벨 : 0
* 문제 종류 : 타입 확인
* 문제 링크 : https://100.pyalgo.co.kr/?page=20
* 통과 여부 : Y

```python
def solution(data):
    for s in data:
        if str(type(s[1]))[8:-2] != s[0]:
            return False
        
    return True
```

# 문제 21번

* 문제 레벨 : 0
* 문제 종류 : 탐색
* 문제 링크 : https://100.pyalgo.co.kr/?page=21
* 통과 여부 : Y

```python
def solution(data):
    return (data[0].index(data[1]) if data[1] in data[0] else False)

```

# 문제 22번

* 문제 레벨 : 0
* 문제 종류 : 탐색
* 문제 링크 : https://100.pyalgo.co.kr/?page=22
* 통과 여부 : Y

```python
def solution(data):
    return (data[0].index(data[1]) if data[1] in data[0] else False)

```

# 문제 23번

* 문제 레벨 : 0
* 문제 종류 : 탐색
* 문제 링크 : https://100.pyalgo.co.kr/?page=23
* 통과 여부 : Y

```python
def solution(data):
    for i in data[0]:
        if data[1] in i:
            return True
    return False
```

# 문제 26번

* 문제 레벨 : 0
* 문제 종류 : 탐색, 슬라이딩 윈도우
* 문제 링크 : https://100.pyalgo.co.kr/?page=26
* 통과 여부 : Y

```python
def solution(data):
    result = 0
    n = data[1]
    
    for i in range(len(data[0])-n):
        if sum(data[0][i:i+n]) > result:
            result = sum(data[0][i:i+n])

    return result
```

# 문제 27번

* 문제 레벨 : 1
* 문제 종류 : 탐색, 슬라이딩 윈도우
* 문제 링크 : https://100.pyalgo.co.kr/?page=27
* 통과 여부 : Y

```python
def solution(data):
    for win in range(2, len(data[0])):
      for i in range(0, len(data[0])-win):
        if sum(data[0][i:i+win+1]) > data[1]:
            return win
  
    return 0
```

# 문제 28번

* 문제 레벨 : 1
* 문제 종류 : 탐색, 투 포인터
* 문제 링크 : https://100.pyalgo.co.kr/?page=28
* 통과 여부 : Y

```python
def solution(data):
    result = []
    
    for i in range(len(data[0])-1):
        for j in range(i+1, len(data[0])):
            result.append(data[0][i] + data[0][j])
   
    return list(sorted(result, key = lambda x: abs(x - data[1])))[0]
```

# 문제 29번

* 문제 레벨 : 0
* 문제 종류 : 비트 조작
* 문제 링크 : https://100.pyalgo.co.kr/?page=29
* 통과 여부 : Y

```python
def solution(data):
    for i in data:
        if data.count(i) == 1:
            return i
```

# 문제 30번

* 문제 레벨 : 0
* 문제 종류 : 비트 조작
* 문제 링크 : https://100.pyalgo.co.kr/?page=30
* 통과 여부 : Y

```python
def solution(data):
    result = ''
    for s in bin(data)[2:]:
        if s == "1":
            result += "A"
        else:
            result += "B"     
    return result
```

# 문제 31번

* 문제 레벨 : 0
* 문제 종류 : 비트 조작
* 문제 링크 : https://100.pyalgo.co.kr/?page=31
* 통과 여부 : Y

```python
def solution(data):
    temp = bin(data)[2:]
    
    while len(temp) < 10:
        temp = '0' + temp
    
    temp = temp.replace('1', '2').replace('0', '1').replace('2', '0')
    
    temp = int(temp, 2)
    return temp
```

