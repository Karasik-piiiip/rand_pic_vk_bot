"""
Бот для ВКонтакте, отправляющий случайные картинки из своих альбомов. Адрес: https://vk.com/picturerand
"""

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

from random import randint as rnd

import datetime

token = ' ' # Токен от группы ВК.
ses = vk_api.VkApi(token = token)
vk = ses.get_api()
longpoll = VkLongPoll(ses)

owner_id = ' ' # id сообщества( со знаком минуса в начале).

def server_info(user_id, photo):
    """
    Функция для ведения журнала сервера.
    """
    men = vk.users.get(user_ids = user_id)
    men = men[0]
    info = '{0} {1} получил картинку {2} в {3}'.format(men['first_name'], men['last_name'], str(photo), str(datetime.datetime.now()))
    print(info)

def generate_num(min, max, isk):
    """
    Та же функция randint(), только не включающая числа из кортежа <isk>.
    """
    result = rnd(min, max)
    if str(result) in isk:
       result = generate_num(min, max, isk)
    return result

def send_pic(id):
    r_num = generate_num(<min>, <max>, [<Исключение_в_формате_строки>]) # Генерируем id фотографии.
    vk.messages.send(user_id = id, attachment= str('photo' + owner_id + '_' + str(r_num)) , random_id = get_random_id())
    server_info(id, r_num)

def send_pic_chat(chat, user_id):
    r_num = generate_num(<min>, <max>, [<Исключение_в_формате_строки>]) # Генерируем id фотографии.
    vk.messages.send(chat_id = chat, attachment= str('photo' + owner_id + '_' + str(r_num)) , random_id = get_random_id())
    server_info(user_id, r_num)

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.from_user:
                    if event.text == '/pic': # Команда.
                        send_pic(event.user_id)
                if event.from_chat:
                    if event.text == '/pic': # Команда.
                        send_pic_chat(event.chat_id, event.user_id)
    except Exception:
        ### Подразумевается, что будет обработана ошибка 
        ### longpoll, которая переодически вызывается из-за
        ### отсуствия ответа при прослушивании серверов ВКонтакте.
        continue
