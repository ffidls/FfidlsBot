import data.work_with_data
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler


def check(update, context):

        check_data = data.work_with_data.check_data_from_bd()
        add_data = data.work_with_data.add_data_in_bd()
        text_user = str(update.message.text)
        user, password = str(text_user.split('/')[0]), str(text_user.split('/')[1])

        check_user, id_in_bd = check_data.check_user(user, password)

        if check_user:
            new_user_id = update.message.from_user.id
            add_data.add_user(new_user_id, user)
            add_data.add_inf_for_task(id_in_bd, user, update.message.from_user.id)

            markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=False)
            update.message.reply_text(
                f'Привет {user}!Теперь я вас запомню). Теперь предлагаю перейти в меню',
                reply_markup=markup)
            return ConversationHandler.END
        else:
            update.message.reply_text(f'Ох, я не могу вас найти, '
                                      f'похоже вы что-то ввели не так, попробуйте еще раз')
            return 1
