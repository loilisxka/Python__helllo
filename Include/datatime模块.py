# -*- coding: utf-8 -*-
from datetime import datetime,timedelta,timezone
import re
def to_timestamp(dt_str,tz_str):
    cday = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    shiqu = re.match(r'UTC([-+]\d+):\d+',tz_str)
    zone = timezone(timedelta(hours=int(shiqu.group(1))))
    return cday.replace(tzinfo=zone).timestamp()
#测试
t1 = to_timestamp('2015-6-1 08:10:30','UTC+7:00')
assert t1 == 1433121030.0,t1
t2 = to_timestamp('2015-5-31 16:10:30','UTC-09:00')
assert t2 == 1433121030.0,t2
print('ok')