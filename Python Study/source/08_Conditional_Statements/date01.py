# 날짜/시간과 관련된 기능을 가져옴
import datetime

# 현재 날짜/시간을 구함
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")