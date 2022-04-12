from telegram import ReplyKeyboardMarkup
import data.work_with_data


def start_task(update, context):
    user = update.message.text
    id_tlg = update.message.from_user.id

    data_tsk = data.work_with_data.work_with_data_take()
    dck_user = data_tsk.make_dck_fail()
    num_task, condition, id_bd = dck_user[id_tlg][2], dck_user[id_tlg][3], dck_user[id_tlg][0]

    data_vk = data_tsk.dck_vk_user()
    dck_user = data_vk[id_bd]

    if user == 'начать':
        if num_task == '1':
            # добавление нынешнего количества друзей check(id_vk) = frs
            # data_vk[id_bd][4] = frs
            dck_user[2] = 'd'



def vk_users(id, ):
    pass