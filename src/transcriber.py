import whisper
import os

def transcribe_audio(audio_path, output_text_path):
    if not os.path.exists(audio_path):
        print(f"❌ File not found: {audio_path}")
        return False

    print(f"\n🤖 AI Processing: {os.path.basename(audio_path)}")
    print("-" * 50)
    
    # 'turbo' 모델 사용 및 실시간 출력(verbose) 활성화
    model = whisper.load_model("turbo")
    result = model.transcribe(audio_path, language="ko", verbose=True)
    
    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print("-" * 50)
    print(f"✅ Success: {output_text_path}")
    return True