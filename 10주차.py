#연습문제 10.2
def find_max(lst) :
  m=lst[0]
  for i in range(1, len(lst)):
    if lst[i]> m :
      m = lst[i]

  return m

#주프
nums = []

for i in range(5):
  n = int(input('정수입력; '))
  nums.append(n)

print(f'가장 큰 정수는 {find_max(nums)}입니다.')

#연습문제 10.3
#사용자정의
def input_scores():
    s = []
    i = 1
    while(True):
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s :
        total += n
    return total/len(s)

def show_scores(s):
    for n in s :
        print(n, end = ' ')
    print()

#주프
print('[점수 입력]')
scores = input_scores()

print('\[점수 출력]')
print('개인 점수 : ', end ='')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}')


#연습문제 10.4
def input_scores():
  s = []
  i =1
  while (True):
    n = int(input(f'#{i}? '))
    if n < 0:
      break
    s.append(n)
    i += 1
  return s

def get_average(s):
  total = 0
  for n in s:
    total += n
  return total/len(s)

def show_scores(s):
  for n in s :
    print(n, end='')
  print()

def search(lst, n):
  if n not in lst:
    return None
  
  return lst.index(n)

#주프
print('[점수 입력]')
scores = input_scores()

print('\n[점수 출력]')
print('개인 점수 : ', end=' ')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}')

print('\n[검색]')
s = int(input('찾고자 하는 점수는? '))
idx = search(scores, s)
if idx != None:
  print(f'{s}점은 {idx +1}번 학생의 점수입니다.')
else:
  print(f'{s}점을 받은 학생은 없습니다.')


#10.6
#사용자
def buy(shopping_bag):
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        return False 
    count = int(input('수량은? '))

    if item in shopping_bag:
        shopping_bag[item] += count
    else:
        shopping_bag[item] = count

    print(f'장바구니에 {item} {count}개가 담겼습니다.')
    return True  

def show(shopping_bag):
    print('\n>>> 장바구니 보기:', shopping_bag)

def find(shopping_bag):
    print('\n[검색]')
    item = input('장바구니에서 확인하고자 하는 상품은? ')
    if item in shopping_bag:
        print(f'{item}(은)는 {shopping_bag[item]}개 담겨 있습니다.')
    else:
        print(f'{item}은(는) 장바구니에 없습니다.')


# 주프
shopping_bag = {}

while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
