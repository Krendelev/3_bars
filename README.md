# Ближайшие бары

Скрипт `bars.py` для нахождения самого большого, самого маленького и самого близкого бара в предоставленном списке.

## Как запустить

Для запуска скрипта укажите путь до файла `JSON` со списком баров и свои координаты в формате `долгота`, `широта`. Список можно взять на сайте [data.mos.ru](https://data.mos.ru/opendata/7710881420-bary)

```bash

$ python3 bars.py bar_list.json 37.586959 55.752179

Самый большой бар – Спорт бар «Красная машина»
Мест: 450
Адрес: Автозаводская улица, дом 23, строение 1

Самый маленький бар – БАР. СОКИ
Мест: 0
Адрес: Дубравная улица, дом 34/29

Самый близкий бар – Brash and Blow
Мест: 20
Адрес: улица Новый Арбат, дом 21

```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
