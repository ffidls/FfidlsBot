import sqlite3


class work_with_data_take:
    def __init__(self):
        pass

    def bd(self): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # заполнение файла data_bd из общей бд
        f = open("data_bd", 'w')
        con = sqlite3.connect('data/bd/life_of_party(1).sqlite')
        cur = con.cursor()
        names = cur.execute("""SELECT name FROM users""").fetchall()
        passwords = cur.execute("""SELECT hashed_password FROM users""").fetchall()
        id = cur.execute("""SELECT id FROM users""").fetchall()
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


class check_data_from_bd:
    def __init__(self):
        pass

    def check_user(self, check_user, check_password):
        # поверка на наличие аккаунта на сайте
        fail = open("data/data_bd", encoding='UTF-8')
        for data in fail:
            user, password, id_bd = data.split('@')[1], data.split('@')[2], data.split('@')[0]
            if '\n' in password:
                password = password[:len(password) - 1]
            if check_user.lower() == user and check_password == password:
                return True, id_bd
        return False, None

    def check_id(self, check_id):
        # проверка на прошлый контакт с пользователем
        fail = open("data/registered_user", encoding='UTF-8')
        try:
            for str in fail:
                id, name = str.split('@')[0], str.split('@')[1]
                if '\n' in name:
                    name = name[:len(name) - 1]
                if int(id) == check_id:
                    if '!' in name:
                        return True, name, True
                    return True, name, False
        except Exception:
            return False, None, None


class add_data_in_bd:
    def __init__(self):
        pass

    def add_user(self, id_user, name_user):
        # добавление ников зарегистрированных пользователей
        f = open("data/registered_user", 'a')
        print(f"{id_user}@{name_user}", file=f)
        f.close()

    def add_inf_for_task(self, id_user, name_user):
        f1 = open("data/inf_for_tasks" 'a')
        print(f"{id_user}@{name_user}@1@n",file=f1)
        f1.close()
