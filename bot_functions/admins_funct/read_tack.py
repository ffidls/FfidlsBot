from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import data.work_with_data


def admins_task(update, context):
    datas = data.work_with_data.work_with_data_take()
    change_data = data.work_with_data.add_data_in_bd()
    wait_users_dck = datas.wait_user()
    markup = ReplyKeyboardMarkup([['/menu_admin']], one_time_keyboard=False)

    for key in wait_users_dck.keys():
        cond, name = wait_users_dck[key][1], wait_users_dck[key][0]
        if cond == 'w':
            markup = ReplyKeyboardMarkup([['зачет', 'незачет']], one_time_keyboard=False)
            update.message.reply_text(name, reply_markup=markup)
            wait_users_dck[key][1] = 'w2'
            change_data.change_cond(wait_users_dck)
            return 1

    update.message.reply_text('Все задания проверены, предлагаю перейти обратно в меню', reply_markup=markup)
    return ConversationHandler.END