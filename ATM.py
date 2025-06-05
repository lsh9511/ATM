#잔액 초기화
balance = 100000 
x = 0
while True : # 조건이 True면 계속 작동합니다.
    num = input('사용하실 기능을 선택해주세요 (1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료): ')
    # 개발할때 최소한의 자원만 쓸 수 있도록 고려를 해보는게 더 좋습니다.
   
    #2번 출금 기능 코드
    if num == "2" :
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : "))  
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')
              
    #1번 입금 기능 코드
    if num == "1" : 
        # 얼마를 입금할거야?
        deposit_amount = int(input("입금할 금액을 입력해주세요 : "))
        
        balance += deposit_amount
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
    
    #4번 종료 기능 코드
    if num == "4" :
        print("종료")
        break


