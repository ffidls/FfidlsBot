from telegram import ReplyKeyboardMarkup


def menu(update, context):
    word_password = update.message.text

    markup = ReplyKeyboardMarkup([['/adviсe', '/rating'], ['/site', '/shop']], one_time_keyboard=True)
    update.message.reply_text(
        "Какая информация вам нужна?",
        reply_markup=markup
    )
