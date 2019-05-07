#파이선 키워드 확인
import keyword
from builtins import print
from itertools import product

print('키워드 리스트: ', keyword.kwlist)
print('키워드 개수: ', len(keyword.kwlist))

#마지막 실행 결과값은 언더스코어 객체에 저장됨
_=10
print('_:', _)

#언더스코어의 무시기능 -> 빈 내역을 땜빵
x,_,y,_,z = [1,2,3,4,5]
print(x,y,z)

#자료형을 통해 객체 선언
a=1
b='안녕'
c=[]
d=()
e={}
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))


#계산기 기능
print(3+2)
print(3-2)
print(3*2)
print(3/2)

#연속 객체 할당
a=b=c=0
print(a)

#콤마 기호로 할당
c,d = 3,4
print(c,d)

#세미콜론 사용
e = 3.5; f = 5
print(e)
print(f)

#인덱스 접근
a = [1,2,3]
print(a[0:2])

#일반 함수
def add(a,b):
    return a+b
print(add(3,4))

#for문
for a in [1,2,3]:
    print(a)

#while문
i = 0
while i <3 :
    i +=1
    print(i)


#모듈
import sys
import calendar

print(sys.version)
calendar.prmonth(2019,5,10,0)

#10진수를 2진수로
print(bin(10))

#10진수를 8진수로
print(oct(10))

#10진수를 16진수로
print(hex(10))

#정수를 부동소수로 반환
print(float(5))

#정수의 몫과 나머지를 반환
print(divmod(7,3))

#int함수: 다른 형식의 진수를 10진수로 변환
print(int('3'))
print(int(3.5))
print(int('111', 2))
print(int('111', 8))
print(int('111', 16))
print(int('111', 10),"\n")

#pow 함수
print(pow(2,3))
print(pow(2,-3))
