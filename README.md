# Lecture-Summarizer-AI

온라인 강의를 틀어 두면 컴퓨터에서 나오는 소리를 그대로 녹음해서 Whisper 로 받아쓰는 도구입니다.
여러 강의의 받아쓰기 결과를 하나로 합치는 기능까지 들어 있습니다.

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI_Whisper-412991?style=flat-square&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white"/>
  <img src="https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white"/>
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square"/>
</p>

> **이름과 달리 요약 기능은 아직 없습니다.**
> 저장소 이름을 지을 때는 받아쓰기 다음에 요약까지 붙일 생각이었는데 거기까지 못 갔습니다.
> 지금 들어 있는 것은 녹음, 받아쓰기, 텍스트 병합 세 가지입니다.
> 이름을 바꾸면 기존 링크가 깨져서 그대로 두고 여기에 적어 둡니다.

<br/>

## 1. 왜 만들었나

녹화 강의를 다시 들으려면 시간이 그대로 또 듭니다.
1시간짜리에서 한 문장을 찾으려고 1시간을 재생하는 게 아까웠습니다.

글로 남으면 검색으로 찾을 수 있습니다. 그래서 만들었습니다.

<br/>

## 2. 마이크가 아니라 스테레오 믹스를 쓴다

이 도구에서 제일 중요한 부분입니다.

마이크로 녹음하면 스피커에서 나온 소리를 다시 받는 셈이라 주변 소음이 섞이고,
이어폰을 쓰면 아무것도 안 잡힙니다.

**스테레오 믹스**는 컴퓨터가 재생 중인 소리를 그대로 입력으로 되돌려 주는 장치입니다.
브라우저에서 나오는 강의 소리를 손실 없이 받습니다.
윈도우가 기본으로 숨겨 놔서 따로 켜야 합니다. 아래 3번에 방법이 있습니다.

<br/>

## 3. 준비

### 파이썬

[python.org](https://www.python.org/downloads/) 에서 받습니다.
설치 화면 아래쪽 **`Add Python to PATH`** 를 반드시 체크해야 합니다.

### FFmpeg

Whisper 가 오디오를 읽는 데 필요합니다.

1. [FFmpeg Windows Builds](https://github.com/BtbN/FFmpeg-Builds/releases) 에서
   `ffmpeg-master-latest-win64-gpl-shared.zip` 을 받습니다
2. `C:\ffmpeg` 폴더를 만듭니다
3. 압축 안 `bin` 폴더의 `ffmpeg.exe`, `ffplay.exe`, `ffprobe.exe` 를 `C:\ffmpeg\bin` 에 넣습니다

### 스테레오 믹스 켜기

윈도우가 기본으로 숨겨 놔서 목록에 안 보입니다.

1. 작업표시줄 스피커 아이콘 우클릭 → **소리 설정**
2. 아래로 내려 **더 많은 소리 설정**
3. **녹음** 탭
4. 빈 공간 우클릭 → **사용할 수 없는 장치 표시** 체크
5. 나타난 **스테레오 믹스** 우클릭 → **사용**

<br/>

## 4. 실행

```bat
start_lms.bat
```

우클릭해서 **관리자 권한으로 실행**합니다.
FFmpeg 경로를 시스템에 등록하고 패키지를 설치하는 단계가 있어서 권한이 필요합니다.

메뉴가 네 개 뜹니다.

| 번호 | 하는 일 |
|---|---|
| 1 | 강의명과 녹음 시간(분)을 입력받아 녹음합니다. 끝나면 바로 받아쓸지 물어봅니다 |
| 2 | `recordings/` 에 이미 있는 wav 를 골라서 받아씁니다 |
| 3 | `transcripts/` 의 텍스트 파일을 골라 하나로 합칩니다 |
| 4 | 종료 |

녹음 시간을 안 넣으면 60분으로 잡힙니다. 파일 이름은 `20260305_1430_강의명` 형식입니다.

3번 병합은 여러 주차 강의를 한 파일로 묶을 때 씁니다.
합칠 때 `--- [Source: 파일명] ---` 구분선을 넣어서 어느 강의 내용인지 알 수 있게 했습니다.

<br/>

## 5. 구조

```
start_lms.bat        환경 설정과 실행
main.py              메뉴와 병합 기능
src/recorder.py      스테레오 믹스로 시스템 소리 녹음 (48kHz)
src/transcriber.py   Whisper 받아쓰기
recordings/          녹음된 wav (실행하면 생김)
transcripts/         변환된 텍스트 (실행하면 생김)
```

받아쓰기는 Whisper `turbo` 모델을 쓰고 언어를 한국어로 고정했습니다.
자동 감지로 두면 강의 중간의 영어 용어 때문에 언어가 바뀌는 일이 있었습니다.

<br/>

## 6. 안 되는 것

- **요약이 없습니다.** 받아쓴 원문이 그대로 나옵니다
- 윈도우 전용입니다. 스테레오 믹스가 없는 사운드 장치에서는 안 됩니다
- 긴 강의를 통으로 넘기면 느립니다. 재생 시간 기준으로 잘라서 보냈어야 했습니다
- 전공 용어를 자주 틀립니다. 과목별 용어 사전을 프롬프트에 넣었으면 나았을 것입니다
- 화면의 판서나 슬라이드는 못 읽습니다. 소리만 봅니다
- 테스트가 없습니다

<br/>

MIT License
