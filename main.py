import os
from datetime import datetime
from src.recorder import record_system_audio
from src.transcriber import transcribe_audio

def main():
    # 1. 환경 설정
    os.makedirs("recordings", exist_ok=True)
    os.makedirs("transcripts", exist_ok=True)

    # 2. 강의 정보 입력
    lecture_name = input("📌 강의명을 입력하세요 (예: 자료구조_01): ") or "lecture"
    duration = int(input("⏱️ 녹음할 시간(분)을 입력하세요: ") or 60)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    audio_file = f"recordings/{timestamp}_{lecture_name}.wav"
    text_file = f"transcripts/{timestamp}_{lecture_name}.txt"

    # 3. 프로세스 실행
    success = record_system_audio(audio_file, duration_minutes=duration)
    
    if success:
        print("\n" + "="*30)
        print("🚀 바로 텍스트 변환을 시작할까요? (y/n)")
        choice = input().lower()
        if choice == 'y':
            transcribe_audio(audio_file, text_file)
            print("✨ 모든 작업이 끝났습니다!")

if __name__ == "__main__":
    main()