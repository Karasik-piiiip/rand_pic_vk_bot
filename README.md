# rand_pic_vk_bot
Бот для ВКонтакте, отправляющий случайные картинки из своих альбомов.

В функции 
```
def send_pic(id):
    owner_id = ' ' # id сообщества.
    a = rnd(<min>, <max>) # Генерируем id фотографии по наименьшему значению ссылки и наибольшему
    vk.messages.send(user_id = id, attachment= str('photo' + owner_id + '_' + str(a)) , random_id = get_random_id())

```
значения <min> и <max> должны быть цельночисленными. Узнать номер фотографии можно по ![ссылке](https://vk.com/photo-205278569_457239267) на неё, где число, стоящее после символа нижнего подчеркивания и есть значение, которое требуется. 
