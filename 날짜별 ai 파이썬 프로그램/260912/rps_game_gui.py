import random  # 랜덤 모듈 가져오기
import tkinter as tk  # GUI 모듈 가져오기

# 전역 변수 선언
user_label = None
computer_label = None
result_label = None

def play(user_choice):  # 게임 실행 함수
    global user_label, computer_label, result_label  # 전역 변수 사용 선언
    
    computer = random.choice(['가위', '바위', '보'])  # 컴퓨터 랜덤 선택
    
    user_label.config(text=f"사용자: {user_choice}")  # 사용자 선택 표시
    computer_label.config(text=f"컴퓨터: {computer}")  # 컴퓨터 선택 표시
    
    if user_choice == computer:  # 선택이 같으면
        result = "무승부!"  # 무승부
    elif (user_choice == "가위" and computer == "보") or \
         (user_choice == "바위" and computer == "가위") or \
         (user_choice == "보" and computer == "바위"):  # 사용자 승리 조건
        result = "사용자 승리!"  # 사용자 승리
    else:  # 그 외의 경우
        result = "컴퓨터 승리!"  # 컴퓨터 승리
    
    result_label.config(text=result)  # 결과 표시

root = tk.Tk()  # 윈도우 생성
root.title("가위바위보")  # 창 제목 설정

user_label = tk.Label(root, text="사용자: ")  # 사용자 라벨 생성
user_label.pack()  # 라벨 배치

computer_label = tk.Label(root, text="컴퓨터: ")  # 컴퓨터 라벨 생성
computer_label.pack()  # 라벨 배치

result_label = tk.Label(root, text="")  # 결과 라벨 생성
result_label.pack()  # 라벨 배치

tk.Button(root, text="가위", command=lambda: play("가위")).pack()  # 가위 버튼
tk.Button(root, text="바위", command=lambda: play("바위")).pack()  # 바위 버튼
tk.Button(root, text="보", command=lambda: play("보")).pack()  # 보 버튼

root.mainloop()  # 윈도우 실행
