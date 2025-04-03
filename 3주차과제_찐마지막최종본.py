

#5.1 문제
exchange_rate=0

def set_rate(rate):
    global exchange_rate
    exchange_rate=rate
def get_rate():
    return exchange_rate
def to_dollar(won):
    return won / exchange_rate
def to_won(dollar):
    return dollar*exchange_rate

def main():
    print('###환율 변환 모듈 테스트###')

    set_rate(1010)

    print('오늘의 환율', get_rate())
    print('2020원=', to_dollar(2020), '달러')
    print('2달러=', to_won(2), '원')

if __name__ == '__main__':
    main()
    

#5.2 문제
import exchange_currency as eRate

rate = int(input('$1에대한 오늘의 환율은?'))
eRate.set_rate(rate)

dollar = int(input('원화로 변환할 달러화 액수는?'))
print(dollar, '달러는', eRate.to_won(dollar),'원입니다')

won = int(input('달러화로 변환할 원화 액수는?'))
print(won, '원은', eRate.to_dollar(won), '달러입니다')



#5.5 문제
discount_rate = 0

#할인전 가격 식 넣어두기
def get_fixed_price(rate): 
    global discount_rate
    originalprice=rate/(1-discount_rate/100)

    return int(originalprice)

discount_rate=int(input('할인율?'))
aprice=int(input('A상품의 할인된 가격은?'))
bprice=int(input('B상품의 할인된 가격은?'))
print('A상품의 정가는', get_fixed_price(aprice), '원')
print('B상품의 정가는', get_fixed_price(bprice), '원')


