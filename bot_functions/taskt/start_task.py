from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import data.work_with_data


def start_task(update, context):
    user = update.message.text
    id_tlg = update.message.from_user.id
    id_tlg = str(id_tlg)

    data_tsk = data.work_with_data.work_with_data_take()
    add_inf = data.work_with_data.add_data_in_bd()
    dck_user_tsk = data_tsk.make_dck_fail()
    num_task, condition, id_bd = dck_user_tsk[id_tlg][2], dck_user_tsk[id_tlg][3], dck_user_tsk[id_tlg][0]

    data_vk = data_tsk.dck_vk_user()


    if user == 'начать':
        if num_task == '1':
            # добавление нынешнего количества друзей check(id_vk) = frs
            # data_vk[id_bd][4] = frs
            dck_user_tsk[id_tlg][3] = 'd'
            add_inf.add_new_inf(dck_user_tsk, data_vk)
        if num_task == '2':
            # проверка на количество фото
            dck_user_tsk[id_tlg][3] = 'd'
            add_inf.add_new_inf(dck_user_tsk, data_vk)
        if num_task == '3':
            dck_user_tsk[id_tlg][3] = 'd'
            add_inf.add_new_inf(dck_user_tsk, data_vk)

        markup = ReplyKeyboardMarkup([['/menu']], one_time_keyboard=True)
        update.message.reply_text(f'Удачи с заданием! Жду от вас хороших результатов. Предлагаю перейти назад в меню'
                                  f'', reply_markup=markup)
        return ConversationHandler.END

    elif user == 'завершить':
        flag = False
        if num_task == '1':
            now_friends = int(data_vk[id_bd][3]) + 2  # для 100% прохождение задания
            if int(now_friends) - int(data_vk[id_bd][3]) == 2:
                data_vk[id_bd][3] = now_friends
                flag = True
        if num_task == '2':
            now_photo = int(data_vk[id_bd][2]) + 2
            if now_photo - int(data_vk[id_bd][2]) == 2:
                data_vk[id_bd][2] = now_photo
                flag = True
        if num_task == '3':
            update.message.reply_text('Введите пожалуйста название вашего канала')
            return 3

        if flag:
            markup = ReplyKeyboardMarkup([['/menu', '/task']])
            update.message.reply_text(f'Поздравляю, вы успешно прошли {num_task} задание,'
                                      f'вы получаете 1 бал, если вы хотите продолжить выберите дальше',
                                      reply_markup=markup)
            dck_user_tsk[id_tlg][3], dck_user_tsk[id_tlg][2] = 'n', int(dck_user_tsk[id_tlg][2]) + 1
            add_inf.add_new_inf(dck_user_tsk, data_vk)
            return ConversationHandler.END
        elif not flag:
            markup = ReplyKeyboardMarkup([['/menu', '/task']])
            update.message.reply_text(f'К сожалению, вы не справились с заданием, попробуйте еще раз',
                                      reply_markup=markup)
            return ConversationHandler.END
