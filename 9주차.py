#연습문제 9.1
scores = []
print('[점수 입력]')
for i in range(3):
    n = int(input(f'#{i + 1}? '))
    scores.append(n)
print('\n[점수 출력]')
print(f'입력점수: {scores[0]} {scores[1]} {scores[2]}')
avg = (scores[0] + scores[1] +scores[2] / len(scores))
print(f'평균: {avg:.1f}')

#연습문제 2
scores = []
print('[점수 입력]')
for i in range(3):
    n = int(input(f'#{i + 1}? '))
    scores.append(n)
    
print('\n[점수 출력]')
print(f'입력점수: {scores[0]} {scores[1]} {scores[2]}')
avg = (scores[0] + scores[1] +scores[2] / len(scores))
print(f'평균: {avg:.1f}')

print('\n[검색]')
s = int(input('찾고자하는 점수는? '))
if s in scores :
       idx = scores.index(s)
       print(f'{s}점은 {idx +1}번 학생의 점수입니다.')
else :
    print(f'{s}점을 받은 학생은 없습니다.')

#연습문제 9.3
shopping_bag = []

print('[구입]')
while True :
    item = input('상품명? ')
    if item ==' ':
        break
    shopping_bag.append(item)
    print(f'장바구니에 {item}가(이) 담겼습니다.')

print(f'\n>>> 장바구니 보기 : {shopping_bag}')    

#연습문제 9.4
shopping_bag = {}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':  
        break
    count = int(input('수량은? '))

    if item in shopping_bag:
        shopping_bag[item] += count
    else:
        shopping_bag[item] = count

    print(f'장바구니에 {item} {count}개가 담겼습니다.')

print('\n>>> 장바구니 보기:', shopping_bag)

print('\n[검색]')
item = input('장바구니에서 확인하고자 하는 상품은? ')
if item in shopping_bag:
    print(f'{item}(은)는 {shopping_bag[item]}개 담겨 있습니다.')
else:
    print(f'{item}은(는) 장바구니에 없습니다.')

