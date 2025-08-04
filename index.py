from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import yt_dlp
import sys
import os

# 유튜브 영상 URL 입력
url = 'https://www.youtube.com/watch?v=TARGET_VIDEO_ID'  # <- 여기에 영상 링크

try:
    # Chrome 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않음
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Chrome 드라이버 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # YouTube 페이지 접속
    print("YouTube 페이지 접속 중...")
    driver.get(url)
    time.sleep(5)  # 페이지 로딩 대기
    
    # 쿠키 가져오기
    cookies = driver.get_cookies()
    
    # 쿠키 파일 생성 (Netscape 형식)
    cookies_file = 'youtube_cookies.txt'
    with open(cookies_file, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# https://curl.haxx.se/rfc/cookie_spec.html\n")
        f.write("# This is a generated file! Do not edit.\n\n")
        for cookie in cookies:
            secure = "TRUE" if cookie.get('secure') else "FALSE"
            http_only = "TRUE" if cookie.get('httpOnly') else "FALSE"
            expires = str(int(cookie.get('expiry', 0))) if cookie.get('expiry') else "0"
            f.write(f"{cookie['domain']}\tTRUE\t{cookie['path']}\t{secure}\t{expires}\t{cookie['name']}\t{cookie['value']}\n")
    
    # 브라우저 종료
    driver.quit()
    
    # yt-dlp 옵션 설정 (고화질 + 쿠키 사용)
    ydl_opts = {
        'cookiefile': cookies_file,
        'format': 'bestvideo[height<=1080][vcodec^=avc1]+bestaudio[acodec^=mp4a]/best[height<=1080][vcodec^=avc1]',  # h264(avc1) 코덱 지정
        'outtmpl': '%(title)s.%(ext)s',  # 유튜브 제목으로 파일명 설정
        'merge_output_format': 'mp4',
    }
    
    # 다운로드 시작
    print("다운로드 시작...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # 쿠키 파일 삭제
    os.remove(cookies_file)
    
    print("다운로드 완료")
except Exception as e:
    print(f"오류가 발생했습니다: {str(e)}")
    sys.exit(1)
