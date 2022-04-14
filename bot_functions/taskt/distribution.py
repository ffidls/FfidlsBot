from telegram import ReplyKeyboardMarkup
import data.work_with_data


def distribution(update, context):
    id_tlg = update.message.from_user.id
    id_tlg = str(id_tlg)
    data_tsk = data.work_with_data.work_with_data_take()
    dck_user = data_tsk.make_dck_fail()
    num_task, condition, id_bd = dck_user[id_tlg][2], dck_user[id_tlg][3], dck_user[id_tlg][0]
    tsk_text = get_txt_task()


    if num_task == '1' and condition == 'n':
        markup = ReplyKeyboardMarkup([['начать', '/menu']], one_time_keyboard=True)

        update.message.reply_text(f'Что ж, предлагаю начать с самого первого задания')
        update.message.reply_text(tsk_text['1'])
        update.message.reply_text(f'Расскажу вам несложные правила. Задание начинается сразу после того, когда вы нажмете '
                                  f'команду начать, и закончится, в тот же момент, если вы нажмете команду завершить. '
                                  f'Бот сам проверяет на успешность выполнение задач, если вы выполняете все удачно, то вам начисляется '
                                  f'1 балл. Удачи)')
        update.message.reply_text(f'Как только вы будете готовы выберите в меню  "начать", если хотите '
                                  f'назад, то введите "menu"', reply_markup=markup)
        return 1

    if num_task == '2' and condition == 'n':
        markup = ReplyKeyboardMarkup([['начать', '/menu']], one_time_keyboard=True)
        update.message.reply_text(f'Перейдем ко второму заданию')
        update.message.reply_text(tsk_text['2'])
        update.message.reply_text(f'Как только вы будете готовы выберите в меню  "начать", если хотите '
                                  f'назад, то введите "menu"', reply_markup=markup)
        return 1

    if num_task == '3' and condition == 'n':
        markup = ReplyKeyboardMarkup([['начать', '/menu']], one_time_keyboard=True)
        update.message.reply_text(f'Перейдем к третьему заданию')
        update.message.reply_text(tsk_text['3'])
        update.message.reply_text(f'Здесь проверка будет по другому происходить. Как только вы закончите '
                                  f'с заданием вам нужно будет отправить название вашего канала, это название прийдет админу, '
                                  f'который уже сам и будет проверять содержание канала и активность, и именно '
                                  f'он будет принимать решение на зачет задания')
        update.message.reply_text(f'Как только вы будете готовы выберите в меню  "начать", если хотите '
                                  f'назад, то введите "menu"', reply_markup=markup)
        return 1


    if condition == 'd':
        markup = ReplyKeyboardMarkup([['завершить', '/menu']], one_time_keyboard=True)
        update.message.reply_text(f'Если вы завершили работу над заданием, нажмите завершить', reply_markup=markup)
        return 1


def get_txt_task():
    fail = open("bot_functions/taskt/task_txt", encoding='UTF-8')
    dck = {}
    for tsk in fail:
        num, text = tsk[0], tsk[1:]
        dck[num] = text
    return dck
