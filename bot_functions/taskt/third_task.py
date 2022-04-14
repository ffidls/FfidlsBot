from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import data.work_with_data


def thr_task(update, context):
    check_name_tlg = update.message.text
    id_tlg = update.message.from_user.id
    id_tlg = str(id_tlg)

    data_tsk = data.work_with_data.work_with_data_take()
    add_inf = data.work_with_data.add_data_in_bd()
    dck_user_tsk = data_tsk.make_dck_fail()
    num_task, condition, id_bd = dck_user_tsk[id_tlg][2], dck_user_tsk[id_tlg][3], dck_user_tsk[id_tlg][0]

    data_vk = data_tsk.dck_vk_user()

    if condition == 'd':
        add_inf.for_admins(id_tlg, check_name_tlg)
        dck_user_tsk[id_tlg][3] = 'w'
        add_inf.add_new_inf(dck_user_tsk, data_vk)
        markup = ReplyKeyboardMarkup([['/menu']])
        update.message.reply_text('Ваш канал отправлен админу, теперь вам всего лишь нужно дождаться решения '
                                  'Сейчас я могу только перейти в меню', reply_markup=markup)
        return ConversationHandler.END
