# dateutil modul
#  + relativedelta
# calendar modul

# https://dev.to/ejbarba/python-dateutil-module-4m03
# https://opensource.com/article/18/4/python-datetime-libraries
# https://opensource.com/article/17/5/understanding-datetime-python-primer
# https://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time
# https://www.guru99.com/calendar-in-python.html
# https://www.geeksforgeeks.org/python-calendar-module/

# A dateutil modul segítségével könnyen tudunk relatív időkülönbségeket manipulálni.

# Installálása:

pip install python-dateutil

#########################################

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import calendar

now = datetime.now()
print(now) # 2021-02-26 12:31:18.063787

# Egy hét múlva:

next_week = now + relativedelta(weeks=+1)
print(next_week) # 2021-03-05 12:31:18.063787

# Egy hónap és egy hét múlva:

next_month_plus_one_week = now + relativedelta(months=+1, weeks=+1)
print(next_month_plus_one_week) # 2021-04-02 12:32:58.063787

# Egy hónap, egy hét és 10 óra múlva:

x = now + relativedelta(months=+1, weeks=+1, hours=+10)
print(x) # 2021-04-02 22:31:18.063787

# Egy hónap és egy hét múlva 13 órakor:

x = now + relativedelta(months=+1, weeks=+1, hour=+13)
print(x) # 2021-04-02 13:31:18.063787

# Helyesen kezeli a szökőéveket:

print(date(2020, 1, 31) + relativedelta(months=+1)) # 2020-02-29

#########################################

# Két dátum különbsége:

nasa_birthday = datetime(1958, 7, 29, 0, 0)
age = relativedelta(today, nasa_birthday)
print(age) # relativedelta(years=+62, months=+7, hours=+6, minutes=+4, seconds=+16, microseconds=+33893)

print(f'{age.years} éve, {age.months} hónapja és { age.days} napja alakult a NASA')
# 62 éve, 6 hónapja és 28 napja alakult a NASA

#########################################

# Jövő kedd:

next_tuesday = today + relativedelta(weeks=+1, weekday=calendar.TUESDAY)
print(next_tuesday) # 2021-03-09 00:00:00

#########################################

# Készítsünk naptárt a calendar modul segítségével.

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
c_str = c.formatmonth(2021,2)
print(c_str)

#    February 2021
# Su Mo Tu We Th Fr Sa
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28

# Ha azt akarjuk, hogy hétfővel kezdődjenek az oszlopok:

c = calendar.TextCalendar(calendar.MONDAY)
c_str = c.formatmonth(2021,2)
print(c_str)

#    February 2021
# Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28

# HTML formátumban is elő tudjuk állítani a naptárt:

c = calendar.HTMLCalendar(calendar.MONDAY)
c_str = c.formatmonth(2021,2)
print(c_str)

#########################################
