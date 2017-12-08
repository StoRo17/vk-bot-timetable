import command
from data.date import load_week
from data.timetable_data import load_timetable
from helpers import prepare_message, change_week, translate_day


def timetable_for_next_week():
    timetable = load_timetable()
    week = change_week(load_week())

    message = ''
    timetable = timetable[week]
    for day in timetable:
        message += translate_day(day) + ':\n\n' + prepare_message(timetable[day]) + \
            '----------------------------------\n\n'

    return message


timetable_for_next_week_command = command.Command()
timetable_for_next_week_command.keys = ['расп след неделя', 'рсн']
timetable_for_next_week_command.description = 'расписание на следующую неделю'
timetable_for_next_week_command.handle = timetable_for_next_week
