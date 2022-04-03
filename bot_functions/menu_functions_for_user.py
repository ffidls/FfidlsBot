from telegram import ReplyKeyboardMarkup


def menu(update, context):
    word_password = update.message.text

    markup = ReplyKeyboardMarkup([['/advice', '/task'], ['/site', '/reviews']], one_time_keyboard=True)
    update.message.reply_text(
        "Какая информация вам нужна?",
        reply_markup=markup
    )
