from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import data.work_with_data


def write_reviews(update, context):
    update.message.reply_text('Пожалуйста оставите отзыв на наш проект, мы будем очень '
                              'благодарны, ведь это поможет нам его улучшить)')
    return 1


def add_reviews(update, context):
    reviews_user = str(update.message.text)
    add_rev = data.work_with_data.add_data_in_bd()
    add_rev.add_reviews(reviews_user)

    markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=False)
    update.message.reply_text(
        f'Спасибо за ваш отзыв, он будет отправлен админам, предлагаю перейти в меню',
        reply_markup=markup)
    return ConversationHandler.END
