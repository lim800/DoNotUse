#str : 부동소수를 표현하는 문자열로 반환
print(str('0.3'))

#repr: 부동소수를 시스템에서 확인 하는 공식적인 문자열을 반환
print(repr('0.3'))

#input 함수
#a = input('입력: ')
#print(a)

#print 함수
for i in range(2):
    print(i, end=' ')

print()
#del: 변수를 삭제
# a = 9
# del a
# print(a)

#정수형 객체를 선언, id로 레퍼런스 확인
a= 10
print(id(a))

#real 내장 메소드로 정수의 실제값 확인
a= 10
print(a.real)

# 두가지 객체의 레퍼런스 확인 테스트
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(id(a), id(b))
x = 1
y = 1
print(x is y)
print(id(x),id(y))

c = [1,2,3,4]
d = [1,2,3,4]
print(c==d)


#함수의 객체화
def call():
    print("객체 호출")

f= call()
f
f = call
f()

#파라미터 있는 함수 콜
def add(a,b):
    return a+b
f = add
print('f 객체 함수 호출: ' , f(4,5))
print('add 함수 식별자의 형식: ' , add)
print('f 객체 실별자의 형식: ' , f)
print('f 객체와 add 함수의 멤버십 테스트', f is add)

#람다 함수의 객체화
f= lambda x,y : x+y
print(f(1,2))


#객체의 인덱스 할당
a = [1,2,3]
b = [1,a,3]
a[1] = 1000
print(a)
print(b)
print()

#객체의 레퍼런스 할당
a = [1,2,3]
print(id(a))
b = [1,a,2]
print(id(b))
c = ['x', a, 'y']
print(id(c))
print(a)
print(b)
print(c)
print()

#객체의 복사
a = [1,2,3,4]
print(id(a))
b = a
print(id(b))
print(b)
b[2] = 100
print(b)
print(a)

#input 함수를 통해 입력 받은 값의 타입
# a = input('나이: ')
# print(a)
# b =  int(input('숫자 입력: '))
# print(b)

# 리스트 자료형의 값 변경
a = [1,2,3]
a[0] = 5
print(a)

#딕셔너리 자료형의 값 변경
b = {'1':'3번','2':'2번','3':'3번'}
b['1'] = '1번'
print(b)

#숫자 자료형에 값을 할당하여 레퍼런스 치환
x = 1
print('1의 레퍼런스', id(x))
x = 2
print('2의 레퍼런스',  id(x))

#2진수를 10진수로 변환
a = 0b1010
print(type(a))
print(a)


#싱글쿼터는 단어로 인식, 더블쿼터는 표현으로 인식
#더블쿼터는 다른 언어의 문법을 담을때 사용
print('hello world')
print("hello world")

#쿼테이션을 두번 써야할땐 더블쿼터 안에 싱글쿼터를 사용(혹은 반대)
print("안녕 '파이썬'")

#트리플 쿼테이션 사용
print("""
this is 
a triple quotation

dot
""")

#역슬래시 사용
print('Don\'t walk alone')
print('\"Python is very easy.\" he said,')
print('python is an \
object-oriented \
language')

#이스케이프 문자
print('123\n456')
print('123\t456')
print('1\r2345')

#자료형의 연산
print('안' + '녕')
print(('hello\t'*3))

#인덱싱 구현
#슬라이스
s = 'he llo'
print(s[0])
print(s[1])
print(s[-1],s[-2],s[-3])
print(s[1:3])
print(s[:])
print(s[1:6:2])
print(s[::2])
print(s[::-1])

s= 'k' + s[1:]
print(s)

m = '20190503Sunny'
date = m[:8]
weather = m[8:]
print('날짜:', date)
print('날씨', weather)
year = date[:4]
month = date[4:6]
day = date[6:8]
print('년도:', year)
print('월:', month)
print('일:', day)


name = 1234
a = '안녕하세요' + str(name) + '님!'
print(a)