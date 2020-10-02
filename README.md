Необходимо сделать приложение для добавления оборудования в базу данных. 

Интерфейс должен содержать:

1. Поле textarea для ввода серийных номеров (в каждой строке свой серийный номер).

2. Поле тип оборудования (значения – из справочника типов оборудования).

3. Кнопка «Добавить».

Запуск web-приложения:

1)Проверить установку Python, flask, MySQL, SQLAlchemy
Либо запустить установку requirements.txt командой 
pip install -r requirements.txt -v.

2)Выполнить действия в MySQL
2.1)Перейти в режим bash
2.2)CREATE DATABASE test_work;

3)Перейти в проект equipment
3.1)Написать актуальные данные для подключения к MySQL в /equipment/config.py (DATABASE_URI)
3.2)Запустить Python console
3.3)Создать таблицы с помощью команд
from add_eqipment.database import init_db
init_db()
3.4)Добавить типы оборудования для тестирования
INSERT INTO type_equipment (type_name, mask_serial_number) 
VALUES ('TP-Link TL-WR74', 'XXAAAAAXAA'),('D-Link DIR-300','NXXAAXZXaa'),('D-Link DIR-300 S', 'NXXAAXZXXX');

4)Запустить сервер flask

5)Открыть /equipment/front/index.html

6)Тестировать управление
