import pymorphy2
import sqlite3
from nltk.corpus import stopwords

def preprocess(text):
    morph = pymorphy2.MorphAnalyzer()

    # Токенизация запроса и удаление стоп-слов
    tokens = text.split()
    stop_words = set(stopwords.words('russian'))
    tokens_without_stop_words = [token for token in tokens if not token in stop_words]

    # Лемматизация слов в запросе
    lemmas = [morph.parse(token)[0].normal_form for token in tokens_without_stop_words]
    return lemmas

def product_recommend(tokens):
    cursor.execute("SELECT id FROM product")
    products = cursor.fetchall()

    key_words1 = ['роза']
    key_words2 = ['тюльпан']
    key_words3 = ['лилия']
    key_words4 = ['гербера']
    key_words5 = ['ромашка']
    key_words6 = ['пион']
    key_words7 = ['орхидея']
    key_words8 = ['хризантема']
    key_words9 = ['нарцисс']
    key_words10 = ['альстромерия']
    key_words11 = ['ранункулюс']
    key_words12 = ['ирис']
    key_words13 = ['эустома']
    key_words14 = ['калла']
    key_words15 = ['фрезия']
    key_words16 = ['гвоздика']
    key_words17 = ['антуриум']
    key_words18 = ['лаванда']
    key_words19 = ['сирень']
    key_words20 = ['хамелион']

    if any(key_word in tokens for key_word in key_words1):
        c = products[0]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words2):
        c = products[1]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words3):
        c = products[2]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words4):
        c = products[3]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words5):
        c = products[4]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words6):
        c = products[5]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        returnrecommendation
    elif any(key_word in tokens for key_word in key_words7):
        c = products[6]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words8):
        c = products[7]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words9):
        c = products[8]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words10):
        c = products[9]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words11):
        c = products[10]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words12):
        c = products[11]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words13):
        c = products[12]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words14):
        c = products[13]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words15):
        c = products[14]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words16):
        c = products[15]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words17):
        c = products[16]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words18):
        c = products[17]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words19):
        c = products[18]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    elif any(key_word in tokens for key_word in key_words20):
        c = products[19]
        cursor.execute("SELECT name, description from product WHERE id=?", (c))
        recommendation = cursor.fetchall()
        return recommendation
    else:
        recommend(tokens)

def recommend(tokens):
    cursor.execute("SELECT id FROM category")
    categories = cursor.fetchall()

    # Определение ключевых слов для категорий
    key_words1 = ['классический', 'классика']
    key_words2 = ['сезонный', 'летний']
    key_words3 = ['трендовый', 'тренд', 'популярный']
    key_words4 = ['экзотический', 'экзотика', 'необчный']
    key_words5 = ['подешевле', 'дешёвый', 'недорогой']
    if any(key_word in tokens for key_word in key_words1):
        c = categories[0]
        cursor.execute("SELECT name, description from product WHERE category=?", (c))
        recommendation = cursor.fetchall()
        return(recommendation)
    elif any(key_word in tokens for key_word in key_words2):
        c = categories[1]
        cursor.execute("SELECT name, description from product WHERE category=?", (c))
        recommendation = cursor.fetchall()
        return (recommendation)
    elif any(key_word in tokens for key_word in key_words3):
        c = categories[2]
        cursor.execute("SELECT name, description from product WHERE category=?", (c))
        recommendation = cursor.fetchall()
        return (recommendation)
    elif any(key_word in tokens for key_word in key_words4):
        c = categories[3]
        cursor.execute("SELECT name, description from product WHERE category=?", (c))
        recommendation = cursor.fetchall()
        return (recommendation)
    elif any(key_word in tokens for key_word in key_words5):
        cursor.execute("SELECT name, description from product WHERE price<=1500")
        recommendation = cursor.fetchall()
        return (recommendation)

conn = sqlite3.connect('AssistantDB.db')
cursor = conn.cursor()

msg = input()
tokens = preprocess(msg)

print(tokens)

print('Предлагаемые товары', product_recommend(tokens))

conn.commit()
conn.close()