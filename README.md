# rand_pic_vk_bot
Бот для ВКонтакте, отправляющий случайные картинки из своих альбомов.

В функции 
```
def send_pic(id):
    r_num = generate_num(<min>, <max>, [<Исключение_в_формате_строки>]) # Генерируем id фотографии.
    vk.messages.send(user_id = id, attachment= str('photo' + owner_id + '_' + str(r_num)) , random_id = get_random_id())
    server_info(id, r_num)

```
значения min и max должны быть цельночисленными. Кортеж, передаваемый в функцию generate_num() должен содержать те значения, находящиеся в промежутке от min до max, которые нельзя возвращать, в формате строки. 

![param](https://sun9-9.userapi.com/impg/m5gnIXzO89K1gYO2XWrl8AWg5LkYgB8RxCrHfw/GBQRfFfHy_o.jpg?size=390x148&quality=96&sign=ccadfcbe889db088eee7e4925bb38151&type=album)

Узнать номер фотографии можно по ссылке на неё. Число, стоящее после символа нижнего подчеркивания и есть значение, которое требуется (например, на приложенной фотографии это 457239017). 

Бот, работающий на этом коде: https://vk.com/picturerand
