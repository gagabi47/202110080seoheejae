#연습문제 8.1
#사용자 정의
def input_age(prompt) :
    while True :
        n = int(input(prompt))

        if  0<= n <= 120 :
            return n
      
def is_adult(age) :
    if 19<= age :
        return True
    else :
        return False

#주사용
age = input_age('나이? ')
if is_adult(age) :
    print('당신은 성인입니다.')
else :
    print('당신은 성인이 아닙니다.')

#연습문제 8.4
#사용자 정의
def is_leap_year(y) :
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
        return True
    else :
        return False

#return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) 위랑 똑같은 코드

#주사용 프로그램
while True:
    y =  int(input('윤년 여부를 확할 연도는 ?'))

#윤년여부 판별 및 출처
    if is_leap_year(y) :
        print(f'{y}년은 윤년입니다.')
    else:
        print(f'{y}년은 평달입니다.')

#반복할 것인지 확인
    reap = input('다른 연도도 확인하겠습니까? ')
    if reap != 'y' and reap !='Y' :
             break

    print()

#연습문제 8.5
#사용자 정의 1
def display_triangle(height):
    for i in range(1, height+1) :
        for j in range(1, i+1) :
            print(j, end='')
        print()

#주 프로그램
h=int(input('높이는? '))
display_triangle(h)

#사용자 정의2
def display_triangle(height, sh = '*'):
    for i in range(1, height +1):
        draw_line(' ', height -1)
        draw_line(ch, i)
        print()

def draw_line(ch, n):
    print(ch * n, end='')

h = int(input('높이? '))

display_triangle(h)

#개념확인
def display_multiplication_block(start_dan, end_dan):
    for i in range(1, 10):
        for dan in range(start_dan, end_dan+1):
            print(f'{dan} * {i} = {dan*i:2d}', end='    ')
        print()


def display_all_multiplication_tables():
    display_multiplication_block(2, 5)
    print()
    display_multiplication_block(6, 9)

#주사용
display_all_multiplication_tables()
