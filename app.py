from bottle import default_app, post, request

from config import confirmation_token, token
import message_handler


@post('/')
def handle():
    data = request.json
    if 'type' not in data.keys():
        return 'This is not VK'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        message_handler.create_answer(data['object'], token)
        return 'ok'


application = default_app()
