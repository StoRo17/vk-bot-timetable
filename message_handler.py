import vkapi
from command import command_list
from commands_loader import load_modules


def get_answer(message_body):
    message = 'Прости, я не могу понять, что ты написал. Для вывода списка доступных команд введи "помощь" ' \
              '(без кавычек)'
    for cmd in command_list:
        if message_body in cmd.keys:
            message = cmd.handle()

    return message


def create_answer(data, token):
    load_modules()
    user_id = data['user_id']
    message = get_answer(data['body'].lower())
    vkapi.send_message(token, user_id, message)
