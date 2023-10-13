import psutil
import win32api
import time
import pyautogui as pag

# pyinstaller -F --icon=.\setting\restart.ico restart.py

file_name_w = open("./main/setting/setting.txt", "a", encoding='utf-8') # 파일 이름 쓰기 변수 할당
file_name_r = open("./main/setting/setting.txt", "r", encoding='utf-8') # 파일 이름 읽기 변수 할당

file_name = file_name_r.readlines() # 파일 이름 읽어옴


if len(file_name) == 0: # 파일 이름이 없으면
    input_file_name = input('와이어 프로그램 파일이름 입력: ') # 파일 이름 입력
    input_root_name = input('와이어 프로그램 경로이름 입력: ')
    input_click_x = input('클릭 x좌표 입력: ')
    input_click_y = input('클릭 y좌표 입력: ')
    save = input_file_name + '\n'+ input_root_name + '\n' + input_click_x + '\n' + input_click_y
    file_name_w.write(save) # 입력한 파일 이름 써서 저장
    file_name_w.close()
    file_name = file_name_r.readlines()
    print(file_name)


file_name_r.close() 

print("-------와이어 알림 자동 재실행 프로그램-------")

while True:
    time.sleep(60)
    processList = []
    for proc in psutil.process_iter():
        processName = proc.name()
        processList.append(processName)
    if file_name[0][0:-1] not in processList:

        date=time.strftime("%Y-%m-%d")
        now=time.strftime("%H:%M:%S")
        root = file_name[1][0:-1] + '/' + file_name[0][0:-1]
        win32api.ShellExecute(0, "open", root, None, None, 1)

        log = open("./main/setting/restart_log.txt", 'a')
        log_contents = date + ' ' + now + ' ' + '재실행 로그' + '\n'
        log.write(log_contents)
        log.close()

        time.sleep(2)
        x = int(file_name[2][0:-1])
        y = int(file_name[3])
        point = (x, y)
        pag.click(point)
        print(date, now, "프로그램 종료 감지, 재실행 =>", root, ', 클릭:',point)
    time.sleep(120)