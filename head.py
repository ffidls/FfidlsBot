from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler
import bot_functions.registration.greetings
import bot_functions.registration.user_verification
import bot_functions.menu_functions_for_user
import data.work_with_data
import bot_functions.adviсe.advice_menu
import bot_functions.adviсe.distribution_of_advice
import bot_functions.menu_functions_for_admin
import bot_functions.taskt.distribution
import bot_functions.taskt.start_task
import bot_functions.taskt.third_task
import bot_functions.admins_funct.read_tack
import bot_functions.admins_funct.check_task
import bot_functions.reviews.reviews_users
import bot_functions.reviews.reviews_admins


def check(update, context):
    id_user = update.message.from_user.id
    check_bd = data.work_with_data.check_data_from_bd()
    flg, name, admin_fl = check_bd.check_id(id_user)

    if flg:
        if admin_fl:
            markup = ReplyKeyboardMarkup([['/menu_admin']], one_time_keyboard=False)
            update.message.reply_text(
                f"Здравствуйте, {name} Предлагаю сразу перейти в меню",
                reply_markup=markup)
        else:
            markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=False)
            update.message.reply_text(
                f"Привет {name} Предлагаю сразу перейти в меню",
                reply_markup=markup)
    else:
        markup = ReplyKeyboardMarkup([['/start_dating']], one_time_keyboard=False)
        update.message.reply_text(
            "Привет, так как мы с тобой еще не знакомы предлагаю это исправить",
            reply_markup=markup)


def link_sait(update, context):
    markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=False)
    update.message.reply_text(
        "http://lifeoftheparty.herokuapp.com/?", reply_markup=markup)


def main():
    updater = Updater('5193691590:AAG8nk7g4wFy2CCzDkmig8bOnPUlrlL1k9k', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", check))
    dp.add_handler(CommandHandler("menu", bot_functions.menu_functions_for_user.menu))
    dp.add_handler(CommandHandler("menu_admin", bot_functions.menu_functions_for_admin.menu))
    dp.add_handler(CommandHandler("site", link_sait))


    # регистрация
    greetings_dialog = ConversationHandler(
        entry_points=[CommandHandler('start_dating',  bot_functions.registration.greetings.greetings)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.registration.user_verification.check)],  # регистрация и проверка
        },
        fallbacks=[CommandHandler('menu', bot_functions.menu_functions_for_user.menu)])
    dp.add_handler(greetings_dialog)


    # проверка заданий для админов
    check_task = ConversationHandler(
        entry_points=[CommandHandler('check_task', bot_functions.admins_funct.read_tack.admins_task)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.admins_funct.check_task.answer)],
            0: [MessageHandler(Filters.text, bot_functions.admins_funct.read_tack.admins_task)]
        },
        fallbacks=[CommandHandler('menu', bot_functions.menu_functions_for_user.menu)])
    dp.add_handler(check_task)


    # advice
    advice_dialog = ConversationHandler(
        entry_points=[CommandHandler('advice', bot_functions.adviсe.advice_menu.menu_advice)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.adviсe.distribution_of_advice.distribution_of_advice)],
            # советы
        },
        fallbacks=[CommandHandler('menu', bot_functions.menu_functions_for_user.menu)])
    dp.add_handler(advice_dialog)


    # task
    task_dialog = ConversationHandler(
        entry_points=[CommandHandler('task', bot_functions.taskt.distribution.distribution)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.taskt.start_task.start_task)],
            2: [MessageHandler(Filters.text, bot_functions.taskt.distribution.distribution)],
            3: [MessageHandler(Filters.text, bot_functions.taskt.third_task.thr_task)]
        },
        fallbacks=[CommandHandler('menu', bot_functions.menu_functions_for_user.menu)])
    dp.add_handler(task_dialog)


    # reviews
    reviews_dialog = ConversationHandler(
        entry_points=[CommandHandler('reviews', bot_functions.reviews.reviews_users.write_reviews)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.reviews.reviews_users.add_reviews)],
        },
        fallbacks=[CommandHandler('menu', bot_functions.menu_functions_for_user.menu)])
    dp.add_handler(reviews_dialog)


    # reviews_for_admin
    reviews_for_admin_dialog = ConversationHandler(
        entry_points=[CommandHandler('read_reviews', bot_functions.reviews.reviews_admins.choice_reviews)],
        states={
            1: [MessageHandler(Filters.text, bot_functions.reviews.reviews_admins.read)],
        },
        fallbacks=[CommandHandler('menu', bot_functions.menu_functions_for_user.menu)])
    dp.add_handler(reviews_for_admin_dialog)


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

