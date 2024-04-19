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
POSTGRES_DB,
POSTGRES_USER,
POSTGRES_PASSWORD,
DB_NAME,
DB_HOST,
DB_PORT
<h2>для settings</h2>
DEBUG,
ALLOWED_HOSTS

<h2>Проект разворачивается в контейнерах</h2>
Для локального запуска используйте: docker compose up