# import psutil
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


a=0
b=1

if (a and b) == 0:
    print('ㅋㅋ')
else:
    print('ㅠㅠ')




import time
import mouse

# def on_click(x, y, button, pressed):
#     print('Button: %s, Position: (%s, %s), Pressed: %s ' %(button, x, y, pressed))
#     return False

# with mouse.Listener(on_click=on_click) as listener:
#     listener.join()


# pos = []
# while True:
#     if mouse.is_pressed("left"):
#         pos.append(mouse.get_position())
#         pos = list(set(pos))
#         print(pos)
#         time.sleep(0.1)
#         for i in pos:
#             if 742 <= i[0] and i[0] <= 794 and 525 <= i[1] and i[1] <= 577:
#                 print(i, '적중')





# list = []

# list.insert(0, (0,1))

# # print(list)

# a=0
# b=0
# if (a and b) == 0:
#     print(112)

# import pyautogui as pag
# print(pag.position())

# def hi():
#     for i in range(15):
#         if i == 14:
#             return True

# print(hi())
# for i in range(15):
#         if idf.referee(Wtype.model, "start") != "start":
#             time.sleep(20)
#             if i == 14:
#                 return True
#         else:
#             break