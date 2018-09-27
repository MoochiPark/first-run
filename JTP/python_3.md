# python  03장 제어문


## 목차
1. if문
2. while문
3. for문


## 03-1. if 문

### 기본구조
```python
money = 1
if money:
    print("Taxi")
else:
    print(`"Work")
```
 __if 조건문__ 에서 "조건문"이란 참과 거짓을 판단하는 문장을 말한다. 자료형의 참과 거짓에 대해서 몇 가지만 다시 살펴보면 다음과 같은 것들이 있다.
|자료형|참|거짓|
|-----|--|----|
|숫자|0이 아닌 숫자|0|
|문자열|"abc"|""|
|리스트|[1,2,3]|[]|
|튜플|(1,2,3)|()|
|딕셔너리|{"a":"b"}|{}|

### 비교연산자

조건이 참인지 거짓인지 판단할 때 자료형보다는 비교연산자(`<`,`>`,`==`,`!=`,`>=`,`<=`)를 쓰는 경우가 훨씬 많다.
|비교연산자|설명|
|-----|--|
|`x < y`|x가 y보다 작다|
|`x > y`|x가 y보다 크다|
|`x == y`|x와 y가 같다|
|`x >= y`|x가 y보다 크거나 같다|
|`x <= y`|x 가 y보다 작거나 같다|

### 예시
```python
>>> x = 3
>>> y = 2
>>> x > y
True
>>>
```

### and, or, not
|연산자|설명|
|-|-|
|x or y|x와 y 둘중에 하나만 참이면 참이다|
|x and y|x와 y 모두 참이어야 참이다|
|not x|x가 거짓이면 참이다|

### in, not in

|in|not in|
|-|-|
|x in list|x not in list|
|x in tuple|x not in tuple|
|x in string|x not in string|

> #### 예시
```python
>>> 1 in [1, 2, 3]
True
>>> 1 not in [1, 2, 3]
False
```
 > ### 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
 > ```python
 >pocket = ['paper', 'money', 'cellphone']
 >if 'money' in pocket:
 >      pass
 >else:
>       print("카드를 꺼내라")
>...
>```

### 조건부 표현식
```python
조건문이_참인_경우 if 조건문 else 조건문이_거짓인_경우
```

> #### 예시

```python
message = "success" if score >= 60 else "failure"
```
----
### 연습문제
*(연습문제 풀이 : https://wikidocs.net/17090#03-1-if)*

__[문제1] 조건문1__

홍길동씨는 5,000원의 돈을 가지고 있고 카드는 없다고 한다. 이러한 홍길동씨의 상태는 아래와 같이 표현할 수 있을 것이다.
```python
>>> money = 5000
>>> card = False
```
홍길동씨는 택시를 타고 목적지까지 가려고 한다. 목적지까지 가기 위해서는 카드를 소유하고 있거나 4,000원 이상의 현금을 가지고 있어야 한다고 한다. 홍길동씨는 택시를 탈 수 있는지를 판별할 수 있는 조건식을 작성하고 그 결과를 출력하시오.

> __[풀이1]__
```python
money = 5000
card = False
if money >= 4000 or card:
    print("택시를 타고가자")
else:
    print("걸어서 가자")
```
__[문제2] 조건문2__

홍길동씨의 행운권 번호는 23번 이라고 한다. 다음은 행운권 당첨번호 리스트이다.
```python
>>> lucky_list = [1, 9, 23, 46]
```
홍길동씨가 당첨되었다면 "야호"라는 문자열을 출력하는 프로그램을 작성하시오.
> __[풀이2]__
```python
lucky_list = [1, 9, 23, 46]

if 23 in lucky_list:
    print("야호")
```
__[문제3] 홀수 짝수 판별__

주어진 수가 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.
> __[풀이3]__
```python
n = int(input("정수 입력 >>> "))

if n % 2 == 0:
    print("짝수")
else:
    print("홀수")
```

__[문제4] 문자열 분석__

다음 문자열을 분석하여 나이가 30미만이고 키가 175이상인 경우에는 YES를 출력하고 아닌 경우에는 NO를 출력하는 프로그램을 작성하시오.

> __[풀이4]__
```python
s = "나이:30,키:180"
y = int(s[3:5])
t = int(s[8:11])

if y < 30 and t > 175:
    print("YES")
else:
    print("NO")
```
__[문제5] 조건문3__

다음 코드의 결과값은 무엇일까?
```python
>>> a = "Life is too short, you need python"
>>> if 'wife' in a:
...     print('wife')
... elif 'python' in a and 'you' not in a:
...     print('python')
... elif 'shirt' not in a:
...     print('shirt')
... elif 'need' in a:
...     print('need')
... else:
...     print('none')
```
> __[풀이5]__

`shirt`는 a에 포함되지 않기 때문에 `shirt`



---

## 출처
 - *Jump to python* *[https://wikidocs.net/20]*