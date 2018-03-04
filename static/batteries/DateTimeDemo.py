"""
    
    date: 2018-03-01 15:37
"""

__author__ = "WXGALY"

# 时间类

from datetime import datetime, timedelta, timezone

# print(datetime.now())

dt = datetime(2018, 4, 19, 12, 20)

# print(dt)


# datetime转换为timestamp

# print(dt.timestamp())

# timestamp转换为datetime
# print(datetime.fromtimestamp(dt.timestamp()))
# print(datetime.utcfromtimestamp(dt.timestamp()))

# str转换为datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)


# datetime转换为str

# print(dt.strftime('%a, %b %d %H:%M'))


# datetime加减

# print(dt)
#
# print(dt + timedelta(hours=10))
#
# print(dt - timedelta(days=1))
#
# print(dt + timedelta(days=2, hours=12))

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)

print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))

print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))

print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))

print(tokyo_dt2)

