import sqlite3

# создаем соединение с базой данных
conn = sqlite3.connect('AssistantDB.db')

# создаем курсор для выполнения запросов
cursor = conn.cursor()

# создаем таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS category (
    id SERIAL NOT NULL,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS product (
    id SERIAL NOT NULL,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price DECIMAL(6) NOT NULL,
    link varchar(255),
    category INTEGER NOT NULL REFERENCES category(id),
    PRIMARY KEY (id)
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS assistant_data (
    msg_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    message VARCHAR(255) NOT NULL
);''')

# добавляем данные в таблицу
cursor.execute("INSERT INTO category (id, name) VALUES (1, 'Классика')")
cursor.execute("INSERT INTO category (id, name) VALUES (2, 'Сезонные')")
cursor.execute("INSERT INTO category (id, name) VALUES (3, 'Трендовые')")
cursor.execute("INSERT INTO category (id, name) VALUES (4, 'Экзотика')")

cursor.execute("INSERT INTO product (id, name, description, price, link, category) VALUES (1, 'Розы «Красная Луна»', "
               "'Красивые крупные цветы с насыщенным красным цветом.', 2500, '1.jpg', 1)")
cursor.execute("INSERT INTO product (id, name, description, price, link, category) VALUES (2, 'Тюльпаны «Радуга»', "
               "'Яркие и насыщенные цвета, подходят для подарка на любой праздник.', 3000, '2.jpg', 1)")
cursor.execute("INSERT INTO product (id, name, description, price, link, category) VALUES (3, 'Лилии «Белый снег»', "
               "'Крупные белые цветы с приятным ароматом.', 1800, '3.jpg', 1)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (4, 'Герберы «Солнечный день»', "
    "'Яркие и насыщенные цвета, поднимут настроение в любую погоду.', 2250, '4.jpg', 2)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (5, 'Ромашки «Луговые»', 'Простые, "
    "но очень красивые цветы, подходят для создания романтического настроения.', 2000, '5.jpg', 2)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (6, 'Пионы «Розовый вихрь»', "
    "'Крупные розовые цветы с нежными лепестками, создадут атмосферу нежности и романтики.', 1000, '6.jpg', 3)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (7, 'Орхидеи «Экзотические»', "
    "'Элегантные и изысканные цветы, подходят для создания особенной атмосферы.', 1500, '7.jpeg', 3)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (8, 'Хризантемы «Осенний букет»', "
    "'Яркие и насыщенные цвета, подходят для создания осеннего настроения.', 1400, '8.jpg', 2)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (9, 'Нарциссы «Весенний заряд»', "
    "'Яркие и насыщенные цвета, поднимут настроение весной.', 1750, '9.jpg', 1)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (10, 'Альстромерии «Радуга»', "
    "'Яркие и насыщенные цвета, подходят для создания праздничной атмосферы.', 2500, '10.jpg', 3)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (11, 'Ранункулюсы «Кокетка»', "
    "'Нежные и красивые цветы, подходят для создания романтической атмосферы.', 1600, '11.jpg', 4)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (12, 'Ирисы «Синий оазис»', "
    "'Красивые и необычные цветы, подходят для создания особенной атмосферы.', 2450, '12.jpg', 1)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (13, 'Эустомы «Розовый вальс»', "
    "'Красивые и нежные цветы, подходят для создания романтической атмосферы.', 1200, '13.jpg', 3)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (14, 'Каллы «Белый танец»', "
    "'Крупные белые цветы с изысканным видом, подходят для создания особенной атмосферы.', 1200, '14.jpg', 1)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (15, 'Фрезии «Лавандовый сон»', "
    "'Нежные и красивые цветы, подходят для создания романтической атмосферы.', 2550, '15.jpg', 4)")
cursor.execute("INSERT INTO product (id, name, description, price, link, category) VALUES (16, 'Гвоздики «Красная "
               "роза»', 'Яркие и насыщенные цвета, подходят для создания праздничной атмосферы.', 1300, '16.jpg', 1)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (17, 'Антуриумы «Красный огонь»', "
    "'Красивые и необычные цветы, подходят для создания особенной атмосферы.', 800, '17.jpg', 2)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (18, 'Лаванда «Французский сад»', "
    "'Ароматные и красивые цветы, подходят для создания романтической атмосферы.', 1400, '18.jpg', 3)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (19, 'Сирень «Фиолетовый вечер»', "
    "'Нежные и красивые цветы, подходят для создания романтической атмосферы.', 1200, '19.jpg', 2)")
cursor.execute(
    "INSERT INTO product (id, name, description, price, link, category) VALUES (20, 'Хамелион «Радужный»', "
    "'Необычные и красивые цветы, подходят для создания особенной атмосферы.', 1200, '20.jpg', 4)")

# сохраняем изменения
conn.commit()

# закрываем соединение с базой данных
conn.close()
