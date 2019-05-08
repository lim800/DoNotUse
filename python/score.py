#점수 입력

kor = int(input('국어점수: '))
mth = int(input('수학점수: '))
eng = int(input('영어점수: '))

total = kor + mth + eng

if total >= 180:
    if kor > 40 and mth > 40 and eng > 40:
        print("합격")
    else: print("불합격")

else: print("불합격")