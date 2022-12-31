from firebase_admin import credentials
import firebase_admin
from PIL import Image
import time
import pyautogui as pag
from clients.Identifier import Identifier
from clients.FirebaseServer import FirebaseServer

# exe 변환 명령어
# pyinstaller -F --icon=.\wire.ico wire.py

# firebase 계정 연결
cred = credentials.Certificate('./serviceAccount.json')
firebase_admin.initialize_app(cred)

# 가동 상태 식별자 객체 생성
idf = Identifier()

# 파이어베이스 서버 연결 객체 생성
fbsvr = FirebaseServer()

# FirebaseServer의 Wtype 객체 주소 할당
Wtype = fbsvr.Wtype

def five_min_stop(): # 5분 정지 감지 타이머
    time.sleep(1)
    for i in range(14):
        if idf.referee(Wtype.model, "start") != "start":
            time.sleep(1)

def firststop(): #첫 멈춤
    if idf.referee(Wtype.model, "uncut") == "uncut": # 줄 씹힘
        fbsvr.firebase('uncut', '와이어 선 씹힘')
    elif idf.referee(Wtype.model, "nowire") == "nowire": # 와이어 선 부족
        fbsvr.firebase('nowire', '와이어 선 부족')
    elif idf.referee(Wtype.model, "finished") == "finished": # 작업완료
        fbsvr.firebase('finished', '작업 종료')
    elif idf.referee(Wtype.model, "contact") == "contact": # 와이어 선 접촉
        fbsvr.firebase('contact', '와이어 선 접촉')
    elif idf.referee(Wtype.model, "pause") == "pause": # 와이어 미동작
        pag.click(680, 430)
        time.sleep(1)
        pag.click(550, 720)
        fbsvr.firebase('pause', '와이어 미동작')
    elif idf.referee(Wtype.model, "moff") == "moff": # M코드 정지
        fbsvr.firebase('moff', 'M코드 정지')
    elif idf.referee(Wtype.model, 'start') == "stop": # 가동 정지
        fbsvr.firebase('off', '가공 정지')

def auto_start(): # 자동 재시작
    pag.screenshot('wire.png', region=(607, 76, 73, 26))
    img = Image.open('wire.png')
    # num = list(pytesseract.image_to_string(img))
    # real_num = num[2] + num[3] + num[4] + num[5] + num[6]

    pag.click(793, 125) # 1. NC 편집 클릭
    time.sleep(0.5)

    pag.rightClick(940, 245) # 2. 줄에서 1~2개 위에 우클릭 
    time.sleep(0.5)

    pag.click(1000, 300) # 3. 셋 점프 라인
    time.sleep(0.5)

    pag.click(772, 720) # 스타트
    time.sleep(300)

    pag.click(772, 720) # 다시 스타트

# 예기치 못한 프로그램 종료 시 수행
# atexit.register(fbsvr.exit_handler())


print("-------와이어 알림 프로그램 시작-------")
# time.sleep(10)

if idf.referee(Wtype.model, 'start') == "start": # 가동중일때
    while True:
        while True:
            time.sleep(10)
            if idf.referee(Wtype.model, 'start') == "start": # 최초 초록불 확인, 퇴근 후
                fbsvr.firebase('on', '가공 시작')
                break
        while True:
            time.sleep(10)
            if idf.referee(Wtype.model, 'start') != "start": # 최초 회색불 감지, 퇴근 후
                five_min_stop() # 5분 동안 20초 간격으로 회색불 확인
                if idf.referee(Wtype.model, "uncut") == "uncut": # 줄 씹힘
                    fbsvr.firebase('uncut', '와이어 선 씹힘')
                    break
                elif idf.referee(Wtype.model, "nowire") == "nowire": # 와이어 선 부족
                    fbsvr.firebase('nowire', '와이어 선 부족')
                    break
                elif idf.referee(Wtype.model, "finished") == "finished": # 작업종료
                    fbsvr.firebase('finished', '작업 종료')
                    break
                elif idf.referee(Wtype.model, "contact") == "contact": # 와이어 선 접촉
                    fbsvr.firebase('contact', '와이어 선 접촉')
                    break
                elif idf.referee(Wtype.model, "moff") == "moff": # M코드 정지
                    fbsvr.firebase('moff', 'M코드 정지')
                    break
                elif idf.referee(Wtype.model, "pause") == "pause": # 와이어 미동작
                    pag.click(680, 430)
                    time.sleep(1)
                    pag.click(550, 720)
                    fbsvr.firebase('pause', '와이어 미동작')
                    break
                elif idf.referee(Wtype.model, 'start') == "stop": # 와이어 줄 연결 실패
                    fbsvr.firebase('off', '가공 정지')
                    break
else: # 멈춰있을때
    date=time.strftime("%Y-%m-%d")
    now=time.strftime("%H:%M:%S")
    firststop()
    while True:
        while True:
            if idf.referee(Wtype.model, 'start') == "start": # 최초 초록불 확인, 퇴근 후
                time.sleep(10)
                fbsvr.firebase('on', '가공 시작')
                break
        while True:
            if idf.referee(Wtype.model, 'start') != "start": # 최초 회색불 감지, 퇴근 후
                time.sleep(10)
                five_min_stop() # 5분 동안 20초 간격으로 회색불 확인
                if idf.referee(Wtype.model, "uncut") == "uncut": # 줄 씹힘
                    fbsvr.firebase('uncut', '와이어 선 씹힘')
                    break
                elif idf.referee(Wtype.model, "nowire") == "nowire": # 와이어 선 부족
                    fbsvr.firebase('nowire', '와이어 선 부족')
                    break
                elif idf.referee(Wtype.model, "finished") == "finished": # 작업종료
                    fbsvr.firebase('finished', '작업 종료')
                    break
                elif idf.referee(Wtype.model, "contact") == "contact": # 와이어 선 접촉
                    fbsvr.firebase('contact', '와이어 선 접촉')
                    break
                elif idf.referee(Wtype.model, "moff") == "moff": # M코드 정지
                    fbsvr.firebase('moff', 'M코드 정지')
                    break
                elif idf.referee(Wtype.model, "pause") == "pause": # 와이어 미동작
                    pag.click(680, 430)
                    time.sleep(1)
                    pag.click(550, 720)
                    fbsvr.firebase('pause', '와이어 미동작')
                    break
                elif idf.referee(Wtype.model, 'start') == "stop": # 와이어 줄 연결 실패
                    fbsvr.firebase('off', '가공 정지')
                    break