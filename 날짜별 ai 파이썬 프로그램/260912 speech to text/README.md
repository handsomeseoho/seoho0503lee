# 한국어 실시간 STT (Speech-to-Text) 프로그램

Google Web Speech API를 사용한 무료 한국어 실시간 음성 인식 프로그램입니다. 마이크로 말하면 실시간으로 텍스트로 변환됩니다. API 키 없이 사용 가능합니다.

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

## 사용 방법

### 실시간 마이크 음성 인식
```bash
python stt_korean.py
```

### 종료 방법
- `Ctrl+C`로 종료

## 출력

- 실시간으로 인식된 텍스트가 콘솔에 출력됨
- 말할 때마다 결과가 즉시 표시됨

## 요구사항

- Python 3.8+
- 마이크 (내장 또는 외장)
- **인터넷 연결**: Google Web Speech API 사용을 위해 필요
- PortAudio (pyaudio 의존성):
  - Windows: 자동 설치됨
  - Mac: `brew install portaudio`
  - Linux: `sudo apt install portaudio19-dev`

## 특징

- **완전 무료**: API 키 불필요
- **모델 다운로드 불필요**: 별도의 모델 파일 필요 없음
- **실시간 인식**: 말하는 즉시 텍스트 변환
- **한국어 지원**: 한국어 음성 인식 지원
- **간단한 설치**: 패키지만 설치하면 바로 사용 가능
- **높은 정확도**: Google의 강력한 STT 엔진 사용

## 주의사항

- 인터넷 연결이 필수입니다
- 네트워크 상태에 따라 응답 속도가 달라질 수 있습니다
- 무료 사용량 제한이 있을 수 있습니다 (Google 정책에 따름)
