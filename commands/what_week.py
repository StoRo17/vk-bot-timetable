import command
from data.date import load_week


def what_week():
    week = load_week()

    if week == 'first_week':
        return 'Сейчас идёт первая (нечётная) неделя'

    return 'Сейчас идёт вторая (чётная) неделя'


what_week_command = command.Command()
what_week_command.keys = ['какая неделя', 'кн']
what_week_command.description = 'какая сейчас идёт неделя'
what_week_command.handle = what_week
