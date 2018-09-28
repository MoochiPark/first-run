## 03-03 for문

### for문의 기본 구조
```python
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
```

#### 예제를 이용해 for문 이해하기
for문은 예제를 통해서 살펴보는 것이 가장 알기 쉽다. 다음 예제를 직접 입력해 보자.

__1.전형적인 for문__
```python
>>> test_list = ['one', 'two', 'three'] 
>>> for i in test_list: 
...     print(i)
... 
one 
two 
three
```
__2. 다양한 for문의 사용__
```python
>>> a = [(1,2), (3,4), (5,6)]
>>> for (first, last) in a:
...     print(first + last)
...
3
7
11
```
위의 예는 a 리스트의 요소값이 튜플이기 때문에 각각의 요소들이 자동으로 (first, last)라는 변수에 대입된다.

>※ 이 예는 02장에서 살펴보았던 튜플을 이용한 변수값 대입 방법과 매우 비슷한 경우이다. >>> (first, last) = (1, 2)

### for와 함께 자주 사용하는 range함수
for문은 숫자 리스트를 자동으로 만들어 주는 range라는 함수와 함께 사용되는 경우가 많다.
다음은 range 함수의 간단한 사용법이다.
```python
>>> a = range(10)
>>> a
range(0, 10)
```
range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.

시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데, 이때 끝 숫자는 포함되지 않는다.
```python
>>> a = range(1, 11)
>>> a
range(1, 11)
```
#### range 함수의 예시 살펴보기

for와 range 함수를 이용하면 1부터 10까지 더하는 것을 다음과 같이 쉽게 구현할 수 있다.
```python
>>> sum = 0 
>>> for i in range(1, 11): 
...     sum = sum + i 
... 
>>> print(sum)
55
```

#### for와 range를 이용한 구구단

for와 range 함수를 이용하면 소스 코드 단 4줄만으로 구구단을 출력할 수 있다. 들여쓰기에 주의하며 입력해 보자.
```python
>>> for i in range(2, 10):
...     for j in range(1, 10):
...         print(i*j, end=" ")
...     print('')
...
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81
```
위의 예를 보면 for문이 두 번 사용되었다.
1번 for문에서 2부터 9까지의 숫자(range(2,10))가 차례로 i에 대입된다. i가 처음 2일 때 2번 for문을 만나게 된다. 2번 for문에서 1부터 9까지의 숫자(range(1,10))가 j에 대입되고 그 다음 문장인 `print(i*j)`를 수행한다.

따라서 i가 2일 때 `2*1, 2*2, 2*3, ...2*9`까지 차례로 수행되며 그 값을 출력하게 된다. 그 다음으로 i가 3일 때 역시 2일 때와 마찬가지로 수행될 것이고 i가 9일 때까지 계속 반복된다.

> __[입력 인수 end를 넣어 준 이유는 무엇일까?]__
> 
> 앞의 예제에서 `print(i*j, end=" ")`와 같이 입력 인수 end를 넣어 준 이유는 해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서이다. 그 다음에 이어지는 print('')는 2단, 3단 등을 구분하기 위해 두 번째 for문이 끝나면 결과값을 다음 줄부터 출력하게 해주는 문장이다.

### 리스트 안에 for문 포함하기
리스트 안에 for문을 포함하는 리스트 내포(List comprehension)를 이용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다. 다음의 예제를 보자.
```python
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)
[3, 6, 9, 12]
```
위 예제는 a라는 리스트의 각 항목에 3을 곱한 결과를 result라는 리스트에 담는 예제이다.

이것을 리스트 내포를 이용하면 아래와 같이 간단히 해결할 수 있다.
```python
result = [num * 3 for num in a]
print(result)
[3, 6, 9, 12]
```

만약 짝수에만 3을 곱하여 담고 싶다면 다음과 같이 "if 조건"을 사용할 수 있다.
```python
result = [num * 3 for num in a if num % 2 == 0]
print(result)
[6, 12]
```
리스트 내포의 일반적인 문법은 다음과 같다. "if 조건" 부분은 앞의 예제에서 볼 수 있듯이 생할할 수 있다.
```python
[표현식 for 항목 in 반복가능객체 if 조건]
```

조금 복잡하지만 for문을 2개 이상 사용하는 것도 가능하다. for문을 여러 개 사용할 때의 문법은 다음과 같다.
```python
[표현식 for 항목1 in 반복가능객체1 if 조건1
        for 항목2 in 반복가능객체2 if 조건2
        ...
        for 항목n in 반복가능객체n if 조건n]
```
만약 구구단의 모든 결과를 리스트에 담고 싶다면 리스트 내포를 이용하여 아래와 같이 간단하게 구현할 수도 있다.
```python
result = [x*y for x in range(2, 10)
              for y in range(1, 10)]

print(result)

[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16,
20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42
, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81]
```
---
### 연습문제

_(연습문제 풀이 : https://wikidocs.net/17090#03-3-for)_


__[문제1] 1부터 100까지 출력__

1부터 100까지의 숫자를 for문을 이용하여 출력하시오.

>[풀이1]
```python
for n in range(1,101):
    print(n)
```

__[문제2] 5의 배수의 총합__

for문을 이용하여 1부터 1000까지의 자연수 중 5의 배수에 해당되는 자연수들의 총합을 구하시오.

>[풀이2]
```python
sum = 0
for n in range(1, 1001):
    if n % 5 == 0:
        sum += n

print(sum)
```

__[문제3] 학급의 평균 점수__

for문을 이용하여 A 학급의 평균 점수를 구해 보자.

>[풀이3]
```python
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for n in A:
    sum += n

avg = sum/len(A)
print(avg)
```

__[문제4] 혈액형__

다음은 학생들의 혈액형에 대한 데이터이다.
`['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']`

for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.

>[풀이4]
```python
b = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
Acnt = 0
Bcnt = 0
ABcnt = 0
Ocnt = 0
for n in b:
    if n == "A":
        Acnt += 1
    elif n == "B":
        Bcnt += 1
    elif n == "AB":
        ABcnt += 1
    else:
        Ocnt += 1

print(Acnt, Bcnt, ABcnt, Ocnt)
```


__[문제5] 리스트 내포1__

리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다.
```python
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
```
위 코드를 리스트 내포를 이용하여 표현하시오.


>[풀이5]
```python
numbers = [1, 2, 3, 4, 5]

result = [n*2 for n in numbers if n % 2 ==1]

print(result)
```

__[문제6] 리스트 내포2__

리스트 내포를 이용하여 다음 문장에서 모음('aeiou')를 제거하시오.

```
Life is too short, you need python
```

>[풀이6]

```python
s = "Life is too short, you need python"
v = "aeiou"
result = [n for n in s if n not in v]
r = "".join(result)
print(r)
```


---

## 출처
 - *Jump to python* *[https://wikidocs.net/22]*