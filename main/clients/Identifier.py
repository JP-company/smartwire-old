from PIL import ImageGrab, Image


class identifier:
    cdn_list = [(0,0)] * 3
    cdn_start_list = [(0,0)] * 5
    case = ""
    model = ""
    green = (0, 255, 0)
    grey = (194, 194, 194)
    red = (255, 0, 0)
    black = (0, 0, 0)

    def __init__(self):
        pass

    
    def realtimeMonitoring(self, model, case): # 작동 상태 값 반환
        self.model = model
        self.case = case

        # SIT와이어 환경 설정
        if model == "wire_1" or "wire_2":
            if case == "nowire": # 와이어 선 부족
                self.cdn_list[0] = (340, 755)
            elif case == "finished": # 작업 완료
                self.cdn_list[0] = (760, 755)
            elif case == "contact": # 와이어 선 접촉
                self.cdn_list[0] = (430, 755)
            elif case == "moff": # M코드 정지
                self.cdn_list[0] = (678, 755)
            elif case == "pause": # 와이어 미동작
                self.cdn_list[0] = (1120, 315)
            elif case == "uncut": # 와이어 선 씹힘
                self.cdn_list[0] = (1120, 165)
                self.cdn_list[1] = (1120, 200)
                self.cdn_list[2] = (1120, 230)
            
            self.cdn_start_list[0] = (765,700)
            self.cdn_start_list[1] = (710, 700)
            self.cdn_start_list[2] = (665, 700)
            self.cdn_start_list[3] = (610, 700)
            self.cdn_start_list[4] = (600, 760)
        # 광명와이어 환경 설정
        elif model == "KM_wire_1" or "KM_wire_2" or "KM_wire_3" or "KM_wire_4":
            if case == "nowire": # 와이어 선 부족
                self.cdn_list[0] = (340, 745)
            elif case == "finished": # 작업 완료
                self.cdn_list[0] = (760, 745)
            elif case == "contact": # 와이어 선 접촉
                self.cdn_list[0] = (430, 745)
            elif case == "moff": # M코드 정지
                self.cdn_list[0] = (680, 745)
            
            self.cdn_start_list[0] = (765,690)
            self.cdn_start_list[1] = (710, 690)
            self.cdn_start_list[2] = (665, 690)
            self.cdn_start_list[3] = (610, 690)
            self.cdn_start_list[4] = (590, 750)

        
        screen = ImageGrab.grab()
        def color(index):
            x = screen.getpixel(self.cdn_list[index])
            return x
        
        def color_start(index):
            x = screen.getpixel(self.cdn_start_list[index])
            return x

        # 값 반환
        if (color_start(0) and color_start(1) and color_start(2) and color_start(3)) == self.green:
            return "start"
        else:
            if color(0) == self.red:
                if self.case == "nowire":
                    return "nowire"
                elif self.case == "finished":
                    return "finished"
                elif self.case == "contact":
                    return "contact"
                elif self.case == "moff":
                    return "moff"
                elif self.case == "pause":
                    return "pause"
                elif (color(1) and color (2)) == self.red and self.case == "uncut":
                    return "uncut"
            return "stop"


