import pyautogui
import keyboard
import time
import speech_recognition as sr
import threading
import pyperclip

# ==================== 자동 클리커 설정 ====================
print("마인크래프트 통합 자동툴")
print("=== 자동 클리커 ===")
print("F8: 근접 공격/채굴 시작/정지 토글")
print("F9: 원거리 무기 연타 (돌풍구, 물약 등) 시작/정지 토글")
print("F10: 우클릭 꾹 눌렀다 떼기 (활, 삼지창) 시작/정지 토글")
print("F11: 우클릭 꾹 눌러 장전 후 발사 (쇠내) 시작/정지 토글")
print("=== 음성 인식 ===")
print("F12: 음성 녹음 시작/정지 (누르고 있으면 녹음, 떼면 변환)")
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

# ==================== 자동 클리커 함수 ====================
def toggle():
    global running
    running = not running
    if running:
        print("근접 공격/채굴 시작!")
    else:
        pyautogui.mouseUp(button='left')
        print("근접 공격/채굴 정지!")

def toggle_ranged():
    global ranged_running
    ranged_running = not ranged_running
    if ranged_running:
        print("원거리 무기 연타 시작!")
    else:
        pyautogui.mouseUp(button='right')
        print("원거리 무기 연타 정지!")

def toggle_charge():
    global charge_running
    charge_running = not charge_running
    if charge_running:
        print("활/삼지창 모드 시작!")
    else:
        pyautogui.mouseUp(button='right')
        print("활/삼지창 모드 정지!")

def toggle_reload():
    global reload_running
    reload_running = not reload_running
    if reload_running:
        print("쇠내 모드 시작!")
    else:
        pyautogui.mouseUp(button='right')
        print("쇠내 모드 정지!")

# 자동 클리커 핫키 등록
keyboard.add_hotkey('f8', toggle)
keyboard.add_hotkey('f9', toggle_ranged)
keyboard.add_hotkey('f10', toggle_charge)
keyboard.add_hotkey('f11', toggle_reload)

# ==================== 음성 인식 설정 ====================
r = sr.Recognizer()
is_recording = False
recording_thread = None
audio_data = None
recording_lock = threading.Lock()

def record_voice():
    global is_recording, audio_data
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("녹음 중... (F12을 떼면 변환)")
            with recording_lock:
                audio_data = None
            new_audio = r.listen(source, timeout=None, phrase_time_limit=None)
            with recording_lock:
                audio_data = new_audio
            print("녹음 완료")
    except Exception as e:
        print(f"녹음 오류: {e}")
        with recording_lock:
            audio_data = None
        is_recording = False

def convert_speech_to_text():
    global audio_data
    try:
        with recording_lock:
            current_audio = audio_data
            audio_data = None
        
        if current_audio:
            print("음성 변환 중...")
            text = r.recognize_google(current_audio, language="ko-KR")
            print(f"인식된 텍스트: {text}")
            
            pyperclip.copy(text)
            time.sleep(0.2)
            
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.3)
            
            print("텍스트 입력 완료 - Enter를 눌러 전송하세요")
        else:
            print("녹음된 데이터가 없습니다")
    except sr.UnknownValueError:
        print("음성을 인식하지 못했습니다")
    except sr.RequestError as e:
        print(f"Google 서비스 오류: {e}")
    except Exception as e:
        print(f"오류: {e}")

def toggle_voice_press(event):
    global is_recording, recording_thread
    if not is_recording:
        is_recording = True
        recording_thread = threading.Thread(target=record_voice)
        recording_thread.daemon = True
        recording_thread.start()

def toggle_voice_release(event):
    global is_recording
    if is_recording:
        is_recording = False
        if recording_thread and recording_thread.is_alive():
            recording_thread.join(timeout=1)
        if audio_data is not None:
            convert_speech_to_text()
        else:
            print("녹음된 데이터가 없어 변환을 건너뜁니다")

# 음성 인식 핫키 등록 (F12)
keyboard.on_press_key("f12", toggle_voice_press)
keyboard.on_release_key("f12", toggle_voice_release)

# ==================== 메인 루프 ====================
try:
    print("\n프로그램 준비 완료.")
    
    while True:
        if running:
            pyautogui.mouseDown(button='left')
            time.sleep(0.1)
            pyautogui.mouseUp(button='left')
            time.sleep(click_delay)
        elif ranged_running:
            pyautogui.mouseDown(button='right')
            time.sleep(0.1)
            pyautogui.mouseUp(button='right')
            time.sleep(ranged_delay)
        elif charge_running:
            pyautogui.mouseDown(button='right')
            time.sleep(charge_time)
            pyautogui.mouseUp(button='right')
            time.sleep(ranged_delay)
        elif reload_running:
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
except Exception as e:
    print(f"오류: {e}")
finally:
    keyboard.unhook_all()
    pyautogui.mouseUp(button='left')
    pyautogui.mouseUp(button='right')
