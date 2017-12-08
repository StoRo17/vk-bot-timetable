import command


def help_information():
    message = 'Список всех доступных команд: \n'
    for cmd in command.command_list:
        keys = '/'.join(cmd.keys)
        message += '• ' + keys + ' - ' + cmd.description + '\n\n'

    message += '\nПри вводе команд регистр не важен'

    return message


help_command = command.Command()
help_command.keys = ['помощь', 'помоги', 'help']
help_command.description = 'вывод списка всех доступных команд'
help_command.handle = help_information
