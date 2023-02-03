import math
import pyautogui as pag

line = '[I](2023-01-24  11:21:56 am)    Z:     75.0253'

print(math.floor(float(line[line.find("Z:") + 3:].strip())))

pag.screenshot("sdsd sd s처리실[프로그램자동결선 FEED MOTOR ALARM!!자동결선 FEED MOTOR ALARM!!자동결선 FEED MOTOR ALARM!!자동결선 FEED MOTOR ALARM!!자동결선 FEED MOTOR ALARM!!]오토스타트패(M21!!).png")