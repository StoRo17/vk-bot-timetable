import command
from data.date import load_week, today
from data.timetable_data import load_timetable
from helpers import change_week, prepare_message


def timetable_for_wednesday():
    timetable = load_timetable()
    week = load_week()

    if today.weekday() > 2:
        week = change_week(week)

    timetable = timetable[week]

    return prepare_message(timetable['wednesday'])


timetable_for_wednesday_command = command.Command()
timetable_for_wednesday_command.keys = ['пары среда', 'пср', 'рср']
timetable_for_wednesday_command.description = 'расписание на среду'
timetable_for_wednesday_command.handle = timetable_for_wednesday
