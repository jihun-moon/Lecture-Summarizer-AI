## 🎓 Lecture-Summarizer-AI (LMS 강의 자동 요약기)

> **실시간 시스템 사운드 캡처와 OpenAI Whisper AI를 활용한 스마트 강의 노트 생성 도구**

본 프로젝트는 다운로드가 제한된 LMS 강의를 실시간으로 녹음하고, AI를 통해 텍스트로 변환하여 학습 효율을 극대화하기 위해 개발되었습니다.

---

### ✨ 주요 기능 (Key Features)

* **루프백 녹음 (Loopback Recording)**: 별도의 장치 없이 스피커로 나가는 시스템 사운드를 직접 캡처합니다.
* **AI 자동 받아쓰기**: OpenAI의 Whisper 모델을 사용하여 높은 정확도로 강의 내용을 텍스트화합니다.
* **원클릭 자동 세팅**: `start_lms.bat` 파일을 통해 환경 변수 등록, 가상환경 구축, 라이브러리 설치를 한 번에 해결합니다.
* **체계적인 파일 관리**: 녹음본과 변환된 텍스트를 날짜별/강의별로 자동 분류하여 저장합니다.

---

### 🛠️ 사전 준비 (Prerequisites)

다른 사용자가 실행하기 전 반드시 확인해야 할 사항입니다.

1. **Python 3.8 이상**이 설치되어 있어야 합니다.
2. **FFmpeg 설치**:
* [FFmpeg 공식 사이트](https://ffmpeg.org/download.html)에서 다운로드합니다.
* **`C:\ffmpeg\bin`** 경로를 생성하고 그 안에 `ffmpeg.exe`를 넣어야 합니다. (프로그램 실행 시 자동으로 시스템 변수에 등록됩니다.)


3. **스테레오 믹스 활성화**:
* 윈도우 소리 설정에서 '스테레오 믹스' 장치를 **[사용함]**으로 설정해야 소리가 녹음됩니다.



---

### 🚀 시작하기 (Getting Started)

#### 방법 1: 자동 실행 (추천 - Windows 전용)

1. 레포지토리를 클론하거나 다운로드합니다.
2. **`start_lms.bat`** 파일을 마우스 우클릭하여 **[관리자 권한으로 실행]**합니다.
3. 터미널의 안내에 따라 강의명과 시간을 입력합니다.

#### 방법 2: 수동 실행 (개발자용)

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python main.py

```

---

### 📂 프로젝트 구조 (Project Structure)

```text
.
├── main.py              # 프로그램 제어 및 진입점
├── recorder.py          # 시스템 사운드 녹음 로직
├── transcriber.py       # Whisper AI 변환 로직
├── start_lms.bat        # 원클릭 자동 설정 및 실행 스크립트
├── requirements.txt     # 필요 라이브러리 목록
├── recordings/          # 녹음된 .wav 파일 저장소
└── transcripts/         # 변환된 .txt 강의 노트 저장소

```

---

### ⚠️ 주의 사항 (Troubleshooting)

* **소리가 녹음되지 않음**: 스피커 소리가 너무 작거나 '스테레오 믹스'가 꺼져 있는지 확인하세요.
* **FFmpeg 에러**: `C:\ffmpeg\bin` 경로가 정확한지, 관리자 권한으로 배치를 실행했는지 확인하세요.
* **변환 속도**: Whisper 모델은 성능에 따라 시간이 소요될 수 있습니다. (첫 실행 시 모델 다운로드 필요).

---

### 👤 Author

* **Jihun Moon** - Computer Software Student
* GitHub: [@jihun-moon](https://www.google.com/search?q=https://github.com/jihun-moon)

---
