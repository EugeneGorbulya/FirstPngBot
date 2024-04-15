import telebot
from tok import token
import psycopg2
from config import dbn, us
import time

TOKEN = token

bot = telebot.TeleBot(TOKEN)
f = open("whiteList.txt", "r")
wl = f.readline()
conn = psycopg2.connect(dbname=dbn, user=us, host='localhost')
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.from_user.username in wl:
        bot.send_message(message.chat.id,"Оцени все картинки в данных категориях товаров. Какую из них ты бы поставил первой?")
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = telebot.types.KeyboardButton(text="Data")
        keyboard.add(button1)
        bot.send_message(message.chat.id,
                         'Выбери категорию',
                         reply_markup=keyboard)

user_states = {}

@bot.message_handler(func=lambda message: message.text == "Data")
def category(message):
    if message.from_user.username in wl:
        query = """
        SELECT MAX(product_id) FROM event WHERE chat_id = %s;
        """
        cursor.execute(query, (message.chat.id,))
        last_product_id = cursor.fetchone()[0]
        if last_product_id:
            user_states[message.chat.id] = {'current_photo': last_photo_number[0] + 1}
        else:
            user_states[message.chat.id] = {'current_photo': 1}
        send_next_photo(message.chat.id)

def send_next_photo(chat_id):
    global current_category
    photo_number = user_states[chat_id]['current_photo']
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = telebot.types.KeyboardButton(text="1")
    b2 = telebot.types.KeyboardButton(text="2")
    b3 = telebot.types.KeyboardButton(text="3")
    b4 = telebot.types.KeyboardButton(text="4")
    b5 = telebot.types.KeyboardButton(text="5")
    ex = telebot.types.KeyboardButton(text="Exit")
    keyboard.add(b1, b2, b3, b4, b5)
    keyboard.add(ex)
    bot.send_media_group(chat_id,
                            [telebot.types.InputMediaPhoto(open(f'Data/{photo_number}/1.png', 'rb')),
                             telebot.types.InputMediaPhoto(open(f'Data/{photo_number}/2.png', 'rb')),
                             telebot.types.InputMediaPhoto(open(f'Data/{photo_number}/3.png', 'rb')),
                             telebot.types.InputMediaPhoto(open(f'Data/{photo_number}/4.png', 'rb')),
                             telebot.types.InputMediaPhoto(open(f'Data/{photo_number}/5.png', 'rb'))])
    bot.send_message(chat_id,
                           'Выбери фотографию',
                           reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in ["1", "2", "3", "4", "5"])
def handle_rating(message):
    if message.from_user.username in wl:
        chat_id = message.chat.id
        photo_number = user_states[chat_id]['current_photo']
        rating = int(message.text)
        cursor.execute(f"""
        UPDATE product SET rank_image_{rating} = rank_image_{rating} + 1
        WHERE id = (
            SELECT product_id FROM event WHERE chat_id = %s ORDER BY id DESC LIMIT 1
        );
        INSERT INTO event (chat_id, product_id, image_index)
        VALUES (%s, %s, %s);
        """, (chat_id, chat_id, photo_number, rating))
        conn.commit()
        user_states[chat_id][f'current_photo'] += 1
        if photo_number <= 250:
            send_next_photo(chat_id)
        else:
            bot.send_message(chat_id, "Спасибо за оценку всех фотографий!")


@bot.message_handler(func=lambda message: message.text == "Exit")
def to_menu(message):
    if message.from_user.username in wl:
        save_last_rate(message.chat.id)
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = telebot.types.KeyboardButton(text="Data")
        keyboard.add(button1)
        bot.send_message(message.chat.id,
                            'Выбери категорию',
                            reply_markup=keyboard)

def save_last_rate(chat_id):
    if chat_id in user_states:
        photo_number = user_states[chat_id]['current_photo'] - 1
        cursor.execute("""
        UPDATE event SET timestamp = CURRENT_TIMESTAMP WHERE chat_id = %s AND product_id = %s
        """, (chat_id, last_photo_number))
        conn.commit()


bot.infinity_polling(none_stop=True,interval=0)
time.sleep(5)
cursor.close()
conn.close()
