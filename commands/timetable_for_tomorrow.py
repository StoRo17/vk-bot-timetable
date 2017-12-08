import command
from data.date import load_week, get_week_day_name
from data.timetable_data import load_timetable
from helpers import prepare_message, change_week


def timetable_for_tomorrow():
    timetable = load_timetable()
    week = load_week()

    if get_week_day_name() == 'sunday':
        week = change_week(week)

    timetable = timetable[week]
    tomorrow = get_week_day_name(1)

    if tomorrow in timetable:
        return prepare_message(timetable[tomorrow])

    return 'Завтра, к сожалению (или к счастью), нет пар'


timetable_for_tomorrow_command = command.Command()
timetable_for_tomorrow_command.keys = ['пары завтра', 'пз', 'рз']
timetable_for_tomorrow_command.description = 'расписание пар на завтра'
timetable_for_tomorrow_command.handle = timetable_for_tomorrow
