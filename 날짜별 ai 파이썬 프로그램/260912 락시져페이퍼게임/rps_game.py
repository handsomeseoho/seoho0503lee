import random

while True:
    # 사용자 입력 받기
    user = input("가위, 바위, 보 중 하나를 선택하세요 (종료하려면 'q'): ")
    
    # 종료 조건
    if user == 'q':
        print("게임을 종료합니다.")
        break
    
    # 컴퓨터 랜덤 선택
    computer = random.choice(['가위', '바위', '보'])
    
    # 결과 출력
    print(f"사용자: {user}")
    print(f"컴퓨터: {computer}")
    
    # 승패 판정
    if user == computer:
        print("무승부!")
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        print("사용자 승리!")
    else:
        print("컴퓨터 승리!")
    
    print()  # 줄바꿈
