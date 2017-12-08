import command
from data.date import load_week, today
from data.timetable_data import load_timetable
from helpers import change_week, prepare_message


def timetable_for_tuesday():
    timetable = load_timetable()
    week = load_week()

    if today.weekday() > 1:
        week = change_week(week)

    timetable = timetable[week]

    return prepare_message(timetable['tuesday'])


timetable_for_tuesday_command = command.Command()
timetable_for_tuesday_command.keys = ['пары вторник', 'пвт', 'рвт']
timetable_for_tuesday_command.description = 'расписание на вторник'
timetable_for_tuesday_command.handle = timetable_for_tuesday
