from telegram import ReplyKeyboardMarkup


def menu(update, context):
    word_password = update.message.text

    markup = ReplyKeyboardMarkup([['/users', '/task'], ['/from users']], one_time_keyboard=True)
    update.message.reply_text(
        "Какая информация вам нужна?",
        reply_markup=markup
    )
