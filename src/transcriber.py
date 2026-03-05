import whisper
import os

def transcribe_audio(audio_path, output_text_path):
    if not os.path.exists(audio_path):
        print("❌ 변환할 오디오 파일이 없습니다.")
        return

    print("🤖 AI가 음성을 텍스트로 변환 중입니다... (사양에 따라 시간이 소요될 수 있습니다)")
    
    # 모델 로드 (성능과 속도의 균형이 좋은 'turbo' 추천)
    model = whisper.load_model("turbo")
    result = model.transcribe(audio_path, language="ko")
    
    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"✅ 변환 완료: {output_text_path}")