## 04-1 함수

### 파이썬 함수의 구조
파이썬 함수의 구조는 다음과 같다
```python
def 함수명(매개변수):
    수행할 문장1
    수행할 문장2
    ...
```
def는 함수를 만들 때 사용하는 예약어이며, 함수명은 함수를 만드는 사람이 임의로 만들 수 있다. 함수명 뒤 괄호 안의 매개변수는 이 함수에 입려긍로 전달되는 값을 받는 변수이다. 이렇게 함수를 정의한 다음 if, while, for문 등과 마찬가지로 함수에서 수행할 문장들을 입력한다.

간단하지만 많은 것을 설명해 주는 다음의 예를 보자.
```python
def sum(a, b):
    return a + b
```

>"이 함수의 이름은 sum이고 입력으로 2개의 값을 받으며 결과값은 2개의 입력값을 더한 값이다"

이제 직접 sum 함수를 사용해 보자.
```python
a = 3
b = 4
c = sum(a, b)
print(c)
7
```

#### 매개변수와 인수

매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 헷갈리는 용어이므로 잘 기억해 두기로 하자. 매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.
```python
def sum(a, b):  #a, b는 매개변수
    return a+b

print(sum(3, 4))    #3, 4는 인수
```

#### 일반적인 함수
입력값이 있고 결과값이 있는 함수가 일반적인 함수이다.
```python
def 함수이름(매개변수):
    <수행할 문장1>
    ...
    return 결과값
```
다음은 일반적인 함수의 전형적인 예이다.
```python
def sum(a, b):
    result = a + b
    return result
```

#### 입력값이 없는 함수
```python
def say():
    return 'Hi'
```

```python
a = say()
print(a)
Hi
```
>결과값을 받을 변수 = 함수명()

#### 결과값이 없는 함수
```python
def sum(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
```
#### 입력값도 결과값도 없는 함수
```python
def say():
    print('Hi')
```

#### 매개변수 지정하여 호출하기

앞서 알아보았던 sum함수이다. 이 함수를 우리는 다음과 같이 매개변수를 지정하여 사용할 수 있다.
```python
>>> sum(a=3, b=7) # a에 3, b에 7을 전달
10
```
매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.
```python
>>> sum(b=5, a=3) # a에 3, b에 5를 전달
8
```

### 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
입력값이 여러 개일 때 그 입력값들을 모두 더해 주는 함수를 생각해 보자. 하지만 몇 개가 입력될지 모를 떄는 어떻게 해야 할까? 아마도 난감할 것이다. 파이썬은 이런 문제를 해결하기 위해 다음과 같은 방법을 제공한다.
```python
def 함수이름(*매개변수):
    <수행할 문장>
    ...
```
일반적으로 볼 수 있는 함수 형태에서 괄호 안의 매개변수 부분이 `*매개변수`로 바뀌었다.

#### 여러 개의 입력값을 받는 함수 만들기
다음의 예를 통해 여러 개의 입력값을 모두 더하는 함수를 직접 만들어 보자.
```python
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
```
위에서 만든 `sum_many`라는 함수는 입력값이 몇 개이든 상관이 없다. `*args`처럼 매개변수명 앞에 `*`를 붙이면 입력값들을 전부 모아서 튜플로 만들어 주기 때문이다. 만약 `sum_many(1, 2, 3)`처럼 이 함수를 쓰면 `args`는 `(1, 2, 3)`이 되고, `sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`처럼 쓰면 `args`는 `(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`이 된다 여기서 `*args`라는 것은 임의로 정한 변수명이다. `*pey`, `*python`처럼 아무 이름이나 써도 된다.

> args는 입력 인수를 뜻하는 영어 단어인 arguments의 약자이며 관례적으로 자주 사용된다.

함수의 인수로 `*args(*매개변수)`만 사용할 수 있는 것은 아니다. 다음의 예를 보자.
```python
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
        return result
```
위의 예는 매개변수로 `choice`와 `*args`를 사용했다. 따라서 다음과 같이 쓸 수 있다.
```python
result = sum_mul('sum', 1,2,3,4,5)
print(result)
15
result = sum_mul('mul',1,2,3,4,5)
print(result)
120
```

>__[키워드 파라미터 kwargs]__

이번에는 키워드 파라미터인 `**kwargs`에 대해서 알아보자 kwargs는 keword arguments의 약어이다. `**kwargs`는 `*args`와는 달리 `*`가 두 개 사용된다. 역시 이것도 예제로 알아보자.

먼저 다음과 같은 함수를 작성 해 보자.

```python
def func(**kwargs):
    print(kwargs)
```
그리고 이 함수를 다음과 같이 사용해 보자.
```python
>>> func(a=1)
{'a': 1}
>>> func(name='foo', age=3)
{'age' :3, 'name': 'foo'}
```
`func` 함수의 인수로 key=value 형태를 주었을 때 입력 값 전체가 kwargs라는 딕셔너리에 저장된다는 것을 알 수 있다.

즉, `**kwargs`는 모든 key=value 형태의 입력인수가 저장되는 딕셔너리 변수이다.

이번에는 다음과 같은 형태의 호출에 대해서 생각해보자.

```python
>>> func(1, 2, 3, name='foo', age=3)
```
일반적인 입력이눗가 키워드형태의 입력 뒤에 존재하는 경우이다. 호출하면 다음과 같은 오류를 만나게 된다.
```python
>>> func(1, 2, 3, name='foo', age=3, 4, 5)
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
```
키워드 형태의 인수뒤에 키워드 형태가 아닌 인수는 올 수 없음을 알 수 있다. 따라서 다음과 같은 형태의 호출로 변경해야 할 것이다.

```python
>>> func(1, 2, 3, 4, 5, name='foo', age=3)
(1, 2, 3, 4, 5)
{'age': 3, 'name': 'foo'}
```

### 함수의 결과값은 언제나 하나이다
```python
def sum_and_mul(a,b):
    return a+b, a*b
```
이 함수를 다음과 같이 호출하면 어떻게 될까?
```python
result = sum_and_mul(3,4)
```
결과값은 `a+b`와 `a*b` 2개인데 결과값을 받아들이는 변수는 result 하나만 쓰였으니 오류가 발생하지 않을까? 하지만 오류는 발생하지 않는다. 그 이유는 함수의 결과값은 2개가 아니라 언제나 1개라는 데 있다. `sum_and_mul` 함수의 결과값 `a+b`와 `a*b`는 튜플값 하나인 `(a+b,a*b)`로 돌려준다.

따라서 result 변수는 다음과 같은 값을 갖게 된다.
```python
result = (7, 12)
```
즉 결과값으로 (7,12)라는 튜플 값을 갖게 되는 것이다.

만약 이 하나의 튜플값을 2개의 결과값처럼 받고 싶다면 다음과 같이 함수를 호출하면 된다.
```python
sum, mul = sum_and_mul(3, 4)
```
이렇게 호출하면 sum은 7이되고 mul은 12가 된다.

### 매개변수에 초깃값 미리 설정하기
```python
def say_myself(name, old, man=True):
    print("이름 : %s" % name)
    print("나이 : %d" % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
```
`say_myself`함수는 다음처럼 사용할 수 있다.
```python
say_myself("박응용", 27)
say_myself("박응용", 27, True)
```
man이라는 변수에는 입력값을 주지 않았지만 초깃값인 `True`값을 갖게 된다.

따라서 위의 예에서 함수를 사용한 2가지 방법은 모두 동일한 결과를 출력한다.

#### 함수 매개변수에 초깃값을 설정할 때 주의할 사항
만약 위에서 본 `say_myself` 함수를 다음과 같이 만들면 어떻게 될까?
```python
def say_myself(name, man=True, old): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.") 
    else: 
        print("여자입니다.")
```
이전 함수와 바뀐 부분은 초깃값을 설정한 매개변수의 위치이다. 결론을 미리 말하면 이것은 함수를 실행할 때 오류가 발생한다.

얼핏 생각하기에 위의 함수를 다음과 같이 하면 될 것 같다.
```python
say_myself("박응용", 27)
```
위와 같이 함수를 호출한다면 name 변수에는 "박응용"이 들어갈 것이다. 하지만 파이썬 인터프리터는 27을 man 변수와 old 변수 중 어느 곳에 전달해야 할지 알 수 없게 된다.

오류 메세지를 보면 다음과 같다
```python
SyntaxError: non-default argument follows default argument
```
위의 오류 메시지는 초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은 매개변수는 사용할 수 없다는 말이다. 즉, 매개변수로 (name, old, man=True)는 되지만 (name, man=True, old)는 안 된다는 것이다. 초기화시키고 싶은 매개변수들을 항상 뒤쪽에 위치시키는 것을 잊지 말자.

### 함수 안에서 선언된 변수의 효력 범위

함수 안에서 사용할 변수의 이름을 함수 밖에서도 동일하게 사용한다면 어떻게 될까?

아래의 예를 보자.
```python
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)
```
먼저 a라는 변수를 생성하고 1을 대입한다. 다음 입력으로 들어온 값에 1을 더해 주고 결과값은 돌려주지 않는 vartest 함수를 선언한다. 그리고 vartest 함수에 입력값으로 a를 주었다. 마지막으로 a의 값을 출력하는 print(a)를 입력한다. 과연 결과값은 무엇이 나올까?

당연히 vartest 함수에서 매개변수 a의 값에 1을 더했으니까 2가 출력되어야 할 것 같지만 프로그램 소스를 작성해서 실행시켜 보면 결과값은 1이 나온다. 그 이유는 함수 안에서 새로 만들어진 매개변수는 함수 안에서만 사용되는 "함수만의 변수"이기 때문이다. 즉, def vartest(a)에서 입력 값을 전달받는 매개변수 a는 함수 안에서만 사용되는 변수이지 함수 밖의 변수 a가 아니라는 뜻이다.

따라서 vartest 함수는 다음처럼 변수 이름을 hello로 한 vartest 함수와 완전히 동일하다.
```python
def vartest(hello):
    hello = hello + 1
```
즉, 함수 안에서 사용되는 매개변수는 함수 밖의 이름들과는 전혀 상관이 없다는 말이다.

#### 함수 안에서 함수 밖의 변수를 변경하는 방법
##### 1. return 이용하기
```python
# vartest_return.py
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)
```
첫 번째 방법은 return을 이용하는 방법이다. vartest 함수는 입력으로 들어온 값에 1을 더한값을 돌려준다. 따라서 a = vartest(a)라고 대입하면 a가 vartest 함수의 결과값으로 바뀐다. 여기서도 물론 vartest 함수 안의 a 매개변수는 함수 밖의 a와는 다른 것이다.

##### 2. global 명령어 이용하기
```python
# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)
```
두 번째 방법은 global이라는 명령어를 이용하는 방법이다. 위의 예에서 볼 수 있듯이 vartest 함수 안의 global a라는 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다. 하지만 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다. 왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다. 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다. 그러므로 가급적 global 명령어를 사용하는 이 방법은 피하고 첫 번째 방법을 사용하기를 권한다.

### lambda
lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다. 보통 함수를 한줄로 간결하게 만들 때 사용한다. 우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다. 사용법은 다음과 같다.
>lambda 매개변수1, 매개변수2, ...:매개변수를 이용한 표현식


한번 직접 만들어 보자.
```py
sum = lambda a, b: a+b
sum(3, 4)
7
```
위의 예제는 def를 사용한 아래 함수와 하는 일이 완전히 동일하다.
```py
def sum(a, b):
    return a+b
```
그렇다면 def가 있는데 왜 lambda라는 것이 나오게 되었을까? 이유는 간단하다. lambda는 def보다 간결하게 사용할 수 있기 때문이다.
또한 lambda는 def를 사용할 수 없는 곳에도 사용할 수 있다. 다음 예제에에서 리스트 내에 lambda가 들어간 경우를 살펴보자.
```py
myList = [lambda a,b:a+b, lambda a,b:a*b]
myList
[at 0x811eb2c>, at 0x811eb64>]
```
즉, 리스트 각각의 요소에 lambda 함수를 만들어 바로 사용할 수 있다. 첫 번째 요소 `myList[0]`은 2개의 입력값을 받아 두 값으 합을 돌려주는 lambda 함수이다.
```py
myList[0]
at 0x811eb2c>
myList[0](3,4)
7
```
두 번째 요소 `myLsit[1]`은 2개의 입력갑승ㄹ 받아 두 값의 곱을 도렬주는 lambda 함수이다.
```py
myList[1](3,4)
12
```
파이썬에 익숙해질수록 lambda 함수가 굉장히 편리하다는 사실을 알게 될 것이다.

## 연습문제
_(연습문제 풀이 : https://wikidocs.net/17090#04-1)_

<br>

__[문제1] 홀수 짝수 판별__

주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성하시오.

>[풀이1]
```python
def is_odd(n):
    if n % 2:
        print("홀수")
    else:
        print("짝수")

is_odd(4)
```

__[문제2] 평균값 계산__

입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 갯수는 정해져 있지 않다.)

>[풀이2]
```python
def avg(*args):
    sum = 0
    for i in args:
        sum += i
    result = sum/len(args)
    print("모든 수의 평균은 {}".format(result))

n = list(map(int, input("숫자 입력 >> ").split()))
avg(*n) # 리스트나 튜플과 같이 index가 존재하는 객체를 *표시를 붙여 인자로서 함수에 입력하면 함수의 정의된 위치에 맡게 입력이 됩니다.
```

__[문제3] 구구단 출력__

입력을 자연수 n(2부터 9까지의 자연수)으로 받았을 때, n에 해당되는 구구단을 출력하는 함수를 작성해 보자.

>[풀이3]
```python
def gg(n):
    for i in range(1,10):
        print("{} x {} = {}".format(n, i, n*i))

gg(2)
```

__[문제4] 피보나치__

입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.

피보나치 수열은 다음과 같은 순서로 결과값을 리턴한다.

fib(0) → 0 리턴
fib(1) → 1 리턴
fib(2) → fib(0) + fib(1) → 0 + 1 → 1 리턴
fib(3) → fib(1) + fib(2) → 1 + 1 → 2 리턴
fib(4) → fib(2) + fib(3) → 1 + 2 → 3 리턴

>[풀이4]
```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

for i in range(1, 11):
    print(fib(i))
```

__[문제5] 5보다 큰 수만__

다음은 숫자들로 이루어진 리스트를 입력으로 받아 5보다 큰 수만 필터링하여 리턴해 주는 함수이다.
```python
>>> def myfunc(numbers):
...     result = []
...     for number in numbers:
...         if number > 5:
...             result.append(number)
...     return result
... 
>>> myfunc([2,3,4,5,6,7,8])
[6, 7, 8]
```
위 함수를 lambda 함수로 변경해 보시오.

>[풀이5]
```python
big = lambda n : [i for i in n if i > 5]

list = big([1,2,3,4,5,6,7,8,9,10])
print(list)
```

---
<br>

## 출처
 - *Jump to python* *[https://wikidocs.net/24]*