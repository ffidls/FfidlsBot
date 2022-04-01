import data.work_with_data
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler


def check(update, context):
    try:
        work_with_data = data.work_with_data.work_with_data()
        text_user = str(update.message.text)
        user, password = str(text_user.split('/')[0]), str(text_user.split('/')[1])

        check_user = work_with_data.check_user(user, password)

        if check_user:
            new_user_id = update.message.from_user.id
            work_with_data.add_user(new_user_id, user)

            markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=False)
            update.message.reply_text(
                f'Привет {user}!Теперь я вас запомню). Теперь предлагаю перейти в меню',
                reply_markup=markup)
            return ConversationHandler.END
        else:
            update.message.reply_text(f'Ох, я не могу вас найти, '
                                      f'похоже вы что-то ввели не так, попробуйте еще раз')
            return 1

    except Exception:
        update.message.reply_text(f'Вы ввели неправильный формат, попробуйте еще раз')
        return 1
