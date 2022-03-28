from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text('work!!!')


def main():
    updater = Updater('5193691590:AAG8nk7g4wFy2CCzDkmig8bOnPUlrlL1k9k', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start1", start))


    updater.start_polling()

    updater.idle()

