# django_api_and_cinema

Задание 1
Создать API Для хранения данных о товарах. В БД 3 таблицы: Товар и Категория, Производитель. В Таблице товар следующие поля: Наименование, Размер, Производитель, Категория и Цена. В таблице Категория: Наименование. В таблице Производитель: Название фирмы, Страна производитель.
Организовать CRUD с помощью класса APIView (только).

Задание 2
Создать API для онлайн кинотеатра, используя классы ListAPIView и RetrieveUpdateDestroyAPIView. Сериализатор можно создать с использованием ModelSerializers. 
В наличии должны быть следующие таблицы:
Фильмы: Название, Год выпуска, Страна, Режиссёр, Жанр
Режиссер: ФИО, год рождения
Жанр: Название жанра
Афиша: Дата, Фильмы
Организовать связи один-ко-многим для таблиц Фильмы и Режиссер, Жанр; Афиша и Фильмы.
В API можно добавить, посмотреть, изменить и удалить информацию в любой таблице.

