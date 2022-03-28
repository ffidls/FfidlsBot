from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
import bot_functions.registration.greetings
import bot_functions.registration.user_verification
import bot_functions.menu
import data.work_with_data
import bot_functions.adviсe.advice_menu
import bot_functions.adviсe.distribution_of_advice


def check(update, context):
    nickname = update.message.from_user.username
    if str(nickname) == 'None':
        nickname = f'{update.message.chat.first_name}'
    check_nickname = data.work_with_data.work_with_data()


    if check_nickname.check_nickname(nickname):
        markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=False)
        update.message.reply_text(
            f"Привет {nickname}) Предлагаю сразу перейти в меню",
            reply_markup=markup)
    else:
        markup = ReplyKeyboardMarkup([['/start_dating']], one_time_keyboard=False)
        update.message.reply_text(
            "Привет, так как мы с тобой еще не знакомы предлагаю это исправить",
            reply_markup=markup)


def main():
    updater = Updater('5193691590:AAG8nk7g4wFy2CCzDkmig8bOnPUlrlL1k9k', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", check))
    dp.add_handler(CommandHandler("menu", bot_functions.menu.menu))


    # регистрация
    greetings_dialog = ConversationHandler(
        entry_points=[CommandHandler('start_dating',  bot_functions.registration.greetings.greetings)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.registration.user_verification.check)],  # регистрация и проверка
        },
        fallbacks=[CommandHandler('menu', bot_functions.menu.menu)])
    dp.add_handler(greetings_dialog)


    #advice
    advice_dialog = ConversationHandler(
        entry_points=[CommandHandler('advice', bot_functions.adviсe.advice_menu.menu_advice)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.adviсe.distribution_of_advice.distribution_of_advice)],
            # советы
        },
        fallbacks=[CommandHandler('back', bot_functions.menu.menu)])
    dp.add_handler(advice_dialog)


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

