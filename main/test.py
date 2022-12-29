# import psutil
# import win32api
# import time
# from pynput import mouse

# def on_click(x, y, button, pressed):
#     if button == mouse.Button.left and pressed:
#         print("Mouse button clicked at ({}, {})".format(x, y))

# # 원격 프로그램(팀뷰어, 크롬 원격 데스크톱) 감지
# def remote_check():
#     processList = []
#     for proc in psutil.process_iter():
#         processName = proc.name()
#         processList.append(processName)
#     return processList

# while True:
#     processList = remote_check()
#     while "TeamViewer_Desktop.exe" in processList or "remoting_desktop.exe" in processList:
#         processList = remote_check()
#         print("원격프로그램 실행중")
#         time.sleep(2)
#     print("원격프로그램 꺼짐")
#     time.sleep(2)

# list = []

# list.insert(0, (0,1))

# # print(list)

# a=0
# b=0
# if (a and b) == 0:
#     print(112)

import pyautogui as pag
print(pag.position())