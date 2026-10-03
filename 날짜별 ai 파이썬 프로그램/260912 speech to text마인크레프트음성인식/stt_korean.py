import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("말하세요... (Ctrl+C로 종료)")
        
        while True:
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                text = r.recognize_google(audio, language="ko-KR")
                print(text)
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"Google 서비스 오류: {e}")
                break
                
except KeyboardInterrupt:
    print("\n종료")
except Exception as e:
    print(f"오류: {e}")
