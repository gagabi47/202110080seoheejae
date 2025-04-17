#연습문제 7.2
#사용자 정의
def is_leap_year(y) :
    if(y % 4 == 0 and y % 100 !=0) or (y%400==0) :
        return True
    else :
        return False
def month_days(y, m) :
    if m ==4 or m == 6 or m== 9 or m==11 :
        return 30
    elif m == 2 :
        if is_leap_year(y) :
            return 29
        else :
            return 28
    else :
        return 31

#주 프로그램
year = int(input('연도는? '))
month = int(input('월? '))
ndays = month_days(year, month)
print(f'{year}년 {month}월은 {ndays}일까지 있습니다.')

#연습문제 7.4
#사용자 정의
def input_age(prompt) :
    n = int(input(prompt))
    if 0<= n and 120>= n :
        return n
    else :
        return -1
    
def is_adult(age) :
    if 19<= age :
        return True
    else :
        return False

#주사용
age = input_age('나이? ')
if age >= 0 :
    if is_adult(age) :
        print('당신은 성인입니다.')
    else :
        print('당신은 성인이 아닙니다.')
else :
    print('오류 : 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')

#연습문제 7.5
#사용자 정의
def find_char_type(ch) :
    if ch == ' ' :
        return '공백'
    elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' :
        return '알파벳'
    elif '0' <= ch <= '9' :
        return '숫자'
    else :
        return '기타'
#주 프로그램
c = input('한 문자 입력? ')
ctype = find_char_type(c)
print(f'{ctype} 문자를 입력했습니다.')

#연습문제 7.6
#사용자 정의
def read_single_digit(f) :
    text = ('영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구')
    print(text[f], end=' ')
    
def read_number(num) :
    for digit in num :
        read_single_digit(int(digit))

#주프로그램
number = input('세자리 정수 입력: ')
read_number(number)
    

