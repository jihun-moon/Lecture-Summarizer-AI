import soundcard as sc
import soundfile as sf
import numpy as np
import time
from tqdm import tqdm

def record_system_audio(output_path, duration_minutes=60, sample_rate=48000):
    speaker = sc.default_speaker()
    mic = sc.get_microphone(speaker.name, include_loopback=True)
    
    total_seconds = int(duration_minutes * 60)
    total_frames = total_seconds * sample_rate
    chunk_size = sample_rate * 2  # 2초 단위 처리로 오차 최소화
    
    print(f"\n🎧 Speaker: {speaker.name}")
    frames = []
    
    # tqdm 기반 실시간 진행바
    with tqdm(total=total_seconds, unit="sec", desc="⏺️  Recording") as pbar:
        try:
            with mic.recorder(samplerate=sample_rate) as recorder:
                recorded_frames = 0
                while recorded_frames < total_frames:
                    to_record = min(chunk_size, total_frames - recorded_frames)
                    data = recorder.record(numframes=to_record)
                    frames.append(data)
                    recorded_frames += to_record
                    pbar.update(to_record / sample_rate)
        except KeyboardInterrupt:
            print("\n⏹️ Recording stopped by user.")

    if frames:
        recorded_data = np.concatenate(frames, axis=0)
        sf.write(output_path, recorded_data, sample_rate)
        return True
    return False