# import re
# import time
# import pyautogui as pag
# from clients.WireType import WireType

# # exe파일 만들기
# # pyinstaller -F test.py

# # 와이어 코드명 불러오기
# Wtype = WireType()

# # 처음 켰을 때 파일 길이 확인
# date = time.strftime("%Y-%m-%d")
# fileWrite = open("C:/spmEzCut/LogMessage/%s.log" %date, "a", encoding='UTF-8')
# fileRead = open("C:/spmEzCut/LogMessage/%s.log" %date, "r", encoding='UTF-8')
# wire_num = fileRead.readlines()
# previousLogLength = len(wire_num)

# while True:
#   # 현재 시간
#   date = time.strftime("%Y-%m-%d")
#   ss_date = time.strftime("%Y%m%d")
#   ss_now = time.strftime("%H%M%S")

#   # 내 컴퓨터용 파일명
#   # fileWrite = open("C:/spmEzCut/LogMessage/2023-01-23.log", "a")
#   # fileRead = open("C:/spmEzCut/LogMessage/2023-01-23.log", "r")
#   # fileWrite.close()

#   # 광명 와이어 용 파일명
#   fileWrite = open("C:/spmEzCut/LogMessage/%s.log" %date, "a", encoding='UTF-8')
#   fileRead = open("C:/spmEzCut/LogMessage/%s.log" %date, "r", encoding='UTF-8')
#   fileWrite.close()

#   # 파일 내용 읽어오기
#   wire_num = fileRead.readlines()
#   fileRead.close()

#   # 현재 로그 파일 길이 확인
#   presentLogLength = len(wire_num)


#   # 로그파일 변경 감지
#   if presentLogLength != previousLogLength and presentLogLength != 0:

#     # 스크린샷
#     fileName = "{}{}{}{}{}{}{}".format('log_screenshots/', '%s'%Wtype.file, ' - ', ss_date[2:], '_', ss_now, '.png')
#     # pag.screenshot(fileName)
#     print(fileName)

#     # 추가된 라인
#     added_loglines = presentLogLength - previousLogLength
    
#     # 추가된 라인 살펴보며 값 반환
#     for i in range(0, added_loglines):
#       line = wire_num[len(wire_num) - 1 - i]
#       if re.search('Wire Contact Auto Stop', line):
#         print("접촉, 오토스타트")
#       elif re.search('작업중 30sec 접촉 정지', line):
#         print("접촉, 오토스타트")
#       elif re.search('작업중 M코드정지', line):
#         print("M코드 정지")
#       elif re.search('작업중 단선', line):
#         print("단선")
#       elif re.search('M20-삽입실패', line):
#         print("자동결선 Error(M20-삽입실패)")
#       elif re.search('M21-절단실패', line):
#         print("자동결선 Error(M21-절단실패)")
#       elif re.search('M21-잔여와이어 처리실패', line):
#         print("자동결선 Error(M21-잔여와이어 처리실패)")


#       elif re.search('와이어 미동작', line):
#         print("와이어 미동작")
#       elif re.search('가공액 미동작', line):
#         print("가공액 미동작")
#       elif re.search('자동결선 FEED MOTOR ALARM', line):
#         print("자동결선 FEED MOTOR ALARM")
#       elif re.search('자동결선 절단 공정 실패', line):
#         print("자동결선 절단 공정 실패")
#       elif re.search('자동결선 잔여 WIRE 처리 실패', line):
#         print("자동결선 잔여 WIRE 처리 실패")
#       elif re.search('자동결선 하부 뭉치 WIRE CONTACT', line):
#         print("자동결선 하부 뭉치 WIRE CONTACT")
#       elif re.search('AWF 명령끝날때까지 센서감지', line):
#         print("AWF 명령끝날때까지 센서감지")
#       elif re.search('Work Tank Fluid Sensor Abnormal', line):
#         print("Work Tank Fluid Sensor Abnormal")
#       elif re.search('Auto Door Sensor Abnormal', line):
#         print("Auto Door Sensor Abnormal")
#       elif re.search('Ready On', line):
#         print("Ready On")
#       elif re.search('Emergency Stop', line):
#         print("Emergency Stop")
#       elif re.search('READY Off', line):
#         print("READY Off")


#       elif re.search('작업 재시작', line):
#         print("작업 재시작")
#       elif re.search('작업 시작', line):
#         print("작업 시작")
#       elif re.search('Reset', line):
#         print("Reset")
#       elif re.search('작업 끝', line):
#         print("작업 끝")

#     # 이전 로그 파일 길이에 현재 로그 파일 길이 할당
#     previousLogLength = presentLogLength
  
#   #0.5초 마다
#   time.sleep(0.5)

import pyautogui as pag

pag.click(550, 710)