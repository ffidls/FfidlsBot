from telegram.ext import Updater, CommandHandler


def menu_advice(update, context):
    update.message.reply_text('Выберите по чему именно вам нужен совет.\n'
                              '1 - как начать знакомство\n'
                              '2 - на какие темы можно поговорить\n'
                              '3 - как не волноваться при разговоре\n'
                              'Если вы хотите вернуться, то введите /back')
