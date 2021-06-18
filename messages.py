"""
Бот для ВКонтакте, отправляющий случайные картинки из своих альбомов. Адрес: https://vk.com/picturerand
"""

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

from random import randint as rnd

token = ' ' # Токен от группы ВК.
ses = vk_api.VkApi(token = token)
vk = ses.get_api()
longpoll = VkLongPoll(ses)

def send_pic(id):
    owner_id = ' ' # id сообщества.
    a = rnd(<min>, <max>) # Генерируем id фотографии по наименьшему значению ссылки и наибольшему
    vk.messages.send(user_id = id, attachment= str('photo' + owner_id + '_' + str(a)) , random_id = get_random_id())

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.text == '/pic':
            send_pic(event.user_id)
        else:
            vk.messages.send(user_id = event.user_id, message = 'unknown message', random_id = 1)
