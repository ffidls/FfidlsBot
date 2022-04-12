from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import data.work_with_data


def start_task(update, context):
    user = update.message.text
    id_tlg = update.message.from_user.id
    id_tlg = str(id_tlg)

    data_tsk = data.work_with_data.work_with_data_take()
    add_inf = data.work_with_data.add_data_in_bd()
    dck_user_tsk = data_tsk.make_dck_fail()
    num_task, condition, id_bd = dck_user_tsk[id_tlg][2], dck_user_tsk[id_tlg][3], dck_user_tsk[id_tlg][0]

    data_vk = data_tsk.dck_vk_user()

    if user == 'начать':
        if num_task == '1':
            # добавление нынешнего количества друзей check(id_vk) = frs
            # data_vk[id_bd][4] = frs
            dck_user_tsk[id_tlg][3] = 'd'
            add_inf.add_new_inf(dck_user_tsk, data_vk)
            update.message.reply_text(f'Удачи с заданием! Жду от вас хороших результатов')
            return ConversationHandler.END
    else:
        pass


def vk_users(id, ):
    pass