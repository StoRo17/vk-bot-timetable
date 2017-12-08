import vk

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(token, user_id, message):
    api.messages.send(access_token=token, user_id=str(user_id), message=message)
