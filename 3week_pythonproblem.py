def get_integer():
    while True:
        try:
            amount = int(input("동전으로 교환하고자 하는 금액은? "))
            if amount >= 0:
                return amount
            else:
                print("양수를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

def exchange(amount):
    coins = [500, 100, 50, 10]  
    coin_counts = {}  
    
    for coin in coins:
        coin_counts[coin] = amount // coin
        amount %= coin  
    
    for coin, count in coin_counts.items():
        print(f"{coin}원 동전의 개수: {count}")

amount = get_integer()
exchange(amount)
