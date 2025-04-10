#연습문제 6.2
def introduce(name, grade):
    real_name = name[1:]
    next_grade = grade +1
    return real_name + '은 내년에' + str(next_grade) + '학년입니다.'

name = input('이름?')
grade = int(input('학년?'))
result = introduce(name, grade)
print(result)

#연습문제 6.4
def rep_char(c, n):
    print(c * n)

rep_char('-', 10)
rep_char('#', 5)

#연습문제 6.5
def rep_char(c,n):
    print(c * n)

def draw_line_string(s):
    width = len(s) * 2
    rep_char('-', width)
    print(s)
    rep_char('-', width)

draw_line_string('안녕하세요')
draw_line_string('안녕')

#개념확인
def rep_char(c, n):
    print(c * n)

def draw_box(msg1, msg2):
    nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)
    rep_char('-', nstr)
    print(msg1)
    print(msg2)
    rep_char('-', nstr)

name = input("Input his/her name: ")
msg1 = "Hello " + name + ","
msg2 = "Welcome to Seoul."

draw_box(msg1, msg2)
