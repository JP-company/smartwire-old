from filecmp import clear_cache
import pyautogui as pag
import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pag.screenshot('wire.png', region=(607, 76, 73, 30))
img = Image.open('wire.png')
num = list(pytesseract.image_to_string(img))
real_num = num[3] + num[4] + num[5]

pag.click(793, 125) # NC 편집 클릭
time.sleep(0.5)

pag.click(1005, 163) # 스크롤 5회 위로 클릭
time.sleep(0.5)
pag.click(1005, 163)
time.sleep(0.5)
pag.click(1005, 163)
time.sleep(0.5)
pag.click(1005, 163)
time.sleep(0.5)
pag.click(1005, 163)
time.sleep(0.5)

pag.click(950, 244) # 맨땅 우클릭
time.sleep(0.5)

pag.click(977, 263) # 넘버 찾기 클릭
time.sleep(0.5)

pag.click(716, 383) # 박스 클릭
time.sleep(0.5)

pag.typewrite(real_num) # 넘버 입력
time.sleep(0.5)

pag.click(650, 420) # 검색 클릭
time.sleep(0.5)

pag.click(743, 280) # 해당 줄 우클릭
time.sleep(0.5)

# pag.click(801, 328) # 셋 점프 라인 클릭
# time.sleep(0.5)

# pag.click(772, 720) # 스타트
# time.sleep(120)

# pag.click(772, 720) # 다시 스타트