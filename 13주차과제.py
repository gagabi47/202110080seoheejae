#12.1
#메모 입력
with open('readme.txt', 'w', encoding='utf-8') as file:
  file.write('안녕하세요, 반갑습니다.\n')
  file.write('이 파일은 테스트 파일 저작을 위해 작성된 텍스트 문서입니다.\n')
  file.write('조금 낯설더라도 포기하지 마세요.\n')

#사용자정의
def show_file(filename):
  with open(filename, 'r', encoding='utf-8') as file:
    i = 1
    while True:
      line = file.readline()

      if line == '':
        break
      print(f'{i}: {line.strip()}')
      i += 1

#주프
fn = input('파일명 : ')
show_file(fn)

#12.3
import os
filename = 'shoppingbag.txt'


  #10.5코드
def buy(sbag):
  print('[구입]')
  item = input('상품명? ')

  if item == '':
    return False

  sbag.append(item)
  print(f'장바구니에 {item}가(이) 담겼습니다\n')

  return True

def show(sbag):
  print('\n>>> 장바구니 보기: ', end= '')
  print(sbag)

def save_data(sbag, filepath):
  with open(filepath, 'w', encoding='utf8')as file:
    for item in sbag:
      file.write(f'{item}\n')
def load_data(filepath):
  lines= []
  with open(filepath, 'r', encoding = 'utf8') as file:
    for line in file:
      lines.append(line.strip('\n'))
  return lines
if os.path.exists(filename):
  print('파일')
  shopping_bag = load_data(filename)
  show(shopping_bag)
else:
  shopping_bag = []

while True:
  if buy(shopping_bag) == False:
    break

show(shopping_bag)

save_data(shopping_bag, filename)

#12.4
import os
import pickle
from datetime import datetime
filename = 'last_dat'

#11.2
#클래스
class Time :
  def __init__(self, hour=0, minute=0):
    self.__hour = hour
    self.__minute = minute

  def display(self):
    print(f'{self.__hour:02d}:{self.__minute:02d}')

  def add(self, time):
    h = self.__hour + time.__hour
    m = self.__minute + time.__minute
    if m >= 60 :
      h += 1
      m -= 60
    return Time(h, m)

  @staticmethod
  def is_valid(hour, minute) :
    if 0<= hour < 24 and 0 <=minute < 60:
      return True
    return False

  def toString(self):
    return f'{self.__hour: 02d}:{self.__minute:02d}'

#사용자정의
def get_current_time():
  now = datetime.now()
  return Time(now.hour, now.minute)
def save_time(time):
  with open(filename, 'wb') as file:
    pickle.dump(time, file)
def load_time():
  with open(filename, 'rb') as file:
    t= pickle.load(file)
  return t

#주프
if os.path.exists(filename):
  t = load_time()
  print(f'안녕하세요, 마지막으로 {t.toString()} 에 실행되었습니다.')
else:
  print('안녕하세요, 처음 실행되었습니다.')

t= get_current_time()
print(f'지금은 {t.toString()}입니다.')
save_time(t)

#12.2
import os
import pickle
filename = 'score.bin'

#사용자 정의
def input_scores():
  s = []
  i = 1
  while True:
    n =int(input(f'#{i}? '))
    if n < 0 :
      break
    s.append(n)
    i += 1
    return s

def get_average(s):
  total = 0
  for n in s:
    total += n
  return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(s, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(s, file)

def load_scores(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)

#주프
if os.path.exists(filename):
    print('[파일 읽기]')
    scores = load_scores(filename)
else:
    print('[점수 입력]')
    scores = input_scores()
    save_scores(scores, filename)

print('\n[점수 출력]')
print('개인 점수 : ', end='')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}')
