# 음성 인식 라이브러리 임포트
import speech_recognition as sr
# 키보드 이벤트 감지 라이브러리 임포트
import keyboard
# 자동화 라이브러리 임포트 (키 입력, 마우스 제어)
import pyautogui
# 시간 관련 라이브러리 임포트
import time
# 스레딩 라이브러리 임포트 (병렬 처리)
import threading
# 클립보드 제어 라이브러리 임포트
import pyperclip

# 음성 인식기 객체 생성
r = sr.Recognizer()
# 녹음 중 상태 변수
is_recording = False
# 녹음 스레드 변수
recording_thread = None
# 오디오 데이터 변수
audio_data = None
# 스레드 동기화를 위한 락 객체
recording_lock = threading.Lock()

# 녹음 시작 함수
def start_recording():
    # 전역 변수 사용 선언
    global is_recording, audio_data
    try:
        # 마이크를 소스로 사용
        with sr.Microphone() as source:
            # 환경 소음 조절 (0.5초 동안)
            r.adjust_for_ambient_noise(source, duration=0.5)
            # 녹음 중 메시지 출력
            print("녹음 중... (F10을 떼면 변환)")
            # 새로운 녹음 시작 전에 이전 데이터 초기화 (락 사용)
            with recording_lock:
                audio_data = None
            # 계속 녹음 (타임아웃 없음, 구간 제한 없음)
            new_audio = r.listen(source, timeout=None, phrase_time_limit=None)
            # 녹음된 데이터 저장 (락 사용)
            with recording_lock:
                audio_data = new_audio
            # 녹음 완료 메시지
            print("녹음 완료")
    # 예외 처리
    except Exception as e:
        # 녹음 오류 메시지
        print(f"녹음 오류: {e}")
        # 오디오 데이터 초기화 (락 사용)
        with recording_lock:
            audio_data = None
        # 녹음 상태 해제
        is_recording = False

# 음성을 텍스트로 변환하고 입력하는 함수
def transcribe_and_type():
    # 전역 변수 사용 선언
    global audio_data
    try:
        # 락을 사용하여 오디오 데이터 안전하게 가져오기
        with recording_lock:
            current_audio = audio_data
            # 즉시 초기화하여 중복 사용 방지
            audio_data = None
        
        # 오디오 데이터가 있는 경우
        if current_audio:
            # 음성 변환 중 메시지
            print("음성 변환 중...")
            # Google STT를 사용하여 한국어 음성 인식
            text = r.recognize_google(current_audio, language="ko-KR")
            # 인식된 텍스트 출력
            print(f"인식된 텍스트: {text}")
            
            # 클립보드에 텍스트 복사 (한글 입력 지원)
            pyperclip.copy(text)
            # 0.2초 대기
            time.sleep(0.2)
            
            # 붙여넣기 (Ctrl+V) - 채팅창이 열려있어야 함
            pyautogui.hotkey('ctrl', 'v')
            # 0.3초 대기
            time.sleep(0.3)
            
            # 텍스트 입력 완료 메시지
            print("텍스트 입력 완료 - Enter를 눌러 전송하세요")
        # 오디오 데이터가 없는 경우
        else:
            # 데이터 없음 메시지
            print("녹음된 데이터가 없습니다")
    # 음성 인식 실패 예외
    except sr.UnknownValueError:
        # 인식 실패 메시지
        print("음성을 인식하지 못했습니다")
    # Google 서비스 오류 예외
    except sr.RequestError as e:
        # 서비스 오류 메시지
        print(f"Google 서비스 오류: {e}")
    # 기타 예외
    except Exception as e:
        # 오류 메시지
        print(f"오류: {e}")

# F10 키를 눌렀을 때 호출되는 함수
def on_f10_press(event):
    # 전역 변수 사용 선언
    global is_recording, recording_thread
    # 녹음 중이 아닌 경우
    if not is_recording:
        # 녹음 상태로 변경
        is_recording = True
        # 별도 스레드에서 녹음 시작
        recording_thread = threading.Thread(target=start_recording)
        # 데몬 스레드로 설정 (메인 스레드 종료시 자동 종료)
        recording_thread.daemon = True
        # 스레드 시작
        recording_thread.start()

# F10 키를 떼었을 때 호출되는 함수
def on_f10_release(event):
    # 전역 변수 사용 선언
    global is_recording
    # 녹음 중인 경우
    if is_recording:
        # 녹음 상태 해제
        is_recording = False
        # 녹음이 끝나면 변환 및 입력
        if recording_thread and recording_thread.is_alive():
            # 스레드가 끝날 때까지 대기 (최대 1초)
            recording_thread.join(timeout=1)
        # 데이터가 있는 경우에만 변환
        if audio_data is not None:
            # 변환 및 입력 함수 호출
            transcribe_and_type()
        # 데이터가 없는 경우
        else:
            # 변환 건너뜀 메시지
            print("녹음된 데이터가 없어 변환을 건너뜁니다")

# 프로그램 시작 메시지
print("마인크래프트 음성 채팅 프로그램")
print("사용 방법:")
print("1. 마인크래프트에서 채팅창 열기 (T 키)")
print("2. F10 키를 누르고 있으면 녹음 시작")
print("3. 말하기")
print("4. F10 키를 떼면 텍스트 변환 및 입력")
print("5. Enter로 전송")
print("Ctrl+C로 종료")

try:
    # F10 키 이벤트 리스너 등록 (눌렀을 때)
    keyboard.on_press_key("f10", on_f10_press)
    # F10 키 이벤트 리스너 등록 (떼었을 때)
    keyboard.on_release_key("f10", on_f10_release)
    
    # 프로그램 유지 (무한 루프)
    while True:
        # 0.1초 대기
        time.sleep(0.1)
        
# 키보드 인터럽트 예외 (Ctrl+C)
except KeyboardInterrupt:
    # 종료 메시지
    print("\n종료")
# 기타 예외
except Exception as e:
    # 오류 메시지
    print(f"오류: {e}")
# finally 블록 (무조건 실행)
finally:
    # 키보드 훅 해제
    keyboard.unhook_all()