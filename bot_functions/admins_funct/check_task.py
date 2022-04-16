from telegram import ReplyKeyboardMarkup
import data.work_with_data


def answer(update, context):
    answer_user = update.message.text
    datas = data.work_with_data.work_with_data_take()
    change_data = data.work_with_data.add_data_in_bd()
    wait_users_dck = datas.wait_user()
    markup = ReplyKeyboardMarkup([['дальше']], one_time_keyboard=False)

    for key in wait_users_dck.keys():
        cond, name = wait_users_dck[key][1], wait_users_dck[key][0]
        if cond == 'w2':
            if answer_user == 'зачет':
                wait_users_dck[key][1] = 'y'
            else:
                wait_users_dck[key][1] = 'n'
        change_data.change_cond(wait_users_dck)
        update.message.reply_text('Предлагаю пройти дальше', reply_markup=markup)

    return 0