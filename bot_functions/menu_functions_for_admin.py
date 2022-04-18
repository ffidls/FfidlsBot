from telegram import ReplyKeyboardMarkup


def menu(update, context):
    word_password = update.message.text

    markup = ReplyKeyboardMarkup([['/read_reviews', '/check_task']], one_time_keyboard=False)
    update.message.reply_text(
        "Какая информация вам нужна?",
        reply_markup=markup
    )
