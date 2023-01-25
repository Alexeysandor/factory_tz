# R4C - Robots for consumers

## Чтобы запустить:
В файле setting подключить свою БД и выполнить миграции, заполнить БД данными.
___
## Как я тестировал:
Чтобы протестировать все три задачи я выполнил следующее:
 - Проверил что по энпоинту 'add_robot' в БД успешно создаются новые записи
 - Создал несколько десятков роботов. После этого запускал сервер, и при переходе по адресу http://127.0.0.1:8000/weekly_report 
 скачивал файл, смотрел, чтобы он соответствовал Task2
 - Добавил в модель order поле waiting_list, и благодаря ему выполнил Task3. Через админку создал пользователей. При выполнении post запроса на эндпоинт 'create_order' в случае если робот необходимой серии есть в БД, подобные post запросы можно отправлять без проблем. Если робота необходимой серии нет в БД, заказ создаётся со значением поля waiting_list = True. Если пользователь попробует опять сделать post запрос с этой серией, он получит сообщение что его заказ уже оформлен, и как только робот появится в наличии, ему придёт сообщение. Для сообщений использовал эмулятор почтового сервиса.
 Для отправки письма использовал сигнал. После того, как необходимый робот появляется в БД, пользователю отправляется письмо, и поле waiting_list приобретает статус False.
___
