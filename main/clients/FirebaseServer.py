import socket
import time
import pyautogui as pag
from firebase_admin import firestore
import pyrebase
from clients.WireType import WireType

class FirebaseServer:
    date = ""
    now = ""
    hour = ""
    min = ""
    strg = ""
    db = ""
    ss_date = ""
    ss_now = ""
    Wtype = ""
    firebaseConfig = {}


    def __init__(self):
        # firebase storage 연결
        self.firebaseConfig = {
        'apiKey': "AIzaSyCd3OwXDKauUYMDmIF163-OIr6qpMxbheQ",
        'authDomain': "flutterfire-8bfdb.firebaseapp.com",
        'databaseURL': "https://flutterfire-8bfdb-default-rtdb.firebaseio.com",
        'projectId': "flutterfire-8bfdb",
        'storageBucket': "flutterfire-8bfdb.appspot.com",
        'messagingSenderId': "711900003254",
        'appId': "1:711900003254:web:1a36463de9785b65829f17",
        'measurementId': "G-WNJLGFPTBH"
        }
        firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.strg = firebase.storage()
        self.db = firestore.client()
        self.Wtype = WireType()


    def internet_cheker(self): #인터넷 연결 확인
        ip_address = socket.gethostbyname(socket.gethostname())
        if ip_address == '127.0.0.1':
            return False
        else:
            return True

    def afterwork(self): # 퇴근시간
        if self.hour > 16 or self.hour < 8:
            return True

    def lunch_1(self): # 점심시간
        if self.hour == 12 and self.min >=30:
            return True    

    def lunch_2(self): # 점심시간
        if self.hour == 13 and self.min <=30:
            return True

    def screenshot(self, status): # 스크린샷 저장
        fileName = "{}{}{}{}{}{}{}{}".format('%s'%self.Wtype.file, ' - ', self.ss_date[2:], '_', self.ss_now, '_', status, '.png')
        pag.screenshot(fileName)
        self.strg.child('{}{}{}'.format('%s'%self.Wtype.file, '/', fileName)).put(fileName)

    def firebase(self, data, coment): # 서버 연결
        # 호출 시 현재시간 저장
        self.date = time.strftime("%Y-%m-%d")
        self.now = time.strftime("%H:%M:%S")
        self.hour = int(time.strftime('%H'))
        self.min = int(time.strftime('%M'))

        # 스크린샷 파일 저장 용
        self.ss_date = time.strftime("%Y%m%d")
        self.ss_now = time.strftime("%H%M%S")

        connect_checker = 0
        log = open("log_ip.txt", 'a')
        ip_address_2 = socket.gethostbyname(socket.gethostname())
        log_ip = self.date + ' ' + self.now + ' ' + ip_address_2 + '\n'
        log.write(log_ip)
        log.close()

        if self.internet_cheker() != True:
            print(self.date, self.now, '인터넷 연결이 불안정합니다.')
            connect_checker = 1
        while True:
            if self.internet_cheker() == True:
                if connect_checker == 1:
                    wire_internet = self.db.collection(u'%s'%self.Wtype.model).document(u'dates').collection('internet').document(u'%s %s'%(self.date, self.now))
                    wire_internet.set({
                    u'internet' : u'disconnected'
                    })
                break
        wire_off = self.db.collection(u'%s'%self.Wtype.model).document(u'dates').collection(u'%s'%self.date).document(u'%s'%self.now)
        wire_off.set({
            u'now': u'%s'%self.now,
            u'onoff': u'%s'%data
        })
        wire_off_date = self.db.collection(u'%s'%self.Wtype.model).document(u'%s'%self.date)
        wire_off_date.set({
            u'date': u'%s'%self.date,
        })
        if self.afterwork() == True:
            wire_push = self.db.collection(u'push_server').document(u'%s'%self.Wtype.model)
            wire_push.set({
                u'push' : u'%s'%data,
                u'time' : u'%s %s'%(self.date, self.now),
                u'wire' : u'%s'%self.Wtype.model
            })
            self.screenshot(coment)

        print(self.date, self.now,'%s'%coment)

    def exit_handler(self): # 알림 프로그램 종료 감지
        self.date=time.strftime("%Y-%m-%d")
        self.now=time.strftime("%H:%M:%S")
        wire_off = self.db.collection(u'%s'%self.Wtype.model).document(u'dates').collection(u'%s'%self.date).document(u'%s'%self.now)
        wire_off.set({
            u'now': u'%s'%self.now,
            u'onoff': u'exit'
        })
        wire_off_date = self.db.collection(u'%s'%self.Wtype.model).document(u'%s'%self.date)
        wire_off_date.set({
            u'date': u'%s'%self.date,
        })
        wire_push = self.db.collection(u'push_server').document(u'%s'%self.Wtype.model)
        wire_push.set({
            u'push' : u'exit',
            u'time' : u'%s %s'%(self.date, self.now),
            u'wire' : u'%s'%self.Wtype.model
        })

        self.screenshot('꺼짐')