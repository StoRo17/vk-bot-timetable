import command
from data.date import load_week, get_week_day_name
from data.timetable_data import load_timetable
from helpers import prepare_message, change_week


def timetable_for_day_after_tomorrow():
    timetable = load_timetable()
    week = load_week()
    today = get_week_day_name()

    if today == 'saturday' or today == 'sunday':
        week = change_week(week)

    timetable = timetable[week]
    day_after_tomorrow = get_week_day_name(2)

    if day_after_tomorrow in timetable:
        return prepare_message(timetable[day_after_tomorrow])

    return 'Послезавтра, к сожалению (или к счастью), нет пар'


timetable_for_day_after_tomorrow_command = command.Command()
timetable_for_day_after_tomorrow_command.keys = ['пары послезавтра', 'пп', 'рп']
timetable_for_day_after_tomorrow_command.description = 'расписание пар на послезавтра'
timetable_for_day_after_tomorrow_command.handle = timetable_for_day_after_tomorrow
