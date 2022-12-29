from datetime import date
from PIL import ImageGrab, Image
import time
import firebase_admin
from firebase_admin import credentials, storage, firestore, initialize_app
import atexit
import pyautogui as pag
import pyrebase
import socket
from clients.Identifier import identifier




# exe 변환 명령어
# pyinstaller -F --icon=.\wire.ico wire.py

file_w = open("./wire_num.txt", "a")
file_r = open("./wire_num.txt", "r")

wire_num = file_r.readlines()
file_r.close()

if len(wire_num) == 0:
    num = input('와이어 기계 번호를 입력하세요: ' )
    file_w.writelines(num)
    wire_num = num

file_w.close()

if wire_num[0] == 'sit1':
    model = 'wire_1'
    file = 'SIT_1'
elif wire_num[0] == 'sit2':
    model = 'wire_2'
    file = 'SIT_2'
elif wire_num[0] == 'km1':
    model = 'KM_wire_1'
    file = 'KM_1'
elif wire_num[0] == 'km2':
    model = 'KM_wire_2'
    file = 'KM_2'
elif wire_num[0] == 'km3':
    model = 'KM_wire_3'
    file = 'KM_3'
elif wire_num[0] == 'km4':
    model = 'KM_wire_4'
    file = 'KM_4'

idf = identifier()




# Use a service account
# cred = credentials.Certificate('C:\\Users\\Owner\\Desktop\\sit_python\\serviceAccount.json')
cred = credentials.Certificate('./serviceAccount.json')
firebase_admin.initialize_app(cred)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
hour = int(time.strftime('%H'))
green = (0, 255, 0)
grey = (194, 194, 194)
red = (255, 0, 0)
black = (0, 0, 0)

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
storage = firebase.storage()
db = firestore.client()


def internet_cheker(): #인터넷 연결 확인
    ip_address = socket.gethostbyname(socket.gethostname())
    if ip_address == '127.0.0.1':
        return False
    else:
        return True

def five_min_stop(): # 5분 정지 감지 타이머
    time.sleep(20)
    for i in range(14):
        if idf.realtimeMonitoring(model, 0) != "start":
            time.sleep(20)
        

def firststop(): #첫 멈춤
    if idf.realtimeMonitoring(model, "uncut") == "uncut": # 줄 씹힘
        firebase('uncut', '와이어 선 씹힘')
    elif idf.realtimeMonitoring(model, "nowire") == "nowire": # 와이어 선 부족
        firebase('nowire', '와이어 선 부족')
    elif idf.realtimeMonitoring(model, "finished") == "finished": # 작업완료
        firebase('finished', '작업 종료')
    elif idf.realtimeMonitoring(model, "contact") == "contact": # 와이어 선 접촉
        firebase('contact', '와이어 선 접촉')
    elif idf.realtimeMonitoring(model, "pause") == "pause": # 와이어 미동작
        pag.click(680, 430)
        time.sleep(1)
        pag.click(550, 720)
        firebase('pause', '와이어 미동작')
    elif idf.realtimeMonitoring(model, "moff") == "moff": # M코드 정지
        firebase('moff', 'M코드 정지')
    elif idf.realtimeMonitoring(model, 0) == "stop": # 가동 정지
        firebase('off', '가공 정지')

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

def afterwork(): # 퇴근시간, 점심시간
    hour = int(time.strftime('%H'))
    min = int(time.strftime('%M'))
    if hour > 16 or hour < 8:
        return True

def lunch_1():
    hour = int(time.strftime('%H'))
    min = int(time.strftime('%M'))
    if hour == 12 and min >=30:
        return True    

def lunch_2():
    hour = int(time.strftime('%H'))
    min = int(time.strftime('%M'))
    if hour == 13 and min <=30:
        return True

def screenshot(status): # 스크린샷 저장
    date=time.strftime("%Y%m%d")
    now=time.strftime("%H%M%S")
    fileName = "{}{}{}{}{}{}{}{}".format('%s'%file, ' - ', date[2:], '_', now, '_', status, '.png')
    pag.screenshot(fileName)
    storage.child('{}{}{}'.format('%s'%file, '/', fileName)).put(fileName)

def firebase(data, coment): # 서버 연결
    date=time.strftime("%Y-%m-%d")
    now=time.strftime("%H:%M:%S")
    connect_checker = 0
    log = open("log_ip.txt", 'a')
    ip_address_2 = socket.gethostbyname(socket.gethostname())
    log_ip = date + ' ' + now + ' ' + ip_address_2 + '\n'
    log.write(log_ip)
    log.close()
    if internet_cheker() != True:
        print(date, now, '인터넷 연결이 불안정합니다.')
        connect_checker = 1
    while True:
        if internet_cheker() == True:
            if connect_checker == 1:
                wire_internet = db.collection(u'%s'%model).document(u'dates').collection('internet').document(u'%s %s'%(date, now))
                wire_internet.set({
                u'internet' : u'disconnected'
                })
            break
    wire_off = db.collection(u'%s'%model).document(u'dates').collection(u'%s'%date).document(u'%s'%now)
    wire_off.set({
        u'now': u'%s'%now,
        u'onoff': u'%s'%data
    })
    wire_off_date = db.collection(u'%s'%model).document(u'%s'%date)
    wire_off_date.set({
        u'date': u'%s'%date,
    })
    if afterwork() == True or lunch_1() == True or lunch_2() == True:
        wire_push = db.collection(u'push_server').document(u'%s'%model)
        wire_push.set({
            u'push' : u'%s'%data,
            u'time' : u'%s %s'%(date, now),
            u'wire' : u'%s'%model
        })
        screenshot(coment)

    print(date, now,'%s'%coment)

def exit_handler(): # 알림 프로그램 종료 감지
    date=time.strftime("%Y-%m-%d")
    now=time.strftime("%H:%M:%S")
    wire_off = db.collection(u'%s'%model).document(u'dates').collection(u'%s'%date).document(u'%s'%now)
    wire_off.set({
        u'now': u'%s'%now,
        u'onoff': u'exit'
    })
    wire_off_date = db.collection(u'%s'%model).document(u'%s'%date)
    wire_off_date.set({
        u'date': u'%s'%date,
    })
    wire_push = db.collection(u'push_server').document(u'%s'%model)
    wire_push.set({
        u'push' : u'exit',
        u'time' : u'%s %s'%(date, now),
        u'wire' : u'%s'%model
    })
    screenshot('꺼짐')

atexit.register(exit_handler)



print("-------와이어 알림 프로그램 시작-------")

if idf.realtimeMonitoring(model, 0) == "start": # 가동중일때
    while True:
        while True:
            time.sleep(10)
            if idf.realtimeMonitoring(model, 0) == "start": # 최초 초록불 확인, 퇴근 후
                firebase('on', '가공 시작')
                break
        while True:
            time.sleep(10)
            if idf.realtimeMonitoring(model, 0) != "start": # 최초 회색불 감지, 퇴근 후
                five_min_stop() # 5분 동안 20초 간격으로 회색불 확인
                if idf.realtimeMonitoring(model, "uncut") == "uncut": # 줄 씹힘
                    firebase('uncut', '와이어 선 씹힘')
                    break
                elif idf.realtimeMonitoring(model, "nowire") == "nowire": # 와이어 선 부족
                    firebase('nowire', '와이어 선 부족')
                    break
                elif idf.realtimeMonitoring(model, "finished") == "finished": # 작업종료
                    firebase('finished', '작업 종료')
                    break
                elif idf.realtimeMonitoring(model, "contact") == "contact": # 와이어 선 접촉
                    firebase('contact', '와이어 선 접촉')
                    break
                elif idf.realtimeMonitoring(model, "moff") == "moff": # M코드 정지
                    firebase('moff', 'M코드 정지')
                    break
                elif idf.realtimeMonitoring(model, "pause") == "pause": # 와이어 미동작
                    pag.click(680, 430)
                    time.sleep(1)
                    pag.click(550, 720)
                    firebase('pause', '와이어 미동작')
                    break
                elif idf.realtimeMonitoring(model, 0) == "stop": # 와이어 줄 연결 실패
                    firebase('off', '가공 정지')
                    break
else: # 멈춰있을때
    date=time.strftime("%Y-%m-%d")
    now=time.strftime("%H:%M:%S")
    firststop()
    while True:
        while True:
            if idf.realtimeMonitoring(model, 0) == "start": # 최초 초록불 확인, 퇴근 후
                time.sleep(10)
                date=time.strftime("%Y-%m-%d")
                now=time.strftime("%H:%M:%S")
                firebase('on', '가공 시작')
                break
        while True:
            if idf.realtimeMonitoring(model, 0) != "start": # 최초 회색불 감지, 퇴근 후
                time.sleep(10)
                date=time.strftime("%Y-%m-%d")
                now=time.strftime("%H:%M:%S")
                five_min_stop() # 5분 동안 20초 간격으로 회색불 확인
                if idf.realtimeMonitoring(model, "uncut") == "uncut": # 줄 씹힘
                    firebase('uncut', '와이어 선 씹힘')
                    break
                elif idf.realtimeMonitoring(model, "nowire") == "nowire": # 와이어 선 부족
                    firebase('nowire', '와이어 선 부족')
                    break
                elif idf.realtimeMonitoring(model, "finished") == "finished": # 작업종료
                    firebase('finished', '작업 종료')
                    break
                elif idf.realtimeMonitoring(model, "contact") == "contact": # 와이어 선 접촉
                    firebase('contact', '와이어 선 접촉')
                    break
                elif idf.realtimeMonitoring(model, "moff") == "moff": # M코드 정지
                    firebase('moff', 'M코드 정지')
                    break
                elif idf.realtimeMonitoring(model, "pause") == "pause": # 와이어 미동작
                    pag.click(680, 430)
                    time.sleep(1)
                    pag.click(550, 720)
                    firebase('pause', '와이어 미동작')
                    break
                elif idf.realtimeMonitoring(model, 0) == "stop": # 와이어 줄 연결 실패
                    firebase('off', '가공 정지')
                    break