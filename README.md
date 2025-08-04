# YouTube Downloader & H.264 Encoder

## English Version

A Python automation tool for downloading YouTube videos and converting them to H.264 (avc1) codec.

**Premium Quality Support:**

- By using cookies from a YouTube Premium account, you can download higher-quality videos (such as 1080p and above) that are only available to Premium users.

### How It Works

1. **Cookie Generation with Selenium**
   - The script launches a headless Chrome browser, logs into YouTube, and saves your session cookies (including Premium access if logged in).
2. **Video Download with yt-dlp**
   - yt-dlp uses the saved cookies to access and download the highest quality video and audio streams available to your account (including Premium-only qualities).
   - Downloads H.264 (avc1) video and AAC audio, up to 1080p or higher if available.
3. **Merging with ffmpeg**
   - Video and audio streams are merged into a single MP4 file using ffmpeg.
4. **(Optional) Re-encoding**
   - You can further re-encode the MP4 file to H.264 or other codecs using the provided script and ffmpeg options.

### Features

- **YouTube Video Download**
  - Automatically logs in to YouTube using Selenium (cookie generation)
  - **Downloads high-quality videos available only to YouTube Premium users by using your account cookies**
  - Downloads up to 1080p high-quality videos with H.264 (avc1) video and AAC audio using yt-dlp
  - **Automatically saves files with YouTube video title as filename**
  - Merges video and audio into mp4 (requires ffmpeg)
- **MP4 H.264 Encoding**
  - Re-encodes large MP4 files to H.264 + AAC using ffmpeg
  - Supports faststart option for streaming optimization

### Installation

1. Requires Python 3.7 or higher
2. Install required packages:
   ```bash
   pip install selenium webdriver-manager yt-dlp
   ```
3. Install ffmpeg
   - **macOS:**
     ```bash
     brew install ffmpeg
     ```
   - **Windows:**
     1. Download the Windows zip from [ffmpeg official site](https://ffmpeg.org/download.html)
     2. Extract and add the `bin` folder path (e.g., `C:\ffmpeg\bin`) to your system `PATH`
     3. Check installation with `ffmpeg -version` in Command Prompt

### Usage

#### 1. Download YouTube Video

Edit the URL in `index.py`:

```python
url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'
```

Run:

```bash
python3 index.py
```

- The file will be saved with the YouTube video title as the filename in the current folder.
- The video will be downloaded with H.264 (avc1) codec automatically.
- **If you are a YouTube Premium user, the script will use your cookies to access and download higher-quality videos only available to Premium accounts.**

#### 2. Re-encode MP4 to H.264

Use `encodIng.py` to convert an existing MP4 file to H.264:

```python
input_file = "YouTube_Video_Title.mp4"    # Downloaded file name (YouTube title)
output_file = "encoded_YouTube_Video_Title.mp4"  # Output file name
encoding(input_file, output_file, crf=23, preset="fast")
```

Run:

```bash
python3 encodIng.py
```

##### Encoding Options

- `crf`: Quality (lower is higher quality, recommended 18~28)
- `preset`: Encoding speed (`ultrafast`, `fast`, `medium`, ...)

### Notes

- **Disk Space:** Ensure enough space for large video downloads.
- **ffmpeg Required:** Merging and encoding require ffmpeg.
- **YouTube Policy:** Use downloaded videos in compliance with YouTube's policy.

---

# YouTube Downloader & H.264 Encoder

유튜브 영상을 자동으로 다운로드하고, H.264 (avc1) 코덱으로 변환하는 Python 자동화 도구입니다.

**프리미엄 고화질 지원:**

- 유튜브 프리미엄 계정의 쿠키를 활용하여, 프리미엄 사용자만 볼 수 있는 고화질(1080p 이상) 영상을 다운로드할 수 있습니다.

### 실제 작동 흐름

1. **Selenium으로 쿠키 생성**
   - 스크립트가 크롬 브라우저를 헤드리스 모드로 실행하여 유튜브에 로그인하고, 세션 쿠키(프리미엄 권한 포함)를 저장합니다.
2. **yt-dlp로 영상 다운로드**
   - 저장된 쿠키를 활용해 yt-dlp가 계정이 접근 가능한 최고 화질(프리미엄 전용 포함)의 비디오/오디오 스트림을 다운로드합니다.
   - H.264(avc1) 비디오와 AAC 오디오, 최대 1080p(또는 그 이상)를 다운로드합니다.
3. **ffmpeg로 병합**
   - 다운로드한 비디오/오디오 스트림을 ffmpeg로 하나의 MP4 파일로 병합합니다.
4. **(선택) 재인코딩**
   - 제공된 스크립트와 ffmpeg 옵션을 활용해 MP4 파일을 H.264 또는 다른 코덱으로 재인코딩할 수 있습니다.

## 주요 기능

- **유튜브 영상 다운로드**
  - Selenium을 이용해 YouTube에 자동 로그인(쿠키 생성)
  - **프리미엄 계정 쿠키를 활용해 프리미엄 전용 고화질 영상 다운로드 가능**
  - yt-dlp로 1080p 이하 고화질, H.264(avc1) 비디오와 AAC 오디오만 다운로드
  - **유튜브 영상 제목을 파일명으로 자동 저장**
  - 영상과 오디오를 mp4로 병합 (ffmpeg 필요)
- **MP4 H.264 인코딩**
  - ffmpeg를 이용해 대용량 MP4 파일을 H.264 + AAC로 재인코딩
  - 스트리밍에 최적화된 faststart 옵션 지원

## 설치 방법

1. Python 3.7 이상 필요
2. 필수 패키지 설치
   ```bash
   pip install selenium webdriver-manager yt-dlp
   ```
3. ffmpeg 설치 (Mac 기준)

   ```bash
   brew install ffmpeg
   ```

   **Windows:**

   1. [ffmpeg 공식 다운로드 페이지](https://ffmpeg.org/download.html)에서 Windows용 zip 파일을 받으세요.
   2. 압축을 해제하고, `bin` 폴더 경로(예: `C:\ffmpeg\bin`)를 환경 변수 `PATH`에 추가하세요.
   3. 명령 프롬프트에서 `ffmpeg -version` 명령으로 설치를 확인하세요.

## 사용법

### 1. 유튜브 영상 다운로드

`index.py` 파일에서 다운로드할 유튜브 영상 URL을 수정하세요.

```python
url = 'https://www.youtube.com/watch?v=영상ID'
```

실행:

```bash
python3 index.py
```

- 실행하면 유튜브 영상 제목으로 된 파일이 현재 폴더에 저장됩니다.
- 자동으로 H.264(avc1) 코덱으로 다운로드됩니다.
- **프리미엄 계정의 쿠키를 활용해 프리미엄 전용 고화질 영상도 다운로드할 수 있습니다.**

### 2. MP4 파일 H.264로 재인코딩

`encodIng.py`를 사용해 이미 있는 MP4 파일을 H.264로 변환할 수 있습니다.

```python
# encodIng.py 예시
input_file = "유튜브_영상_제목.mp4"      # 다운로드된 파일명 (유튜브 제목)
output_file = "encoded_유튜브_영상_제목.mp4"  # 변환 후 파일명
encoding(input_file, output_file, crf=23, preset="fast")
```

실행:

```bash
python3 encodIng.py
```

#### 인코딩 옵션

- `crf`: 화질(낮을수록 고화질, 18~28 권장)
- `preset`: 인코딩 속도 (`ultrafast`, `fast`, `medium`, ...)

## 주의사항

- **디스크 공간**: 대용량 영상 다운로드 시 충분한 저장 공간이 필요합니다.
- **ffmpeg 필수**: 병합 및 인코딩에 ffmpeg가 필요합니다.
- **YouTube 정책**: 다운로드한 영상의 사용은 YouTube 정책을 준수해야 합니다.

## 라이선스

MIT License
