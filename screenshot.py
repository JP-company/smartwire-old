import time

hour = int(time.strftime('%H'))

if hour < 15 or hour > 45:
  print(hour)
else:
  print(hour + 100)

print(hour)