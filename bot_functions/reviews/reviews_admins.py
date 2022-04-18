from telegram import ReplyKeyboardMarkup
import data.work_with_data


def choice_reviews(update, context):
    markup = ReplyKeyboardMarkup([['новые', 'все']], one_time_keyboard=False)
    update.message.reply_text('Какие отзывы вы хотите почитать?', reply_markup=markup)
    return 1


def read(update, context):
    take_all_rev, add_rev = data.work_with_data.work_with_data_take(), data.work_with_data.add_data_in_bd()
    all_reviews = take_all_rev.take_reviews()

    if str(update.message.text) == 'новые':
        for rev in all_reviews.keys():
            if rev == 'n':
                update.message.reply_text(all_reviews[rev])
    else:
        for rev in all_reviews.keys():
            update.message.reply_text(all_reviews[rev])

    add_rev.add_reviews(all_reviews, False)
    update.message.reply_text('На этом пока все')
    markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=False)
    update.message.reply_text('Предлагаю вернуть в меню', reply_markup=markup)
