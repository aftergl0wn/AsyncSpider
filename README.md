# Проект AsyncSpider
Автор: Анастасия Давыдова  
Асинхронный парсер документации, который собирает информацию с нескольких страниц сайта.  

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/aftergl0wn/AsyncSpider.git
```

```
cd AsyncSpider
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запуск парсера:

```
scrapy crawl pep
```
