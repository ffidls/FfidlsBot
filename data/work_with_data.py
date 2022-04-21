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
        photo = cur.execute("""SELECT vk_photos FROM users""").fetchall()
        friends = cur.execute("""SELECT vk_friends FROM users""").fetchall()
        vk = cur.execute("""SELECT vk FROM users""").fetchall()

        for i in range(len(names)):
            print(f'{id[i]}@{names[i]}@{passwords[i]}@{photo[i]}@{friends[i]}@{vk[i]}', file=f)
        f.close()
        con.close()

    def make_dck_fail(self):
        # создание словаря из данных tsk
        fail = open("data/inf_tsk", encoding='UTF-8')
        dck = {}
        for data in fail:
            id_bd, user, numb_tsk, condition, id_tlg = data.split('@')[0], data.split('@')[1], data.split('@')[2], \
                                                      data.split('@')[3], data.split('@')[4].replace("\n","")
            dck[id_tlg] = [id_bd, user, numb_tsk, condition]
        return dck

    def dck_vk_user(self):
        fail = open("data/data_bd", encoding='UTF-8')
        dck = {}
        for data in fail:
            id, name, password, photo, friends, vk = data.split('@')[0], data.split('@')[1], data.split('@')[2], \
                                               data.split('@')[3], data.split('@')[4], data.split('@')[5].replace("\n","")
            dck[id] = [name, password, photo, friends, vk]
        return dck

    def wait_user(self):
        f = open("data/for_admins", encoding='UTF-8')
        dck = {}
        for data in f:
            data = data.replace("@@","@")
            id_tlg, name_k, cond = data.split('@')
            dck[id_tlg] = [name_k, cond.replace("\n","")]
        return dck

    def take_reviews(self):
        f = open("data/reviews", encoding='UTF-8')
        dck = {}
        for r in f:
            rev, cond = r.split('@')
            dck[cond.replace("\n","")] = rev
        return dck



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
            return False, None, None
        except Exception:
            return False, None, None

    def check_task_3(self, id_tlg):
        fail = open("data/for_admins", encoding='UTF-8')
        for i in fail:
            id1, cond = i.split('@')[0], i.split('@')[2].replace("\n","")
            if id1 == id_tlg and cond == 'y':
                return True
        return False


class add_data_in_bd:
    def __init__(self):
        pass

    def add_user(self, id_user, name_user):
        # добавление ников зарегистрированных пользователей
        f = open("data/registered_user", 'a')
        print(f"{id_user}@{name_user}", file=f)
        f.close()

    def add_inf_for_task(self, id_user, name_user, id_tlg):
        f1 = open("data/inf_tsk", 'a')
        print(f"{id_user}@{name_user}@1@n@{id_tlg}",file=f1)
        f1.close()

    def add_new_inf(self, dck_task, dck_vk):
        f_data_bd = open("data/data_bd", 'w')
        f_inf_tsk = open("data/inf_tsk", 'w')

        for key in dck_vk.keys():
            name, psw, ph, frd, vk = dck_vk[key]
            print(f"{key}@{name}@{psw}@{ph}@{frd}@{vk}", file=f_data_bd)
        for key2 in dck_task:
            id_bd, user, tsk, cond = dck_task[key2]
            print(f"{id_bd}@{user}@{tsk}@{cond}@{key2}", file=f_inf_tsk)
        f_inf_tsk.close()
        f_data_bd.close()

    def for_admins(self, id_user, name_tlg):
        f = open("data/for_admins", 'a')
        print(f'{id_user}@{name_tlg}@w', file=f)
        f.close()

    def change_cond(self, dck):
        f = open("data/for_admins", 'w')
        for i in dck.keys():
            id_tlg, name, cond = i, dck[i][0], dck[i][1]
            print(f'{id_tlg}@{name}@{cond}', file=f)
        f.close()

    def add_reviews(self, reviews, fl=True):
        if not fl:
            f = open("data/reviews", 'w')
            for i in reviews.keys():
                print(f'{reviews[i]}@f', file=f)
            f.close()
        else:
            f = open("data/reviews", 'a')
            print(f'{reviews}@n', file=f)
            f.close()
