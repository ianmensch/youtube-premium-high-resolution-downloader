import subprocess
import os

def encoding(input_path, output_path, crf=23, preset="medium"):
    """
    대용량 MP4 파일을 H.264 + MP4 포맷으로 인코딩한다.

    :param input_path: 원본 파일 경로
    :param output_path: 인코딩된 파일 저장 경로
    :param crf: Constant Rate Factor (화질 설정, 낮을수록 고화질, 보통 18~28)
    :param preset: 인코딩 속도 설정 (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)

    # ===== 비디오 코덱 옵션 =====
    # -c:v libx264 : H.264(AVC) 코덱, 윈도우/맥/리눅스 모두 호환성 매우 높음 (권장)
    # -c:v libx265 : H.265(HEVC) 코덱, 더 높은 압축률(파일 용량↓), 단 일부 구형 기기/플레이어에서 재생 불가
    # -c:v mpeg4   : MPEG-4 Part 2, 구형 기기 호환성↑, 화질/압축률은 H.264보다 떨어짐
    #
    # ===== 오디오 코덱 옵션 =====
    # -c:a aac         : AAC(권장, mp4 표준)
    # -c:a libmp3lame  : MP3(일부 구형 기기 호환↑, mp4 컨테이너에서 비권장)
    #
    # ===== 유용한 ffmpeg 옵션 =====
    # -crf [18~28]     : 화질/용량 조절(낮을수록 고화질, 23 기본)
    # -preset [ultrafast~veryslow] : 인코딩 속도/압축률 트레이드오프
    # -movflags +faststart : 스트리밍/웹 재생 최적화(권장)
    # -vf scale=1280:720 : 해상도 강제 변환(예시)
    # -b:v 2M        : 비디오 비트레이트 직접 지정(권장X, crf와 동시 사용 비권장)
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"입력 파일이 존재하지 않습니다: {input_path}")

    command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libx264",  # 비디오 코덱: libx264(H.264)
        "-preset", preset,
        "-crf", str(crf),
        "-c:a", "aac",      # 오디오 코덱: AAC
        "-b:a", "192k",
        "-movflags", "+faststart",  # 스트리밍 최적화
        # "-vf", "scale=1280:720",  # 해상도 변환 예시(주석 해제시 적용)
        output_path
    ]

    print("실행할 명령어:", " ".join(command))
    subprocess.run(command, check=True)
    print("인코딩 완료:", output_path)

# 사용 예시
if __name__ == "__main__":
    # 다운로드된 유튜브 영상 파일명 (제목으로 저장됨)
    input_file = "다운로드된_유튜브_제목.mp4"  # 실제 다운로드된 파일명으로 변경
    output_file = "encoded_" + input_file
    
    # encoding(input_file, output_file, crf=23, preset="fast")
    #
    # ===== 다른 코덱/옵션 예시 =====
    # H.265(HEVC)로 인코딩 (파일 용량↓, 최신 기기 권장)
    # command에서 "-c:v", "libx265"로 변경
    #
    # MPEG-4로 인코딩 (구형 기기 호환↑)
    # command에서 "-c:v", "mpeg4"로 변경
    #
    # 오디오를 MP3로 인코딩 (mp4 컨테이너에서는 권장X)
    # command에서 "-c:a", "libmp3lame"로 변경
    #
    # 해상도 강제 변환(720p)
    # command에 "-vf", "scale=1280:720" 추가
    
    print(f"사용법: encoding('{input_file}', '{output_file}', crf=23, preset='fast')")
    print("실제 파일명으로 변경한 후 주석을 해제하고 실행하세요.")
