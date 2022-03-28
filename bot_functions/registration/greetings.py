from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler


def greetings(update, context):
    update.message.reply_text(f"Прежде чем перейти к функционалу этого бота, нужно войти в свой профиль."
                              f"Введите пожалуйста через / свой никнейм и пароль. Если вы еще не создали свой аккаунт,"
                              f"то перейдите на сайт")
    return 1

