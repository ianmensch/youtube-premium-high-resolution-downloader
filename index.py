import shutil
import sys

import yt_dlp

# 유튜브 영상 URL (Chrome에서 youtube.com 로그인 권장)
url = 'https://www.youtube.com/watch?v=O1d2DYZZrek&list=RDGMEM0s70dY0AfCwh3LqQ-Bv1xgVMO1d2DYZZrek&start_radio=1'  # <- 여기에 영상 링크

# yt-dlp 2026.x: YouTube는 EJS(외부 JS 런타임)로 챌린지를 풀어야 함. pip: pip install -U "yt-dlp[default]"
# Deno 2+ 권장; 없으면 Node 20+ 사용: https://github.com/yt-dlp/yt-dlp/wiki/EJS
js_runtimes = {}
if shutil.which('deno'):
    js_runtimes['deno'] = {}
if shutil.which('node'):
    js_runtimes['node'] = {}
if not js_runtimes:
    print(
        '오류: Deno 2+ 또는 Node.js 20+ 이 PATH에 없습니다. '
        'YouTube 다운로드에 필요합니다.\n'
        '설치: https://github.com/yt-dlp/yt-dlp/wiki/EJS\n'
        '의존성: pip install -U "yt-dlp[default]"  (yt-dlp-ejs 포함)',
        file=sys.stderr,
    )
    sys.exit(1)


def _print_format_diagnosis(info: dict) -> None:
    """로그인 쿠키로 열린 포맷 목록에서 Premium 표시·최대 해상도를 요약한다."""
    formats = info.get('formats')
    if not formats:
        print('[진단] 추출된 포맷 목록이 없습니다.')
        return

    vfmt = [
        f
        for f in formats
        if f.get('height') and f.get('vcodec') not in (None, 'none')
    ]
    if not vfmt:
        print('[진단] 비디오 스트림 포맷이 없습니다.')
        return

    max_h = max(f['height'] for f in vfmt)
    premium = [f for f in vfmt if 'Premium' in (f.get('format_note') or '')]

    print(f'[진단] 이 세션에서 보이는 비디오 최대 세로 해상도: {max_h}p')
    if premium:
        ph = max(f['height'] for f in premium)
        print(
            f'[진단] format_note에 "Premium"이 붙은 스트림 {len(premium)}개 '
            f'(그중 최대 {ph}p). Premium 구독 세션에서만 나오는 고화질 후보가 잡힌 상태입니다.'
        )
    else:
        print(
            '[진단] "Premium" 표시 스트림 없음. '
            '일반 해상도만 제공되거나, 이 영상/계정에서는 extractor에 Premium 라벨이 안 붙을 수 있습니다.'
        )

    vfmt.sort(
        key=lambda f: (f.get('height') or 0, f.get('tbr') or 0, f.get('fps') or 0),
        reverse=True,
    )
    print('[진단] 화질 상위 후보 (최대 5개):')
    for f in vfmt[:5]:
        note = (f.get('format_note') or '').strip() or '(비고 없음)'
        print(
            f"  - {f.get('height')}p  id={f.get('format_id')}  "
            f"{f.get('ext')}  {note}"
        )


ydl_opts = {
    'cookiesfrombrowser': ('chrome',),
    'noplaylist': True,
    'js_runtimes': js_runtimes,
    # yt-dlp가 source_preference 등으로 정렬할 때 Premium 변형이 위로 올라오는 경우가 많음
    'format': 'bestvideo*+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
}

try:
    print(
        '세션 확인 및 다운로드… (쿠키: Chrome, EJS: '
        + ', '.join(js_runtimes.keys())
        + ')'
    )
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        _print_format_diagnosis(info)
        print('다운로드 시작…')
        ydl.process_info(info)
    print('다운로드 완료')
except Exception as e:
    print(f'오류가 발생했습니다: {str(e)}')
    sys.exit(1)
