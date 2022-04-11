import vk_api


class check_vk:
    def __init__(self):
        pass

    def ID(self, id):
        login, password = '547065524', 'c1a2k3e4'
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api()
        response = vk.users.get(user_id='547065524')
        return response[0]['id']

    def Friends(self, id):
        login, password = '+79312912908', 'c1a2k3e4'
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api()
        response = vk.friends.get(user_id=id)
        return response['count']


    def Photos(self, id):
        vk_session = vk_api.VkApi('id547065524', 'aaaaa6f')
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api()
        response = vk.users.get(user_id=id, fields='counters')
        return response[0]['counters']['photos']


a = check_vk()
print(a.Photos('id547065524'))