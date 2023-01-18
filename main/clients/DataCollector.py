import psutil
import mouse


class DataCollector:
    completeFlag = False
    pos = []

    def __init__(self):
        pass

    # 원격 프로그램(팀뷰어) 실행중인지 확인
    def remote_check(self):
        processList = []
        # num1 = 0
        # num2 = 0
        # num3 = 0
        # num4 = 0
        for proc in psutil.process_iter():
            processName = proc.name()
            processList.append(processName)
            # if "remoting_host.exe" in processList:
            #     num1 += 1
            # if "TeamViewer_Desktop.exe" in processList:
            #     num2 += 1

            # if 'remoting_desktop.exe' in processList:
            #     num3 += 1
            # if 'remoting_native_messaging_host.exe' in processList:
            #     num4 += 1

        # a = sorted(processList)
        # print(a)
        # print("remoting_host.exe 횟수: ", num1)
        # print("TeamViewer_Desktop.exe 횟수: ", num2)
        # print("remoting_desktop.exe 횟수: ", num3)
        # print("remoting_native_messaging_host.exe 횟수: ", num4)

        # print("remoting_host.exe 여부: ","remoting_host.exe" in processList)
        # print("TeamViewer_Desktop.exe 여부: ","TeamViewer_Desktop.exe" in processList)
        # print("remoting_desktop.exe 여부: ", "remoting_desktop.exe" in processList)
        # print("remoting_native_messaging_host.exe 여부: ", "remoting_native_messaging_host.exe" in processList)


        # 크롬 원격 데스크톱 remoting_host.exe
        if "TeamViewer_Desktop.exe" in processList:
            return True


    def start_button_clicked(self):
        for i in self.pos:
            if 742 <= i[0] and i[0] <= 794 and 698 <= i[1] and i[1] <= 730:
                return True
            elif 525 <= i[0] and i[0] <= 577 and 698 <= i[1] and i[1] <= 730:
                return True


    def click_checker(self):
        if mouse.is_pressed("left"):
            self.pos.append(mouse.get_position())
            self.pos = list(set(self.pos))
            print(mouse.get_position())
        if self.start_button_clicked():
                return True