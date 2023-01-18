import socket
import time
import pyautogui as pag
from firebase_admin import firestore
import pyrebase
from PIL import Image
from clients.WireType import WireType
from clients.DataCollector import DataCollector
import pytesseract

class FirebaseServer:
    # 현재 시간 
    date = ""
    now = ""
    hour = ""
    min = ""

    # firebase storage, firestore 연결용
    strg = ""
    db = ""

    # 스크린샷 저장 파일용 시간
    ss_date = ""
    ss_now = ""

    # 와이어 종류 확인 참조변수
    Wtype = ""

    # 원격제어 데이터 수집기 참조변수
    DC = ""


    def __init__(self):
        # firebase storage 연결
        firebaseConfig = {
        'apiKey': "AIzaSyCd3OwXDKauUYMDmIF163-OIr6qpMxbheQ",
        'authDomain': "flutterfire-8bfdb.firebaseapp.com",
        'databaseURL': "https://flutterfire-8bfdb-default-rtdb.firebaseio.com",
        'projectId': "flutterfire-8bfdb",
        'storageBucket': "flutterfire-8bfdb.appspot.com",
        'messagingSenderId': "711900003254",
        'appId': "1:711900003254:web:1a36463de9785b65829f17",
        'measurementId': "G-WNJLGFPTBH"
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        self.strg = firebase.storage()
        self.db = firestore.client()
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # 와이어 종류 객체 생성
        self.Wtype = WireType()

        # 데이터 수집기 객체 생성
        self.DC = DataCollector()

    def internet_checker(self): #인터넷 연결 확인
        ip_address = socket.gethostbyname(socket.gethostname())
        if ip_address == '127.0.0.1':
            return False
        else:
            return True

    def afterwork(self): # 퇴근시간
        if self.hour > 18 or self.hour < 8:
            return True

    def lunch_1(self): # 점심시간
        if self.hour == 12 and self.min >=30:
            return True    

    def lunch_2(self): # 점심시간
        if self.hour == 13 and self.min <=30:
            return True

    def screenshot(self, status): # 스크린샷 저장
        fileName = "{}{}{}{}{}{}{}{}{}".format('main_screenshots/','%s'%self.Wtype.file, ' - ', self.ss_date[2:], '_', self.ss_now, '_', status, '.png')
        pag.screenshot(fileName)
        # self.strg.child('{}{}{}'.format('%s'%self.Wtype.file, '/', fileName)).put(fileName)
        
        # 만약에 원격제어중이면
        # if self.DC.completeFlag:

        # # 남은거리 좌표
        # areaRemainDistance = (395, 400, 530, 415)
        # # 재료 T
        # areaThickness = (94, 338, 134, 357)
        # # 방전시간
        # areaRunTime = (460, 430, 500, 455)

        # # 이미지 자르기
        # cropRemainDistance = img.crop(areaRemainDistance)
        # cropThickness = img.crop(areaThickness)
        # cropRunTime = img.crop(areaRunTime)

        # # pytesseract로 이미지 -> 문자열 변환
        # RemainDistance = pytesseract.image_to_string(cropRemainDistance)
        # Thickness = pytesseract.image_to_string(cropThickness)
        # RunTime = pytesseract.image_to_string(cropRunTime)

        # self.remote_data(RemainDistance, Thickness, RunTime)


    def firebase(self, data, coment): # 서버 연결

        # 인터넷 불안정 확인 변수
        disconnect = False

        # 인터넷 ip 따기
        log = open("./main/setting/log_ip.txt", 'a')
        ip_address_2 = socket.gethostbyname(socket.gethostname())
        log_ip = self.date + ' ' + self.now + ' ' + ip_address_2 + '\n'
        log.write(log_ip)
        log.close()

        # 인터넷이 연결이 안되었을때
        if self.internet_checker() == False:
            print(self.date, self.now, '인터넷 연결이 불안정합니다.')
            # 불안정 했다는 기록 남김
            disconnect = True

        # 인터넷 연결 될때까지 무한 루프
        while True:
            # 연결 되었을 때
            if self.internet_checker():
                # 인터넷이 전에 불안정 했다면 서버에 기록
                if disconnect:
                    wire_internet = self.db.collection(u'%s'%self.Wtype.model).document(u'dates').collection('internet').document(u'%s %s'%(self.date, self.now))
                    wire_internet.set({
                    u'internet' : u'disconnected'
                    })
                # 정상적으로 연결되었다면 그냥 빠져나옴
                break

        # 서버 - 현재 시간, 가동 종류
        wire_off = self.db.collection(u'%s'%self.Wtype.model).document(u'dates').collection(u'%s'%self.date).document(u'%s'%self.now)
        wire_off.set({
            u'now': u'%s'%self.now,
            u'onoff': u'%s'%data
        })

        # 서버 - 날짜
        wire_off_date = self.db.collection(u'%s'%self.Wtype.model).document(u'%s'%self.date)
        wire_off_date.set({
            u'date': u'%s'%self.date,
        })

        # 서버 - 퇴근 시간 이후에만 푸쉬서버에 알림을 보냄
        if self.afterwork():
            wire_push = self.db.collection(u'push_server').document(u'%s'%self.Wtype.model)
            wire_push.set({
                u'push' : u'%s'%data,
                u'time' : u'%s %s'%(self.date, self.now),
            })
        
        self.screenshot(coment)
        print(self.date, self.now,'%s'%coment)

    def exit_handler(self): # 알림 프로그램 종료 감지

        self.date=time.strftime("%Y-%m-%d")
        self.now=time.strftime("%H:%M:%S")

        # 프로그램이 꺼졌을 때 서버 올림
        wire_off = self.db.collection(u'%s'%self.Wtype.model).document(u'dates').collection(u'%s'%self.date).document(u'%s'%self.now)
        wire_off.set({
            u'now': u'%s'%self.now,
            u'onoff': u'exit'
        })
        wire_off_date = self.db.collection(u'%s'%self.Wtype.model).document(u'%s'%self.date)
        wire_off_date.set({
            u'date': u'%s'%self.date,
        })

        # 항상 푸시 알림 
        wire_push = self.db.collection(u'push_server').document(u'%s'%self.Wtype.model)
        wire_push.set({
            u'push' : u'exit',
            u'time' : u'%s %s'%(self.date, self.now),
            u'wire' : u'%s'%self.Wtype.model
        })
        self.screenshot('꺼짐')

    def remote_data(self, RemainDistance, Thickness, RunTime): # 원격제어로 재가동한 사례 모음
        self.date = time.strftime("%Y-%m-%d")
        self.now = time.strftime("%H:%M:%S")
        wire_push = self.db.collection(u'remote_data').document(u'%s'%self.Wtype.model).collection(u'%s'%self.date).document(u'%s'%self.now)
        wire_push.set({
            u'time' : u'%s %s'%(self.date, self.now),
            u'remain_distance' : u'%s'%RemainDistance,
            u'thickness' : u'%s'%Thickness,
            u'RunTime' : u'%s'%RunTime
        })