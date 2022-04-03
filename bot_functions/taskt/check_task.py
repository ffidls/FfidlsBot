'''
import vk_api


class check_vk:
    def __init__(self):
        pass

    def ID(self, id):
        login, password = 'ваш телефон', 'ваш пароль'
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api()
        response = vk.users.get(user_id=id)
        return response[0]['id']


    def Friends(self, id, numer, psw):
        login, password = numer, psw
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api()
        response = vk.friends.get(user_id=id)
        return response['count']


    def Photos(self, id, number, psw):
        login, password = number, psw
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api()
        response = vk.users.get(user_id=id, fields='counters')
        return response[0]['counters']['photos']

'''