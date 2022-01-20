import telebot
from telebot import types
from random import randint
import os
import time

bot = telebot.TeleBot('5014594116:AAHpVXrVwyRtrMJI93TEDBmHQCgtXWZdktA')


def check_user(txt, message):
    f = open(txt, 'r')
    we_have = False
    lines = f.readlines()
    for line in lines:
        if line[0:len(line) - 1] == str(message.chat.id):
            we_have = True
    if not we_have:
        f.close()
        f = open(txt, 'a')
        f.write(str(message.chat.id) + '\n')
        bot.send_message(chat_id=2125635674, text='Новый пользователь бота: @' + str(message.from_user.username) + ' : ' + str(message.chat.id))
    f.close()


@bot.message_handler(commands='start')
def dota(message):
    key = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    but = types.KeyboardButton("🎲Рандомный герой🎲")
    key.add(but)
    bot.send_message(chat_id=message.chat.id, text='🔯 Бот который скажет на каком герое поиграть сёдня', reply_markup=key)


@bot.message_handler(commands='updatedrain')
def updatedrain(message):
    bot.send_message(chat_id=message.chat.id, text='Начинаем обновление репозитория на гитхабе (~50 секунд)')
    time.sleep(1)
    cd = os.getcwd()
    os.system('cd ' + str(cd))
    bot.send_message(chat_id=message.chat.id, text='cd ' + str(cd))
    time.sleep(5)
    os.system('git init')
    time.sleep(10)
    os.system('git add .')
    time.sleep(10)
    os.system('git commit -m "new member"')
    time.sleep(10)
    os.system('git pull origin main')
    time.sleep(10)
    os.system('git push -u origin main')
    time.sleep(10)
    bot.send_message(chat_id=message.chat.id, text= 'Репозиторий на гитхабе обновлен')


@bot.message_handler(content_types=['text'])
def text(message):
    rand = randint(1, 3)
    if rand == 1:
        bot.send_photo(chat_id=message.chat.id, caption='♿Паааааааджж♿',
                       photo='http://risovach.ru/upload/2013/11/mem/bombochka_35876964_orig_.jpg')
    if rand == 2:
        bot.send_photo(chat_id=message.chat.id, caption='♿mineeer♿',
                       photo='https://steamuserimages-a.akamaihd.net/ugc/31861554314034185/6605F9776017E5765DC3D9DE7E9D4887E652AC5B/?imw=512&amp;imh=325&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true')
    if rand == 3:
        bot.send_photo(chat_id=message.chat.id, caption='♿Аирлейнс♿',
                       photo='https://cs.pikabu.ru/post_img/2013-01_2/1357669124_46598435.jpg')
    check_user('users_id.txt', message)
    cd = os.getcwd()
    os.system('cd ' + str(cd))


bot.polling(none_stop=True)
