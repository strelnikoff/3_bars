﻿# 3_bars

# Описание скрипта

Данный скрипт умеет показвать наименьший, наибольший (по колличеству мест) бары,а также определять ближайший бар относительно заданной координаты. Для работы потребуется json файл который можно загрузить по адресу:

[http://data.mos.ru/opendata/7710881420-bary](data.mos.ru/opendata/7710881420-bary)

Для запуска потребуется Python берсии 3 и более.

# Запуск

Запуск осуществляется командой:
>    python3 bars.py [аргументы] [путь к файлу json]

>    biggest   покажет самый большой бар

>    minimal   покажет самый маленький бар

>    closest {longitude, latitude}    покажет самый близкий бар относительно заданных координат 

>    -h, help        покажет справку по скрипту
