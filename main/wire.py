import firebase_admin
from firebase_admin import credentials
import atexit
import time
import pyautogui as pag
from clients.Identifier import Identifier
from clients.FirebaseServer import FirebaseServer


# exe 변환 명령어
# pyinstaller -F --icon=.\setting\wire.ico wire.py

# firebase 계정 연결
cred = credentials.Certificate('./main/setting/serviceAccount.json')
firebase_admin.initialize_app(cred)


class WireSolution:
    idf = ''
    fbsvr = ''
    Wtype = ''
    DC = ''

    def __init__(self):
        # 가동상태 식별자 객체 생성
        self.idf = Identifier()

        # 파이어베이스 서버연결 객체 생성
        self.fbsvr = FirebaseServer()

        # FirebaseServer의 Wtype 객체 주소 할당
        self.Wtype = self.fbsvr.Wtype

        # FirebaseServer의 DC 객체 주소 할당
        self.DC = self.fbsvr.DC

    def four_min_stop(self): # 4분 정지 감지 타이머
        for i in range(240):
            if self.idf.referee(self.Wtype.model, "start") != "start":
                time.sleep(1)
                if i == 179:
                    return True
            else:
                break

    def one_min_start(self): # 1분 시작 감지 타이머
        for i in range(60):
            if self.idf.referee(self.Wtype.model, "start") == "start":
                time.sleep(1)
                if i == 59:
                    return True
            else:
                break
    

    def stopType(self): # 멈춤 종류 반환
        if self.idf.referee(self.Wtype.model, "uncut") == "uncut": # 줄 씹힘
            self.fbsvr.firebase('uncut', '와이어 선 씹힘')
        elif self.idf.referee(self.Wtype.model, "nowire") == "nowire": # 와이어 선 부족
            self.fbsvr.firebase('nowire', '와이어 선 부족')
        elif self.idf.referee(self.Wtype.model, "finished") == "finished": # 작업완료
            self.fbsvr.firebase('finished', '작업 종료')
        elif self.idf.referee(self.Wtype.model, "contact") == "contact": # 와이어 선 접촉
            self.fbsvr.firebase('contact', '와이어 선 접촉')
        elif self.idf.referee(self.Wtype.model, "pause") == "pause": # 와이어 미동작
            pag.click(680, 430)
            time.sleep(1)
            pag.click(550, 720)
            self.fbsvr.firebase('pause', '와이어 미동작')
        elif self.idf.referee(self.Wtype.model, "moff") == "moff": # M코드 정지
            self.fbsvr.firebase('moff', 'M코드 정지')
        elif self.idf.referee(self.Wtype.model, 'start') == "stop": # 가동 정지
            self.fbsvr.firebase('off', '가공 정지')



# 와이어 솔루션 객체 생성
WS = WireSolution()

# 예기치 못한 프로그램 종료 시 수행
atexit.register(WS.fbsvr.exit_handler)


print("-------와이어 알림 프로그램 시작-------")
# time.sleep(10)

# 최초 프로그램 시작 시 멈춰있을때
if WS.idf.referee(WS.Wtype.model, 'start') != "start":
    WS.stopType()


while True:
    # 가동 시작 감지
    while True:
        time.sleep(1) # 1초마다

        # 원격 제어로 가동 시키는지
        WS.DC.completeFlag = False
        while WS.DC.remote_check() == True:
            if WS.idf.referee(WS.Wtype.model, 'start') == "start":
                WS.DC.completeFlag = True
                WS.fbsvr.firebase('on', '[원격 제어] 가공 시작')
                break
        if WS.DC.completeFlag:   
            break

        # 초록불 1분간 1초 간격 감지, 퇴근 후
        if WS.one_min_start() == True:
            WS.fbsvr.firebase('on', '가공 시작')
            break

    # 가동 정지 감지
    while True:
        time.sleep(1) # 1초마다

        # 회색불 4분간 1초 간격 감지, 퇴근 후
        if WS.four_min_stop() == True:
            WS.stopType() # 멈춤 종류 반환
            break                  