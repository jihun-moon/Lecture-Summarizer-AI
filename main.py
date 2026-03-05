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
    print("3. 📂  Merge Transcripts (텍스트 파일 합치기) ✨") # 신규 추가
    print("4. ❌  Exit (종료)")
    print("="*40)
    return input("👉 Choice (1-4): ")

def merge_transcripts():
    """transcripts 폴더 내의 텍스트 파일들을 하나로 병합"""
    files = sorted([f for f in os.listdir("transcripts") if f.endswith(".txt")])
    if not files:
        print("\n⚠️ 'transcripts/' 폴더에 합칠 파일이 없습니다.")
        return

    print("\n📂 Available Transcripts:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    selection = input("\n🔢 합칠 번호들을 순서대로 입력 (예: 1,2,3,4) 또는 'all': ").strip()
    
    to_merge = []
    if selection.lower() == 'all':
        to_merge = files
    else:
        try:
            indices = [int(x.strip()) for x in selection.split(',')]
            to_merge = [files[i-1] for i in indices if 1 <= i <= len(files)]
        except:
            print("❌ 잘못된 입력입니다.")
            return

    if not to_merge: return

    merged_name = input("📝 저장할 새 파일 이름 (확장자 제외): ").strip() or "combined_transcript"
    output_path = f"transcripts/{merged_name}.txt"

    with open(output_path, "w", encoding="utf-8") as outfile:
        for fname in to_merge:
            fpath = os.path.join("transcripts", fname)
            with open(fpath, "r", encoding="utf-8") as infile:
                outfile.write(f"\n--- [Source: {fname}] ---\n") # 구분선 추가
                outfile.write(infile.read())
                outfile.write("\n\n")

    print(f"✅ 병합 완료: {output_path}")

def get_existing_files():
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
            try:
                duration = int(input("⏱️ Duration (min): ") or 60)
            except ValueError:
                duration = 60
            
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

        elif choice == '3': # 병합 기능 연결
            merge_transcripts()

        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)