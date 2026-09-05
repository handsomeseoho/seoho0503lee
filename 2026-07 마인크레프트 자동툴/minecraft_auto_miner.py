import pyautogui
import keyboard
import time

print("마인크래프트 오토 클리커")
print("F8: 근접 공격/채굴 시작/정지 토글")
print("F9: 원거리 무기 연타 (돌풍구, 물약 등) 시작/정지 토글")
print("F10: 우클릭 꾹 눌렀다 떼기 (활, 삼지창) 시작/정지 토글")
print("F12: 우클릭 꾹 눌러 장전 후 발사 (쇠내) 시작/정지 토글")
print("ESC: 종료")
print("마우스를 사용할 위치에 올리고 해당 키를 누르세요")

running = False
ranged_running = False
charge_running = False
reload_running = False

# 설정
click_delay = 0.02  # 클릭 딜레이 (초)
ranged_delay = 0.1  # 원거리 무기 연타 딜레이 (초)
charge_time = 1.0  # 활/삼지창 차지 시간 (초)
reload_time = 1.5  # 쇠내 장전 시간 (초)


def toggle():
    global running
    running = not running
    if running:
        print("근접 공격/채굴 시작!")
    else:
        pyautogui.mouseUp(button='left')  # 마우스 떼기
        print("근접 공격/채굴 정지!")

def toggle_ranged():
    global ranged_running
    ranged_running = not ranged_running
    if ranged_running:
        print("원거리 무기 연타 시작!")
    else:
        pyautogui.mouseUp(button='right')  # 마우스 떼기
        print("원거리 무기 연타 정지!")

def toggle_charge():
    global charge_running
    charge_running = not charge_running
    if charge_running:
        print("활/삼지창 모드 시작!")
    else:
        pyautogui.mouseUp(button='right')  # 마우스 떼기
        print("활/삼지창 모드 정지!")

def toggle_reload():
    global reload_running
    reload_running = not reload_running
    if reload_running:
        print("쇠내 모드 시작!")
    else:
        pyautogui.mouseUp(button='right')  # 마우스 떼기
        print("쇠내 모드 정지!")


keyboard.add_hotkey('f8', toggle)
keyboard.add_hotkey('f9', toggle_ranged)
keyboard.add_hotkey('f10', toggle_charge)
keyboard.add_hotkey('f12', toggle_reload)


try:
    print("\n프로그램 준비 완료.")
    
    while True:
        if running:
            # 근접 공격/채굴: 현재 마우스 위치에서 좌클릭 반복
            pyautogui.mouseDown(button='left')
            time.sleep(0.1)
            pyautogui.mouseUp(button='left')
            time.sleep(click_delay)
        elif ranged_running:
            # 원거리 무기 연타: 우클릭 반복 (돌풍구, 물약 등)
            pyautogui.mouseDown(button='right')
            time.sleep(0.1)
            pyautogui.mouseUp(button='right')
            time.sleep(ranged_delay)
        elif charge_running:
            # 활/삼지창: 우클릭 꾹 눌렀다 떼서 발사
            pyautogui.mouseDown(button='right')
            time.sleep(charge_time)
            pyautogui.mouseUp(button='right')
            time.sleep(ranged_delay)
        elif reload_running:
            # 쇠내: 우클릭 꾹 눌러 장전, 그 후 우클릭으로 발사
            pyautogui.mouseDown(button='right')
            time.sleep(reload_time)
            pyautogui.mouseUp(button='right')
            time.sleep(0.1)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            time.sleep(ranged_delay)
        else:
            time.sleep(0.01)
        
except KeyboardInterrupt:
    print("\n프로그램 종료")
