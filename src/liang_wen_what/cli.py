from datetime import datetime, time, timezone, timedelta
from chinese_calendar import is_holiday

WEEKDAYS = ["一", "二", "三", "四", "五", "六", "日"]


def main():
    now = datetime.now(timezone(timedelta(hours=8)))
    today = now.date()
    current = now.time()

    weekday = now.weekday()
    holiday = is_holiday(today)

    if weekday >= 5:
        peak = False
        reason = "今天是周末，全天执行谷价"
    elif holiday:
        peak = False
        reason = "今天是中国法定节假日，全天执行谷价"
    elif time(9, 0) <= current < time(12, 0):
        peak = True
        reason = "工作日 09:00-12:00，属于上午高峰时段"
    elif time(14, 0) <= current < time(18, 0):
        peak = True
        reason = "工作日 14:00-18:00，属于下午高峰时段"
    else:
        peak = False
        reason = "当前不在工作日高峰时段，执行谷价"

    print(f"梁文{'峰' if peak else '谷'}")
    print(f"时间：{now:%Y-%m-%d %H:%M:%S} 星期{WEEKDAYS[weekday]}")
    print(f"裁定：{reason}")


if __name__ == "__main__":
    main()
