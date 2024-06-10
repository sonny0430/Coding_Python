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

