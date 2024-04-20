![workflow](https://github.com/alexey32134/kittygram_final/actions/workflows/main.yml/badge.svg?event=push)

### Описание:

Проект, в который публикуют фото котов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram_backend.git
```

```
cd kittygram_backend
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


<h2>Проект разворачивается в контейнерах</h2>
Команда docker compose -f docker-compose.production.yml up -
разворачивает 4 контейнера:
- backend
- frontend
- gateway
- postgres


<h1>Стек использованных технологий:</h1>

```
Python
```

```
Django
```

```
Javascript
```

```
React
```

<h1>Переменные окружения .env</h1>
<h2>для postgres</h2>
POSTGRES_DB - название базы данных (необязательная переменная, по умолчанию совпадает с POSTGRES_USER),
POSTGRES_USER - имя пользователя БД (необязательная переменная, значение по умолчанию — postgres),
POSTGRES_PASSWORD - пароль пользователя БД (обязательная переменная для создания БД в контейнере),
DB_HOST - адрес, по которому Django будет соединяться с базой данных.,
DB_PORT - порт, по которому Django будет обращаться к базе данных.
<h2>для settings</h2>
DEBUG - Режим разработки(True/False),
ALLOWED_HOSTS - по умолчанию ['localhost', '127.0.0.1']
