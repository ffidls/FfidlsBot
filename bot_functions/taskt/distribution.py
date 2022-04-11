from telegram import ReplyKeyboardMarkup
import data.work_with_data


def distribution(update, context):
    id_tlg = update.message.from_user.id
    data_tsk = data.work_with_data.work_with_data_take()
    dck_user = data_tsk.make_dck_fail(str(id_tlg))
    num_task, condition, id_bd = dck_user[1], dck_user[2], dck_user[3]
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
    elif num_task == '1' and condition == 'd':
        pass


def get_txt_task():
    fail = open("bot_functions/taskt/task_txt", encoding='UTF-8')
    dck = {}
    for tsk in fail:
        num, text = tsk[0], tsk[1:]
        dck[num] = text
    return dck