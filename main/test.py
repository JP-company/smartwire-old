import time
import pyautogui as pag
from clients.WireType import WireType

# exe파일 만들기
# pyinstaller -F test.py

# 와이어 코드명 불러오기
Wtype = WireType()

# 이전 로그 파일 길이
previous_log_length = 0

while True:
    # 현재 시간
    date = time.strftime("%Y-%m-%d")
    ss_date = time.strftime("%Y%m%d")
    ss_now = time.strftime("%H%M%S")

    # 내 컴퓨터용 파일명
    # file_read = open("C:/spmEzCut/LogMessage/log_2/%s.log" %date, "r")

    # 광명 와이어 용 파일명
    file_read = open("C:/spmEzCut/LogMessage/%s.log" %date, "r")

    # 파일 내용 읽어오기
    wire_num = file_read.readlines()

    # 현재 로그 파일 길이 확인
    present_log_length = len(wire_num)

    # 길이가 달라졌으면
    if present_log_length != previous_log_length:

        # 스크린샷
        fileName = "{}{}{}{}{}{}{}".format('log_screenshots/', '%s'%Wtype.file, ' - ', ss_date[2:], '_', ss_now, '.png')
        pag.screenshot(fileName)

        print(fileName)

        # 이전 로그 파일 길이에 현재 로그 파일 길이 할당
        previous_log_length = present_log_length
    
    #0.5초 마다
    time.sleep(0.5)