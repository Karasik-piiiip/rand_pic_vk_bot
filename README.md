# rand_pic_vk_bot
Бот для ВКонтакте, отправляющий случайные картинки из своих альбомов.

В функции 
```
def send_pic(id):
    owner_id = ' ' # id сообщества.
    a = rnd(<min>, <max>) # Генерируем id фотографии по наименьшему значению ссылки и наибольшему
    vk.messages.send(user_id = id, attachment= str('photo' + owner_id + '_' + str(a)) , random_id = get_random_id())

```
значения <min> и <max> должны быть цельночисленными. Узнать номер фотографии можно по ссылке на неё:
    ![param](https://sun9-9.userapi.com/impg/m5gnIXzO89K1gYO2XWrl8AWg5LkYgB8RxCrHfw/GBQRfFfHy_o.jpg?size=390x148&quality=96&sign=ccadfcbe889db088eee7e4925bb38151&type=album)  
Число, стоящее после символа нижнего подчеркивания и есть значение, которое требуется. 
