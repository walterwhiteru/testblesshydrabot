import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('5014594116:AAHpVXrVwyRtrMJI93TEDBmHQCgtXWZdktA')

@bot.message_handler(commands='start')
def dota(message):
    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    but = types.KeyboardButton("🎲Рандомный герой🎲")
    key.add(but)
    bot.send_message(chat_id=message.chat.id, text='🔯 Бот который скажет на каком герое поиграть сёдня', reply_markup=key)


@bot.message_handler(content_types=['text'])
def text(message):
    rand = randint(1, 3)
    if rand == 1:
        bot.send_photo(chat_id=message.chat.id, caption='♿Паааааааджж♿', photo='http://risovach.ru/upload/2013/11/mem/bombochka_35876964_orig_.jpg')
    if rand == 2:
        bot.send_photo(chat_id=message.chat.id, caption='♿mineeer♿', photo='https://steamuserimages-a.akamaihd.net/ugc/31861554314034185/6605F9776017E5765DC3D9DE7E9D4887E652AC5B/?imw=512&amp;imh=325&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true')
    if rand == 3:
        bot.send_photo(chat_id=message.chat.id, caption='♿Аирлейнс♿', photo='https://cs.pikabu.ru/post_img/2013-01_2/1357669124_46598435.jpg')

bot.polling(none_stop=True)
