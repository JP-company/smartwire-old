from datetime import date
from PIL import ImageGrab, Image
import time
import firebase_admin
from firebase_admin import credentials, storage, firestore, initialize_app
import atexit
import pyautogui as pag
import pytesseract
import pyrebase

model = 'wire_1'
file = 'SIT_1'

# Use a service account
# cred = credentials.Certificate('C:\\Users\\Owner\\Desktop\\sit_python\\serviceAccount.json')
cred = credentials.Certificate('./serviceAccount.json')
firebase_admin.initialize_app(cred)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
hour = int(time.strftime('%H'))
green = (0, 255, 0)
grey = (194, 194, 194)
red = (255, 0, 0)

firebaseConfig = {
  'apiKey': "AIzaSyCd3OwXDKauUYMDmIF163-OIr6qpMxbheQ",
  'authDomain': "flutterfire-8bfdb.firebaseapp.com",
  'databaseURL': "https://flutterfire-8bfdb-default-rtdb.firebaseio.com",
  'projectId': "flutterfire-8bfdb",
  'storageBucket': "flutterfire-8bfdb.appspot.com",
  'messagingSenderId': "711900003254",
  'appId': "1:711900003254:web:1a36463de9785b65829f17",
  'measurementId': "G-WNJLGFPTBH"
};
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
db = firestore.client()


def grey_reader(): # 회색불
    screen = ImageGrab.grab()
    pos = (765, 700)
    RGB = screen.getpixel(pos)

    if RGB == grey: 
        return True

def uncut_reader(): # 줄 씹힘
    screen = ImageGrab.grab()
    pos_1 = (1120, 165)
    pos_2 = (1120, 200)
    pos_3 = (1120, 230)
    RGB_1 = screen.getpixel(pos_1)
    RGB_2 = screen.getpixel(pos_2)
    RGB_3 = screen.getpixel(pos_3)


    if RGB_1 == red or RGB_2 == red or RGB_3 == red: 
        return True

def nowire_reader(): # 와이어 선 부족
    screen = ImageGrab.grab()
    pos = (340, 755)
    RGB = screen.getpixel(pos)

    if RGB == red:
        return True

def finished_reader(): # 작업종료
    screen = ImageGrab.grab()
    pos = (760,755)
    RGB = screen.getpixel(pos)

    if RGB == green:
        return True

def comoff_reader(): # 컴퓨터 종료
    screen = ImageGrab.grab()
    pos = (995,660)
    RGB = screen.getpixel(pos)

    if RGB == grey:
        return True

def contact_reader(): # 접촉
    screen = ImageGrab.grab()
    pos = (430, 755)
    RGB = screen.getpixel(pos)

    if RGB == red:
        return True

def pause_reader(): # 와이어 미동작
    screen = ImageGrab.grab()
    pos = (1120, 315)
    RGB = screen.getpixel(pos)

    if RGB == red:
        return True

def moff_reader(): # M코드 정지
    screen = ImageGrab.grab()
    pos = (680, 755)
    RGB = screen.getpixel(pos)

    if RGB == red:
        return True

def start_reader(): # 초록불 감지 센서
    screen = ImageGrab.grab()
    pos_1 = (765,700)
    pos_2 = (600, 760)
    pos_3 = (710, 700)
    pos_4 = (665, 700)
    pos_5 = (610, 700)
    RGB_1 = screen.getpixel(pos_1)
    RGB_2 = screen.getpixel(pos_2)
    RGB_3 = screen.getpixel(pos_3)
    RGB_4 = screen.getpixel(pos_4)
    RGB_5 = screen.getpixel(pos_5)
    if RGB_1 == green and RGB_2 == green and RGB_3 == green and RGB_4 == green and RGB_5 == green:
        return True

def five_min_stop(): # 5분 정지 감지 타이머
    time.sleep(20)
    if start_reader() != True:
        time.sleep(20)
        if start_reader() != True:
            time.sleep(20)
            if start_reader() != True:
                time.sleep(20)
                if start_reader() != True:
                    time.sleep(20)
                    if start_reader() != True:
                        time.sleep(20)
                        if start_reader() != True:
                            time.sleep(20)
                            if start_reader() != True:
                                time.sleep(20)
                                if start_reader() != True:
                                    time.sleep(20)
                                    if start_reader() != True:
                                        time.sleep(20)
                                        if start_reader() != True:
                                            time.sleep(20)
                                            if start_reader() != True:
                                                time.sleep(20)
                                                if start_reader() != True:
                                                    time.sleep(20)
                                                    if start_reader() != True:
                                                        time.sleep(20)
                                                        if start_reader() != True:
                                                            time.sleep(20)

def firststop(): #첫 멈춤
    date=time.strftime("%Y-%m-%d")
    now=time.strftime("%H:%M:%S")
    #five_min_stop() # 5분 동안 20초 간격으로 회색불 확인
    if start_reader() != True and uncut_reader() == True: # 줄 씹힘
        firebase('uncut', '와이어 선 씹힘', 'STOP')
    elif start_reader() != True and nowire_reader() == True: # 와이어 선 부족
        firebase('nowire', '와이어 선 부족', 'STOP')
    elif start_reader() != True and finished_reader() == True: # 작업종료
        firebase('finished', '작업 종료', 'STOP')
    elif start_reader() != True and comoff_reader() ==True: # 컴퓨터 종료
        firebase('comoff', '컴퓨터 종료', 'STOP')
    elif start_reader() != True and contact_reader() == True: # 와이어 선 접촉
        firebase('contact', '와이어 선 접촉', 'STOP')
    elif start_reader() != True and pause_reader() == True: # 와이어 미동작
        pag.click(680, 430)
        time.sleep(1)
        pag.click(550, 720)
        firebase('pause', '와이어 미동작', 'STOP')
    elif start_reader() != True and moff_reader() == True: # M코드 정지
        firebase('moff', 'M코드 정지', 'STOP')
    elif start_reader() != True and uncut_reader() != True and nowire_reader() != True and finished_reader() != True and comoff_reader() != True and contact_reader() != True and pause_reader() != True and moff_reader() != True: # 와이어 줄 연결 실패
        firebase('off', '가공 정지', 'STOP')
    else:
        firebase('off', '가공 정지', 'STOP')

def auto_start(): # 자동 재시작
    pag.screenshot('wire.png', region=(607, 76, 73, 26))
    img = Image.open('wire.png')
    num = list(pytesseract.image_to_string(img))
    real_num = num[2] + num[3] + num[4] + num[5] + num[6]

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
    if hour > 19 or hour < 8:
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

def firebase(data, coment, status): # 서버 연결
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
        wire_push = db.collection(u'%s'%model).document(u'dates').collection('time').document(u'%s %s'%(date, now))
        wire_push.set({
            u'push' : u'yes'
        })
        screenshot(status)

    print(date, now,'%s'%coment)




if start_reader() == True: # 가동중일때
    while True:
        while True:
            if start_reader() == True: # 최초 초록불 확인
                date=time.strftime("%Y-%m-%d")
                now=time.strftime("%H:%M:%S")
                firebase('on', '가공 시작', 'START')
                break
        while True:
            if start_reader() != True: # 최초 회색불 감지
                date=time.strftime("%Y-%m-%d")
                now=time.strftime("%H:%M:%S")
                five_min_stop() # 5분 동안 20초 간격으로 회색불 확인
                if start_reader() != True and uncut_reader() == True: # 줄 씹힘
                    firebase('uncut', '와이어 선 씹힘', 'STOP')
                    break
                elif start_reader() != True and nowire_reader() == True: # 와이어 선 부족
                    firebase('nowire', '와이어 선 부족', 'STOP')
                    break
                elif start_reader() != True and finished_reader() == True: # 작업종료
                    firebase('finished', '작업 종료', 'STOP')
                    break
                elif start_reader() != True and comoff_reader() ==True: # 컴퓨터 종료
                    firebase('comoff', '컴퓨터 종료', 'STOP')
                    break
                elif start_reader() != True and contact_reader() == True: # 와이어 선 접촉
                    firebase('contact', '와이어 선 접촉', 'STOP')
                    break
                elif start_reader() != True and pause_reader() == True: # 와이어 미동작
                    pag.click(680, 430)
                    time.sleep(1)
                    pag.click(550, 720)
                    firebase('pause', '와이어 미동작', 'STOP')
                    break
                elif start_reader() != True and moff_reader() == True: # M코드 정지
                    firebase('moff', 'M코드 정지', 'STOP')
                    break
                elif start_reader() != True and uncut_reader() != True and nowire_reader() != True and finished_reader() != True and comoff_reader() != True and contact_reader() != True and pause_reader() != True and moff_reader() != True: # 와이어 줄 연결 실패
                    firebase('off', '가공 정지', 'STOP')
                    break
else: # 멈춰있을때
    date=time.strftime("%Y-%m-%d")
    now=time.strftime("%H:%M:%S")
    firststop()
    while True:
        while True:
            if start_reader() == True: # 최초 초록불 확인
                date=time.strftime("%Y-%m-%d")
                now=time.strftime("%H:%M:%S")
                firebase('on', '가공 시작', 'START')
                break
        while True:
            if start_reader() != True: # 최초 회색불 감지
                date=time.strftime("%Y-%m-%d")
                now=time.strftime("%H:%M:%S")
                five_min_stop() # 5분 동안 20초 간격으로 회색불 확인
                if start_reader() != True and uncut_reader() == True: # 줄 씹힘
                    firebase('uncut', '와이어 선 씹힘', 'STOP')
                    break
                elif start_reader() != True and nowire_reader() == True: # 와이어 선 부족
                    firebase('nowire', '와이어 선 부족', 'STOP')
                    break
                elif start_reader() != True and finished_reader() == True: # 작업종료
                    firebase('finished', '작업 종료', 'STOP')
                    break
                elif start_reader() != True and comoff_reader() ==True: # 컴퓨터 종료
                    firebase('comoff', '컴퓨터 종료', 'STOP')
                    break
                elif start_reader() != True and contact_reader() == True: # 와이어 선 접촉
                    firebase('contact', '와이어 선 접촉', 'STOP')
                    break
                elif start_reader() != True and pause_reader() == True: # 와이어 미동작
                    pag.click(680, 430)
                    time.sleep(1)
                    pag.click(550, 720)
                    firebase('pause', '와이어 미동작', 'STOP')
                    break
                elif start_reader() != True and moff_reader() == True: # M코드 정지
                    firebase('moff', 'M코드 정지', 'STOP')
                    break
                elif start_reader() != True and uncut_reader() != True and nowire_reader() != True and finished_reader() != True and comoff_reader() != True and contact_reader() != True and pause_reader() != True and moff_reader() != True: # 와이어 줄 연결 실패
                    firebase('off', '가공 정지', 'STOP')
                    break