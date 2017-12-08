import command
from data.date import load_week, today
from data.timetable_data import load_timetable
from helpers import change_week, prepare_message


def timetable_for_thursday():
    timetable = load_timetable()
    week = load_week()

    if today.weekday() > 3:
        week = change_week(week)

    timetable = timetable[week]

    return prepare_message(timetable['thursday'])


timetable_for_thursday_command = command.Command()
timetable_for_thursday_command.keys = ['пары четверг', 'пчт', 'рчт']
timetable_for_thursday_command.description = 'расписание на четверг'
timetable_for_thursday_command.handle = timetable_for_thursday
