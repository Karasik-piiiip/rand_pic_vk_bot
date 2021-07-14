# rand_pic_vk_bot
Бот для ВКонтакте, отправляющий случайные картинки из своих альбомов.

В функции ```send_pic()``` значения ```min``` и ```max``` должны быть цельночисленными. Они означают номер фотографии в любом альбоме группы.
```
def send_pic(id):
    try:
        r_num = rnd(<min>, <max>) # Генерируем id фотографии.
        vk.messages.send(user_id = id, attachment= str('photo' + owner_id + '_' + str(r_num)) , random_id = get_random_id(), keyboard = k_board.get_keyboard())
    except Exception:
        send_pic(id)
```

![param](https://sun9-9.userapi.com/impg/m5gnIXzO89K1gYO2XWrl8AWg5LkYgB8RxCrHfw/GBQRfFfHy_o.jpg?size=390x148&quality=96&sign=ccadfcbe889db088eee7e4925bb38151&type=album)

Узнать номер фотографии можно по ссылке на неё. Число, стоящее после символа нижнего подчеркивания и есть значение, которое требуется (например, на приложенной фотографии это 457239017). 
Для значения ```min``` следует брать самую старую фотокарточку в группе, и наоборот, для ```max``` - самую новую.

Бот, работающий на этом коде: https://vk.com/picturerand
