import re
import datetime  as dt
from datetime import datetime as dtdt

def get_days_from_today(dd):
    td = dtdt.now()
    day = int(td.strftime("%d"))
    
    day2 = dtdt.strptime(dd,'%m/%d/%y %H:%M:%S').date()
    day2 = int(day2.strftime("%d"))
    newDate = (day-day2)
    print(f"Кількість дні між датами {newDate}")
    pass

dd = '10/19/22 13:55:26'
get_days_from_today(dd)