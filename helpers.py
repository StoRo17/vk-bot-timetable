from data.timetable_data import load_subjects_time


def prepare_message(day):
    subjects_time = load_subjects_time()

    message = ''
    subject_template = '{0} пара:\n\U0001F393{2}\n\U0001F552 {1}\n\U0001F6AA {3}\nпреп. {4}\n\n'
    for subject_number in day:
        subject_info = day[subject_number]
        message += subject_template.format(subject_number,
                                           subjects_time[subject_number],
                                           subject_info['name'],
                                           subject_info['room'],
                                           subject_info['teacher'])

    return message


def change_week(week):
    if week == 'first_week':
        return 'second_week'

    return 'first_week'


def translate_day(day):
    return {'monday': 'Понедельник',
            'tuesday': 'Вторник',
            'wednesday': 'Среда',
            'thursday': 'Четверг',
            'friday': 'Пятница',
            'saturday': 'Суббота',
            'sunday': 'Воскресенье'}[day]
