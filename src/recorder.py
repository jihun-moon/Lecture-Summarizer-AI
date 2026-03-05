import soundcard as sc
import soundfile as sf
import numpy as np
import time

def record_system_audio(output_path, duration_minutes=60, sample_rate=48000):
    speaker = sc.default_speaker()
    # 루프백(Loopback) 마이크 활성화 (스피커 소리 가로채기)
    mic = sc.get_microphone(speaker.name, include_loopback=True)
    
    print(f"🎙️ 녹음 시작: {speaker.name}")
    print("🛑 중단하려면 Ctrl + C를 누르세요.")

    frames = []
    try:
        with mic.recorder(samplerate=sample_rate) as recorder:
            start_time = time.time()
            # 1초 단위로 데이터를 읽어와 리스트에 추가
            while time.time() - start_time < (duration_minutes * 60):
                data = recorder.record(numframes=sample_rate)
                frames.append(data)
    except KeyboardInterrupt:
        print("\n⏹️ 사용자에 의해 녹음이 중단되었습니다.")
    
    # 데이터 병합 및 저장
    if frames:
        recorded_data = np.concatenate(frames, axis=0)
        sf.write(output_path, recorded_data, sample_rate)
        print(f"💾 파일 저장 완료: {output_path}")
        return True
    return False