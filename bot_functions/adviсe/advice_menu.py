from telegram import ReplyKeyboardMarkup


def menu_advice(update, context):
    markup = ReplyKeyboardMarkup([['1', '2'], ['3', '/menu']], one_time_keyboard=False)
    update.message.reply_text('Выберите по чему именно вам нужен совет.\n'
                              '1 - как начать знакомство\n'
                              '2 - на какие темы можно поговорить\n'
                              '3 - как не волноваться при разговоре\n'
                              'Если вы хотите вернуться, то введите /menu',
                              reply_markup=markup)
    return 1
