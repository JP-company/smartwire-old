class WireType:
    wire_num = [] # 와이어 기계 종류
    model = '' 
    file = ''

    def __init__(self):
        self.naming()

    # 와이어 기계 종류 파일 읽어오기, 없으면 생성
    def file_reader(self):
        file_write = open("./wire_num.txt", "a")
        file_read = open("./wire_num.txt", "r")

        # 파일 내용 읽어오기
        self.wire_num = file_read.readlines()
        file_read.close()

        # 파일에 암것도 없으면 새로 입력
        if len(self.wire_num) == 0:
            num = input('와이어 기계 번호를 입력하세요: ' )
            file_write.writelines(num)
            self.wire_num.append(num)
        
        file_write.close()


    def naming(self):

        # file_reader 호출
        self.file_reader()

        # 와이어 기계명 할당
        if self.wire_num[0] == 'sit1':
            self.model = 'wire_1'
            self.file = 'SIT_1'
        elif self.wire_num[0] == 'sit2':
            self.model = 'wire_2'
            self.file = 'SIT_2'
        elif self.wire_num[0] == 'km1':
            self.model = 'KM_wire_1'
            self.file = 'KM_1'
        elif self.wire_num[0] == 'km2':
            self.model = 'KM_wire_2'
            self.file = 'KM_2'
        elif self.wire_num[0] == 'km3':
            self.model = 'KM_wire_3'
            self.file = 'KM_3'
        elif self.wire_num[0] == 'km4':
            self.model = 'KM_wire_4'
            self.file = 'KM_4'