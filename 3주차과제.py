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


