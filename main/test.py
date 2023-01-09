import datetime as dt
import pyautogui as pag
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# 남은 거리
# pag.screenshot('wire1.png', region=(670, 600, 160, 16))
# pag.screenshot('wire1.png', region=(665, 595, 170, 25))
img = pag.screenshot('wire.png')
area1 = (665, 595, 835, 620)
area2 = (320, 525, 367, 549)
area3 = (750, 642, 792, 661)
crop1 = img.crop(area1)
crop2 = img.crop(area2)
crop3 = img.crop(area3)

# 재료 T 두께
# pag.screenshot('wire2.png', region=(320, 525, 47, 24))

# 걸린 시간
# pag.screenshot('wire3.png', region=(665, 639, 130, 25))
# pag.screenshot('wire3.png', region=(750, 642, 42, 19))

num1 = pytesseract.image_to_string(crop1)
num2 = pytesseract.image_to_string(crop2)
num3 = pytesseract.image_to_string(crop3)
print('가공 전 남은 거리:',num1)
print('가공 전 T 두께:',num2)
print('가공 전 가동 시간:',num3)
remain = int(num1.split('.')[0])
T = int(num2.split('.')[0])

print('\n남은 거리:', remain)
print('재료 T 두께:', T)


# 남은거리
# (395, 400, 135, 15)

# 재료 T
# (95 ,339 , 40, 18)

# 방전시간
# (388, 433, 112, 23)

y = dt.datetime.strptime('20170511 010000' ,"%Y%m%d %H%M%S")
x = dt.datetime.strptime('20170510 003000' ,"%Y%m%d %H%M%S")

y = dt.datetime.strptime('1:00' ,"%H:%M")
x = dt.datetime.strptime('0:30' ,"%H:%M")

y = y - x
print('시간 변환:', y)

