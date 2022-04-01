from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler


def distribution_of_advice(update, context):
    try:
        advices = get_advices()
        number_advice = update.message.text
        update.message.reply_text(advices[number_advice])

        markup = ReplyKeyboardMarkup([['/advice', '/menu']], one_time_keyboard=True)
        update.message.reply_text('Если вы хотите почитать еще советов - выберите команду '
                                  'advice, а если хотите снова вернуться в меню, то menu',
                                  reply_markup=markup)
        return ConversationHandler.END
    except Exception:
        return ConversationHandler.END


def get_advices():
    fail = open("bot_functions/adviсe/advice_txt", encoding='UTF-8')
    dck = {}
    for adv in fail:
        num, text = adv[0], adv[1:]
        dck[num] = text
    return dck
