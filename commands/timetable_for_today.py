import command
from data.date import load_week, get_week_day_name
from data.timetable_data import load_timetable
from helpers import prepare_message


def timetable_for_today():
    timetable = load_timetable()
    week = load_week()
    today = get_week_day_name()

    timetable = timetable[week]

    if today in timetable:
        return prepare_message(timetable[today])

    return 'Сегодня, к сожалению (или к счастью), нет пар'


timetable_for_today_command = command.Command()
timetable_for_today_command.keys = ['пары сегодня', 'пс', 'рс']
timetable_for_today_command.description = 'расписание пар на сегодня'
timetable_for_today_command.handle = timetable_for_today
