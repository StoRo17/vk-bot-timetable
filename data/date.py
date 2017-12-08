import calendar
from datetime import datetime, timedelta

today = datetime.today()+timedelta(hours=3)


def load_week():
    week_number = today.isocalendar()[1]

    if week_number % 2 == 0:
        return 'first_week'

    return 'second_week'


def get_week_day_name(days_after_current=0):
    week_day_number = (today + timedelta(days=days_after_current)).weekday()

    return calendar.day_name[week_day_number].lower()
