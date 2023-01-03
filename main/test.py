import pyautogui as pag
from PIL import Image
import pytesseract
import datetime as dt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# 남은 거리
pag.screenshot('wire1.png', region=(670, 600, 160, 16))
# pag.screenshot('wire1.png', region=(665, 595, 170, 25))

# 재료 T 두께
pag.screenshot('wire2.png', region=(320, 525, 47, 24))

# 걸린 시간
# pag.screenshot('wire3.png', region=(665, 639, 130, 25))
pag.screenshot('wire3.png', region=(750, 642, 42, 19))

img_1 = Image.open('wire1.png')
img_2 = Image.open('wire2.png')
img_3 = Image.open('wire3.png')
num1 = pytesseract.image_to_string(img_1)
num2 = pytesseract.image_to_string(img_2)
num3 = pytesseract.image_to_string(img_3)
print('가공 전 남은 거리:',num1)
print('가공 전 T 두께:',num2)
print('가공 전 걸린 시간:',num3)
remain = int(num1.split('.')[0])
T = int(num2.split('.')[0])

print('\n남은 거리:', remain)
print('재료 T 두께:', T)


# 재료 T
# (95 ,339 , 40, 18)

# 남은거리
# (395, 400, 135, 15)

# 방전시간
# (388, 433, 112, 23)d
y = dt.datetime.strptime = ("%d"%num3, "%H:%M")
print('시간 변환', y)