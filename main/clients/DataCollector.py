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
        for proc in psutil.process_iter():
            processName = proc.name()
            processList.append(processName)
            
        # 크롬 원격 데스크톱 remoting_host.exe
        if "TeamViewer_Desktop.exe" in processList or "remoting_host.exe":
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
        if self.start_button_clicked() == True:
                return True