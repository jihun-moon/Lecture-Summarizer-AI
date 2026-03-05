import os
import sys
from datetime import datetime
from src.recorder import record_system_audio
from src.transcriber import transcribe_audio

def show_menu():
    print("\n" + "="*40)
    print("🎓  LMS LECTURE ASSISTANT v2.0")
    print("="*40)
    print("1. 🎙️  Start New Recording (녹음 후 변환)")
    print("2. 📝  Transcribe Existing File (기존 파일 변환)")
    print("3. ❌  Exit (종료)")
    print("="*40)
    return input("👉 Choice (1-3): ")

def get_existing_files():
    # recordings 폴더 내 .wav 파일 목록 추출
    files = [f for f in os.listdir("recordings") if f.endswith(".wav")]
    if not files:
        print("\n⚠️ No recording files found in 'recordings/' folder.")
        return None
    
    print("\n📂 Available Recordings:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")
    
    choice = input("\n🔢 Select file number (or 'q' to cancel): ")
    if choice.isdigit() and 1 <= int(choice) <= len(files):
        return os.path.join("recordings", files[int(choice)-1])
    return None

def main():
    os.makedirs("recordings", exist_ok=True)
    os.makedirs("transcripts", exist_ok=True)

    while True:
        choice = show_menu()

        if choice == '1':
            name = input("📌 Lecture Name: ").strip() or "lecture"
            duration = int(input("⏱️ Duration (min): ") or 60)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            audio_path = f"recordings/{timestamp}_{name}.wav"
            
            if record_system_audio(audio_path, duration):
                convert = input("\n🚀 Transcribe right now? (y/n): ").lower()
                if convert == 'y':
                    text_path = f"transcripts/{timestamp}_{name}.txt"
                    transcribe_audio(audio_path, text_path)

        elif choice == '2':
            audio_path = get_existing_files()
            if audio_path:
                name = os.path.splitext(os.path.basename(audio_path))[0]
                text_path = f"transcripts/{name}.txt"
                transcribe_audio(audio_path, text_path)

        elif choice == '3':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)