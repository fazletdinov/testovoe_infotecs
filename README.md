# Тестовое задание для Инфотекс

Реализовать HTTP-сервер для предоставления информации по географическим объектам.
Данные взять из географической базы данных GeoNames, по [ссылке](http://download.geonames.org/export/dump/RU.zip).

Проект релизован с помощью Fastapi, SQLAlchemy, SQLite, pytest

## Чтобы запустить проект у себя локально, вам необохимо
Склонировать репозиторий

`git clone https://github.com/fazletdinov/testovoe_infotecs.git`

Далее необходимо создать виртуальное окружение
и установить все необходимые зависимости

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
В директории `database` есть скрипт `filling_in_the_database.py`
для автоматического заполнения вашей базы данных, данными из 
текстового файла RU.txt, в приницпе можете его не запускать,
так как база данных уже будет заполнена
После чего можете запустить скрипт командой

```
python3 script
```
Вышеуказанная команда запустит приложение
### Метод принимает идентификатор geonameid и возвращает информацию о городе

`GET api/v1/cities/geonameid` вернёт информацию о городе.

### Пример запроса
`GET api/v1/cities/12537084`

### Ответ

Успешный ответ приходит с кодом `200 OK` и содержит тело:

```json
{
  "geonameid": 12537084,
  "name": "Urochishche Krestovyy Kust",
  "asciiname": "Urochishche Krestovyy Kust",
  "alternatenames": "Urochishche Krestovyy Kust,Urochishhe Krestovyj Kust,Урочище Крестовый Куст",
  "latitude": 51.48569,
  "longitude": 40.0862,
  "feature_class": "L",
  "feature_code": "AREA",
  "country_code": "RU",
  "cc2": "",
  "admin1_code": "86",
  "admin2_code": "",
  "admin3_code": "",
  "admin4_code": "",
  "population": 0,
  "elevation": "",
  "dem": 166,
  "timezone": "Europe/Moscow",
  "modification_date": "2023-06-16"
}
```

### Пример неудачного запроса
`GET api/v1/cities/1253708`

В случае недуачи, вернет ответ со статусом 404 с телом:

```json
{
  "detail": "Город с id 1253708 не существует"
}
```

### Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией
`GET api/v1/list_cities` возвращает список городов с их информацией.

Параметры:
* `page` – номер страницы
* `size` – количество результатов на страницу

### Пример запроса
`GET api/v1/list_cities?page=3&size=3`

### Ответ
```json
{
  "items": [
    {
      "geonameid": 451753,
      "name": "Zelëntsyno",
      "asciiname": "Zelentsyno",
      "alternatenames": "",
      "latitude": 56.73452,
      "longitude": 34.92011,
      "feature_class": "P",
      "feature_code": "PPL",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "77",
      "admin2_code": "",
      "admin3_code": "",
      "admin4_code": "",
      "population": 0,
      "elevation": "",
      "dem": 159,
      "timezone": "Europe/Moscow",
      "modification_date": "2011-07-09"
    },
    {
      "geonameid": 451754,
      "name": "Zelënaya Niva",
      "asciiname": "Zelenaya Niva",
      "alternatenames": "",
      "latitude": 57.1711,
      "longitude": 34.76977,
      "feature_class": "P",
      "feature_code": "PPL",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "77",
      "admin2_code": "",
      "admin3_code": "",
      "admin4_code": "",
      "population": 0,
      "elevation": "",
      "dem": 160,
      "timezone": "Europe/Moscow",
      "modification_date": "2011-07-09"
    },
    {
      "geonameid": 451755,
      "name": "Zasten’ye",
      "asciiname": "Zasten'ye",
      "alternatenames": "",
      "latitude": 57.27055,
      "longitude": 34.73,
      "feature_class": "P",
      "feature_code": "PPL",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "77",
      "admin2_code": "",
      "admin3_code": "",
      "admin4_code": "",
      "population": 0,
      "elevation": "",
      "dem": 184,
      "timezone": "Europe/Moscow",
      "modification_date": "2011-07-09"
    }
  ],
  "total": 368272,
  "page": 3,
  "size": 3,
  "pages": 122758
}
```

### Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах

При выходе будет дополнительная информация
* `to_the_north` – город, расположенный севернее
* `equal_timezone` – возвращает True, если у городов одинаковые временные зоны. Если разные временые зоны, то возвращает False 
* `difference_timezone` - возвращает разницу между временными зонами
двух городов

### Пример запроса
`GET /api/v1/cities/?city_1=Сосновка&city_2=Добровка`
 
### Ответ
```json
{
  "cities": [
    {
      "geonameid": 461698,
      "name": "Sosnovka",
      "asciiname": "Sosnovka",
      "alternatenames": "Sosnovka,Sosnovo,Сосновка",
      "latitude": 60.01667,
      "longitude": 30.35,
      "feature_class": "P",
      "feature_code": "PPLX",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "66",
      "admin2_code": "",
      "admin3_code": "",
      "admin4_code": "",
      "population": 66227,
      "elevation": "",
      "dem": 23,
      "timezone": "Europe/Moscow",
      "modification_date": "2013-03-29"
    },
    {
      "geonameid": 1507332,
      "name": "Dobrovka",
      "asciiname": "Dobrovka",
      "alternatenames": "Dobrovka,Dobrovskiy,Dobryy,Добровка",
      "latitude": 53.3079,
      "longitude": 79.5179,
      "feature_class": "P",
      "feature_code": "PPL",
      "country_code": "RU",
      "cc2": "",
      "admin1_code": "04",
      "admin2_code": "",
      "admin3_code": "",
      "admin4_code": "",
      "population": 0,
      "elevation": "",
      "dem": 171,
      "timezone": "Asia/Barnaul",
      "modification_date": "2012-01-17"
    }
  ],
  "to_the_north": "Dobrovka",
  "equal_timezone": false,
  "difference_timezone": -4
}
```

### Пример неудачного запроса, не может найти города

### Ответ со статусом 404
```json
{
  "detail": "Города не найдены"
}
```
### Автор
[Idel Fazletdinov - fazletdinov](https://github.com/fazletdinov)