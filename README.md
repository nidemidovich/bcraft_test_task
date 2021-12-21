# Тестовое задание для Bcraft

В этом репозитории содержится решение тестового задания для Bcraft. Задача: разработать микросервис для счетчиков статистики. Сервис должен уметь взаимодействовать с клиентом при помощи REST API.

| URL                                | Метод  | Действие                                                                                                                                                                                                                   |
|------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /api/get_stats/                    | GET    | Показывает всю статистику, отсортированную по дате.                                                                                                                                                                        |
| /api/get_stats/start_date/end_date | GET    | Показывает статистику за определенную дату. Опционально можно добавить параметр sort_by, который примет колонку для сортировки вывода. Если этого параметра нет или поле не опознано, то по умолчанию отсортирует по дате. |
| /api/send_stats/                   | POST   | Сохраняет статистику.                                                                                                                                                                                                      |
| /api/delete_stats/                 | DELETE | Удаляет всю статистику.                                                                                                                                                                                                    |

## Примеры использования
Запрос на показ статистики за определенный промежуток:
```bash
curl http://127.0.0.1:8000/api/get_stats/2021-12-01/2021-12-15/
```
Ответ:
```json
[
    {
        "date": "2021-12-01",
        "views": 7,
        "clicks": 34,
        "cost": "890.10",
        "cpc": 26.18,
        "cpm": 127157.14
    },
    {
        "date": "2021-12-15",
        "views": 1,
        "clicks": 34,
        "cost": "198.65",
        "cpc": 5.84,
        "cpm": 198650.0
    }
]
```
\
Запрос на показ статистики за определенный промежуток с сортировкой по определенному полю:
```bash
curl http://127.0.0.1:8000/api/get_stats/2021-12-01/2021-12-15/?sort_by=views
```
Ответ:
```json
[
    {
        "date": "2021-12-15",
        "views": 1,
        "clicks": 34,
        "cost": "198.65",
        "cpc": 5.84,
        "cpm": 198650.0
    },
    {
        "date": "2021-12-01",
        "views": 7,
        "clicks": 34,
        "cost": "890.10",
        "cpc": 26.18,
        "cpm": 127157.14
    }
]
```
\
Запрос на удаление статистики:
```bash
curl -X DELETE http://127.0.0.1:8000/api/delete_stats/
```
Ответ:
```json
{
    "result": "Success"
}
```
## Запуск
```bash
git clone https://github.com/nidemidovich/bcraft_test_task.git
cd bcraft_test_task
python3 -m venv /path/to/venv/venv_name
source /path/to/venv/venv_name/bin/activate
pip install -r requirements.txt
cd bcraft_api
python manage.py runserver
```