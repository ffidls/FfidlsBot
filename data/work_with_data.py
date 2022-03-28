class work_with_data:
    def __init__(self):
        pass

    def bd(self):
        # заполнение файла data_bd из общей бд
        # f = open("registered_user", 'w')
        pass

    def make_dck_fail(self):
        # создание словаря из данных
        fail = open("data/data_bd", encoding='UTF-8')
        data_dc = {}
        data_dc.keys()
        for data in fail:
            user, password, password_word = data.split('@')[0], data.split('@')[1], data.split('@')[2]
            data_dc[user] = [password_word, password_word]
        return data_dc

    def check_user(self, check_user, check_password):
        # поверка на наличие аккаунта на сайте
        fail = open("data/data_bd", encoding='UTF-8')
        for data in fail:
            user, password = data.split('@')[0], data.split('@')[1]
            if '\n' in password:
                password = password[:len(password) - 1]
            if check_user.lower() == user and check_password == password:
                return True
        return False

    def check_nickname(self, check_nickname):
        # проверка на прошлый контакт с пользователем
        fail = open("data/registered_user", encoding='UTF-8')
        for nickname in fail:
            if '\n' in nickname:
                nickname = nickname[:len(nickname) - 1]
            if nickname == check_nickname:
                return True
        return False

    def add_user(self, name_user):
        # добавление ников зарегистрированных пользователей
        f = open("data/registered_user", 'a')
        print(name_user, file=f)
        f.close()
