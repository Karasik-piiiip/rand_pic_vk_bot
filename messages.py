"""
Бот для ВКонтакте, отправляющий случайные картинки из своих альбомов. Адрес: https://vk.com/picturerand
"""
import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from random import randint as rnd
import logging
import re

import db_logic

token = ' ' # Токен от группы ВК.
ses = vk_api.VkApi(token = token)
vk = ses.get_api()
longpoll = VkLongPoll(ses)

owner_id = ' ' # id сообщества( со знаком минуса в начале).

k_board = VkKeyboard() # Клавиатура.
k_board.add_button('/pic', color=VkKeyboardColor.POSITIVE, payload={"type": "pic"})

def send_mailing(text):
    users, chats = db_logic.get_table()
    for user in users:
        vk.messages.send(user_id = user, message = text, random_id = get_random_id(), keyboard = k_board.get_keyboard())
    for chat in chats:
        vk.messages.send(chat_id = chat, message = text, random_id = get_random_id(), keyboard = k_board.get_keyboard())


def send_pic(id):
    """Отправляет картинку в личные сообщения. """
    try:
        r_num = rnd(<min>, <max>) # Генерируем id фотографии.
        vk.messages.send(user_id = id, attachment= str('photo' + owner_id + '_' + str(r_num)) , random_id = get_random_id(), keyboard = k_board.get_keyboard())
    except Exception:
        send_pic(id)

def send_pic_chat(chat):
    """Отправляет картинку в чат. """
    try:
        r_num = rnd(<min>, <max>) # Генерируем id фотографии.
        vk.messages.send(chat_id = chat, attachment= str('photo' + owner_id + '_' + str(r_num)) , random_id = get_random_id(), keyboard = k_board.get_keyboard())
    except Exception:
        send_pic_chat(chat)

while True:
    try:
        logging.info('Программа запущена')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.from_user:
                    db_logic.table(event.user_id) # Добавляем в базу пользователя.
                    if event.text == '/pic': # Команда.
                        send_pic(event.user_id)
					if '/ra' in re.findall('/ra', event.text) and event.user_id == <ID_администратора_группы>:
						# Идея в том, чтобы отправлять рассылку
						# прямо из ВКонтакте, написан в лс боту.
                        logging.info('Запрошена команда /ra пользователем %s' % str(event.user_id))
                        send_mailing(event.text[3:])
                if event.from_chat:
                    db_logic.table(chat_id = event.chat_id) # Добавляем в базу беседу.
                    if event.text == '/pic': # Команда.
                        send_pic_chat(event.chat_id)
    except Exception as e:
        ### Подразумевается, что будет обработана ошибка 
        ### HTTPSConnectionPool, которая переодически вызывается 
        ### из-за отсуствия ответа при прослушивании серверов ВКонтакте.
        logging.error('Произошла ошибка: %s' % str(e))
    	continue
