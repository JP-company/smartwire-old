import firebase_admin
from firebase_admin import credentials
import atexit
import time
import re
import math
import pyautogui as pag
from clients.Identifier import Identifier
from clients.FirebaseServer import FirebaseServer


# exe 변환 명령어
# pyinstaller -F --icon=.\setting\wire.ico wire.py

# firebase 계정 연결
cred = credentials.Certificate('./main/setting/serviceAccount.json')
firebase_admin.initialize_app(cred)


class WireSolution:
  idf = ""
  fbsvr = ""
  Wtype = ""
  DC = ""
  restart = False
  currentStatus = False
  count = 0
  resetCount = True

  def __init__(self):
    # 가동상태 식별자 객체 생성
    self.idf = Identifier()

    # 파이어베이스 서버연결 객체 생성
    self.fbsvr = FirebaseServer()

    # 현재 시간 설정
    self.set_time()

    # 현재 가공 정보 초기화
    self.fbsvr.currentlyInProgress()

  def afterwork(self): # 퇴근시간 후에
    if self.fbsvr.hour > 21 or self.fbsvr.hour < 8:
      return True

  def set_time(self): # 시간 설정
    # 호출 시 현재시간 저장
    self.fbsvr.date = time.strftime("%Y-%m-%d")
    self.fbsvr.now = time.strftime("%H:%M:%S")
    self.fbsvr.hour = int(time.strftime('%H'))
    self.fbsvr.min = int(time.strftime('%M'))

    # 스크린샷 파일 저장용
    self.fbsvr.ss_date = time.strftime("%Y%m%d")
    self.fbsvr.ss_now = time.strftime("%H%M%S")

  def four_min_stop(self): # 4분 정지 감지 타이머
    self.set_time()
    for i in range(240):
      if self.idf.referee(self.fbsvr.Wtype.model, "start") != "start":
        time.sleep(1)
        if i == 179:
          return True
      else:
        break

  def one_min_start(self): # 1분 시작 감지 타이머
    self.set_time()
    for i in range(60):
      if self.idf.referee(self.fbsvr.Wtype.model, "start") == "start":
        time.sleep(1)
        if i == 59:
          return True
      else:
        break

  def stopType(self): # 멈춤 종류 반환
    stopType = ['uncut', 'nowire', 'finished', 'contact', 'pause', 'moff', 'off']
    printResult = ['와이어 선 씹힘', '와이어 선 부족', '작업 종료', '와이어 선 접촉', '와이어 미동작', 'M코드 정지', '가공 정지']
    index = 0
    for stopCode in stopType:
      if self.idf.referee(self.fbsvr.Wtype.model, stopCode) == stopCode:
        self.fbsvr.firebase(stopCode, printResult[index])
      index += 1

  def autoStart(self):  # 기타 설정
    if self.restart:
      self.fbsvr.remote_data('가공 완료 후')
    self.currentStatus = False
    self.restart = False
    self.count = 0

# 와이어 솔루션 객체 생성
WS = WireSolution()

# 처음 켰을 때 설정

previousLogLength = 0

# 예기치 못한 프로그램 종료 시 수행
atexit.register(WS.fbsvr.exit_handler)


print("-------와이어 알림 프로그램 시작-------")

while True:
  # 현재 시간 설정
  WS.set_time()

  # 광명 와이어 로그파일 위치
  fileWrite = open("C:/spmEzCut/LogMessage/%s.log" %WS.fbsvr.date, "a", encoding='ANSI') # UTF8 ANSI
  fileRead = open("C:/spmEzCut/LogMessage/%s.log" %WS.fbsvr.date, "r", encoding='ANSI')
  fileWrite.close()

  # 파일 내용 읽어오기
  wire_num = fileRead.readlines()
  fileRead.close()

  # 현재 로그파일 길이 확인
  presentLogLength = len(wire_num)
  if presentLogLength < previousLogLength:
    previousLogLength = 0

  # 로그파일 변경 감지
  if presentLogLength != previousLogLength and presentLogLength != 0:

    # 추가된 라인 저장
    added_loglines = presentLogLength - previousLogLength
    
    # 추가된 라인 살펴보며 값 반환
    for i in range(0, added_loglines):
      line = wire_num[len(wire_num) - 1 - i]
      print(line)

      if re.search('Wire Contact Auto Stop', line):
        WS.fbsvr.firebase('stop_contact', '와이어 접촉')
        WS.currentStatus = False

        if WS.restart:
          WS.fbsvr.remote_data('가공 완료 후')
          WS.currentStatus = False
          WS.restart = False
        
        # 퇴근 후 자동 재실행
        if WS.afterwork() and WS.count < 5:
          WS.fbsvr.remote_data('멈춤')
          time.sleep(3)
          # Auto Start 누르기
          pag.click(550, 710)
          print("접촉 감지, 오토 스타트 실행")
          WS.restart = True
          WS.count += 1
        break

      elif re.search('작업중 30sec 접촉 정지', line):
        WS.fbsvr.firebase('stop_contact_30s', '와이어 30초 접촉')
        WS.currentStatus = False

        if WS.restart:
          WS.fbsvr.remote_data('가공 완료 후')
          WS.currentStatus = False
          WS.restart = False

        # 퇴근 후 자동 재실행
        if WS.afterwork() and WS.count < 5:
          WS.fbsvr.remote_data('처음 멈춤')
          time.sleep(3)
          # Auto Start 누르기
          pag.click(550, 710)
          print("접촉 감지, 오토 스타트 실행")
          WS.restart = True
          WS.count += 1
        break

      elif re.search('작업중 M코드정지', line):
        WS.fbsvr.firebase('stop_moff', 'M코드 정지')
        WS.autoStart()
        break
      elif re.search('작업중 단선', line):
        WS.fbsvr.firebase('stop_cut', '작업중 와이어 단선')
        WS.autoStart()
        break
      elif re.search('M20-삽입실패', line):
        WS.fbsvr.firebase('stop_insert_failure', '자동결선 삽입실패(M20)')
        WS.autoStart()
        break
      elif re.search('M21-절단실패', line):
        WS.fbsvr.firebase('stop_cut_failure', '자동결선 절단실패(M21)')
        WS.autoStart()
        break
      elif re.search('M21-잔여와이어 처리실패', line):
        WS.fbsvr.firebase('stop_cleanup_failure', '자동결선 잔여와이어 처리실패(M21)')
        WS.autoStart()
        break


      elif re.search('와이어 미동작', line):
        WS.fbsvr.firebase('stop_wire_notworking', '와이어 미동작')
        WS.autoStart()
        break
      elif re.search('가공액 미동작', line):
        WS.fbsvr.firebase('stop_liquid_notworking', '가공액 미동작')
        WS.autoStart()
        break
      elif re.search('자동결선 FEED MOTOR ALARM', line):
        WS.fbsvr.firebase('stop_feed_motor_alarm', '자동결선 FEED MOTOR ALARM!!')
        WS.autoStart()
        break
      elif re.search('자동결선 절단 공정 실패', line):
        WS.fbsvr.firebase('stop_auto_cut_failure', '자동결선 절단 공정 실패')
        WS.autoStart()
        break
      elif re.search('자동결선 잔여 WIRE 처리 실패', line):
        WS.fbsvr.firebase('stop_auto_cleanup_failure', '자동결선 잔여와이어 처리 실패')
        WS.autoStart()
        break
      elif re.search('자동결선 하부 뭉치 WIRE CONTACT', line):
        WS.fbsvr.firebase('stop_lowerpart_contact', '자동결선 하부 뭉치 WIRE CONTACT')
        WS.autoStart()
        break
      elif re.search('자동결선 상부 센서 WIRE CONTACT', line):
        WS.fbsvr.firebase('stop_upperpart_contact', '자동결선 상부 센서 WIRE CONTACT')
        WS.autoStart()
        break
      elif re.search('AWF 명령끝날때까지 센서감지', line):
        WS.fbsvr.firebase('stop_awf_sensor', 'AWF 명령끝날때까지 센서감지 안됨')
        WS.autoStart()
        break
      elif re.search('Work Tank Fluid Sensor Abnormal', line):
        WS.fbsvr.firebase('stop_fluid_sensor', '오일센서 이상 감지')
        WS.autoStart()
        break
      elif re.search('Auto Door Sensor Abnormal', line):
        WS.fbsvr.firebase('stop_door_sensor', '자동문센서 이상 감지')
        WS.autoStart()
        break
      elif re.search('회수부 와이어 이탈', line):
        WS.fbsvr.firebase('stop_collect_breakaway', '회수부 와이어 이탈')
        WS.autoStart()
        break
      elif re.search('Ready On', line):
        WS.fbsvr.firebase('ready_on', 'Ready On')
        WS.autoStart()
        break
      elif re.search('Emergency Stop', line):
        WS.fbsvr.firebase('stop_emergency', '비상정지')
        WS.autoStart()
        break
      elif re.search('READY Off', line):
        WS.fbsvr.firebase('ready_off', 'READY Off')
        WS.autoStart()
        break

      elif re.search('Reset', line):
        # 리셋 중복이면 서버에 안올림
        if WS.resetCount:
          WS.fbsvr.ncFile = ""
          WS.fbsvr.thickness = 0
          WS.fbsvr.currentlyInProgress()

        WS.fbsvr.firebase('stop_reset', 'Reset')
        WS.autoStart()
        WS.resetCount = False
        break
      elif re.search('작업 끝', line):
        WS.fbsvr.firebase('stop_finished', '작업 완료')
        WS.autoStart()
        break
      elif re.search('작업중 정지', line):
        WS.fbsvr.firebase('stop', '정지')
        WS.autoStart()
        break

      elif re.search('작업 재시작', line):
        # 자동재시작으로 가동시켰을 때
        if WS.restart:
          WS.fbsvr.firebase('start_autostart', '[프로그램]오토스타트')
          WS.currentStatus = True
          WS.restart = False
          break

        WS.fbsvr.firebase('start_restart', '가공 재시작')
        WS.currentStatus = True
        break
      
      elif re.search('Z:', line):
        WS.fbsvr.thickness = math.floor(float(line[line.find("Z:") + 3:].strip()))
      elif re.search('Nc File:', line):
        line = line[37:]
        WS.fbsvr.ncFile = line[line.find('-') + 1 : line.find('.NC') + 3]
        WS.fbsvr.currentlyInProgress()
        WS.fbsvr.firebase('start', '작업 시작')
        WS.currentStatus = True
        WS.restart = False
        WS.count = 0
        WS.resetCount = True
        break

      elif re.search('Initialization', line):
        WS.fbsvr.firebase('stop_initialization', '와이어 기계 연결 완료')
        WS.autoStart()
        break
      elif re.search('SPM Device Closed', line):
        WS.fbsvr.firebase('stop_closed', '와이어 기계 전원 종료됨')
        WS.autoStart()
        break
      elif re.search('SPM Device DisConnected', line):
        WS.fbsvr.firebase('stop_disconnected', '와이어 기계 연결 끊어짐')
        WS.autoStart()
        break
      elif re.search('SPM Device Open Succeeded', line):
        WS.fbsvr.firebase('stop_open_succeeded', '와이어 기계 전원 켜짐')
        WS.autoStart()
        break

    # 이전 로그 파일 길이에 현재 로그 파일 길이 할당
    previousLogLength = presentLogLength
  
  # 현재 멈춰있는데 시작됐다면
  if WS.currentStatus == False and WS.one_min_start():
    WS.set_time()
    WS.fbsvr.firebase('start_restart_detected', '가공 감지, 가공 재시작')
    if WS.restart:
      WS.fbsvr.remote_data('가공 완료 후')
    WS.currentStatus = True
    WS.restart = False
    WS.count = 0

  #1.1초 마다
  time.sleep(1.1)