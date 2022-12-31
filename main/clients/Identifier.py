from PIL import ImageGrab

class Identifier:
    cdn_list = [(0,0)] * 5
    case = ""
    model = ""
    green = (0, 255, 0)
    grey = (194, 194, 194)
    red = (255, 0, 0)
    black = (0, 0, 0)

    def __init__(self):
        pass


    # 회사별 좌표값 할당 메서드
    def coordinateCollector(self, model, case):
        
        # iv에 할당
        self.model = model
        self.case = case
        
        # 호출될때마다 리스트 비워줌
        self.cdn_list = [(0,0)] * 5

        # SIT와이어 환경 설정
        if model == "wire_1" or model == "wire_2":
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
            elif case == "start": # 시작 감지 좌표
                self.cdn_list[0] = (765,700)
                self.cdn_list[1] = (710, 700)
                self.cdn_list[2] = (665, 700)
                self.cdn_list[3] = (610, 700)
                self.cdn_list[4] = (600, 760)

        # 광명와이어 환경 설정
        elif model == "KM_wire_1" or model == "KM_wire_2" or model == "KM_wire_3" or model == "KM_wire_4":
            if case == "nowire": # 와이어 선 부족
                self.cdn_list[0] = (340, 745)
            elif case == "finished": # 작업 완료
                self.cdn_list[0] = (760, 745)
            elif case == "contact": # 와이어 선 접촉
                self.cdn_list[0] = (430, 745)
            elif case == "moff": # M코드 정지
                self.cdn_list[0] = (680, 745)
            elif case == "start": # 시작 감지 좌표
                self.cdn_list[0] = (765,690)
                self.cdn_list[1] = (710, 690)
                self.cdn_list[2] = (665, 690)
                self.cdn_list[3] = (610, 690)
                self.cdn_list[4] = (590, 750)



    # 작동 상태 값 반환 메서드
    def referee(self, model, case):

        # coordinateCollector 메서드 호출 
        self.coordinateCollector(model, case) 

        # 해당 좌표 RGB값 확인
        screen = ImageGrab.grab()
        def color(index):
            x = screen.getpixel(self.cdn_list[index])
            return x
        
        # 값 반환
        # 초록색이 아니면 멈췄다고 판단
        if (color(0) and color(1) and color(2) and color(3)) == self.green:
            return self.case
        else:
            if color(0) == self.red: # 해당 멈춤 케이스가 빨간불이라면
                if (color(1) and color(2)) == self.red: # 선 씹힘 케이스
                    return self.case
                elif self.case != "uncut": # 선 씹힘 케이스
                    return self.case
            return "stop"