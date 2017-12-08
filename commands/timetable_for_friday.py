import command
from data.date import load_week, today
from data.timetable_data import load_timetable
from helpers import change_week, prepare_message


def timetable_for_friday():
    timetable = load_timetable()
    week = load_week()

    if today.weekday() > 4:
        week = change_week(week)

    timetable = timetable[week]

    return prepare_message(timetable['friday'])


timetable_for_friday_command = command.Command()
timetable_for_friday_command.keys = ['пары пятница', 'ппт', 'рпт']
timetable_for_friday_command.description = 'расписание на пятницу'
timetable_for_friday_command.handle = timetable_for_friday
