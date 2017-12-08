import command
from data.date import load_week
from data.timetable_data import load_timetable
from helpers import prepare_message, translate_day


def timetable_for_this_week():
    timetable = load_timetable()
    week = load_week()

    message = ''
    timetable = timetable[week]
    for day in timetable:
        message += translate_day(day) + ':\n\n' + prepare_message(timetable[day]) +\
            '----------------------------------\n\n'

    return message


timetable_for_this_week_command = command.Command()
timetable_for_this_week_command.keys = ['расп неделя', 'рн']
timetable_for_this_week_command.description = 'расписание на эту неделю'
timetable_for_this_week_command.handle = timetable_for_this_week
