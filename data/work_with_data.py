import sqlite3
# import bot_functions.taskt.check_task


class work_with_data:
    def __init__(self):
        # self.vk = bot_functions.taskt.check_task.check_vk()
        pass

    def add_results(self):
        pass

    def bd(self):
        # заполнение файла data_bd из общей бд
        f = open("data_bd", 'w')
        con = sqlite3.connect('data/bd/life_of_party(1).sqlite')
        cur = con.cursor()
        names = cur.execute("""SELECT * FROM name""").fetchall()
        passwords = cur.execute("""SELECT * FROM hashed_password""").fetchall()
        for i in range(len(names)):
            print(f'{names[i]}@{passwords[i]}', file=f)
        f.close()
        con.close()

    def make_dck_fail(self): # ??????? смысл его существования
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

    def check_id(self, check_id):
        # проверка на прошлый контакт с пользователем
        fail = open("data/registered_user", encoding='UTF-8')
        for str in fail:
            id, name = str.split('@')[0], str.split('@')[1]
            if '\n' in name:
                name = name[:len(name) - 1]
            if int(id) == check_id:
                if '!' in name:
                    return True, name, True
                return True, name, False
        return False, None

    def add_user(self, id_user, name_user):
        # добавление ников зарегистрированных пользователей
        f = open("data/registered_user", 'a')
        print(f"{id_user}@{name_user}", file=f)
        f.close()

    def add_inf_for_task(self, id_user, name_user, inf_vk):
        '''# добавление информации зарегистрированных пользователей для заданий
        id_vk, psw, number = inf_vk[0], inf_vk[1], inf_vk[2]
        friends = self.vk.Friends(id_vk, psw, number)
        photo = self.vk.Photos(id_vk, psw, number)
        f = open("bot_functions/taskt/task_txt" 'a')
        print(f"{id_user}@{name_user}@1@n@{friends}@{photo}", file=f)  # f"{id_user}@{name_user}@номер задания@в какой стадии выполнения@друзья в вк@фото"
        f.close()'''
        pass
