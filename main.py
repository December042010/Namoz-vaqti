import requests
import telebot
from telebot import types

from keep_alive import keep_alive

keep_alive()

TOKEN = "6996337014:AAGXq-tQQbjbfT-RIXNdcppTZsPYAMbnzRQ"
bot = telebot.TeleBot(TOKEN)

Jiz_url = 'https://islomapi.uz/api/present/day?region=Jizzax'
Tosh_url = 'https://islomapi.uz/api/present/day?region=Toshkent'
Sam_url = 'https://islomapi.uz/api/present/day?region=Samarqand'
Sir_url = 'https://islomapi.uz/api/present/day?region=Sirdaryo'
Bux_url = 'https://islomapi.uz/api/present/day?region=Buxoro'
Nav_url = 'https://islomapi.uz/api/present/day?region=Navoiy'



@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(True, one_time_keyboard=True)
    Jizzax_butt = types.KeyboardButton("Jizzax")
    Sirdaryo_butt = types.KeyboardButton("Sirdaryo")
    Navoiy_butt = types.KeyboardButton("Navoiy")
    Toshkent_butt = types.KeyboardButton("Toshkent")
    bux_butt = types.KeyboardButton("Buxoro")
    sam_butt = types.KeyboardButton("Samarqand")
    markup.add(Jizzax_butt, Toshkent_butt, sam_butt, Sirdaryo_butt, Navoiy_butt, bux_butt)
    mess = f"Salom <b>{message.from_user.first_name} {message.from_user.last_name}</b>, bu bot <u><b><i>Namoz Vaqtlarini</i></b></u> ko'rsatadi."
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')
    bot.send_message(message.chat.id, "Viloyatni tanlang:", reply_markup=markup)


@bot.message_handler(content_types='text')
def PrayTime(message):
    text = message.text
    if text == 'Jizzax':
        response = requests.get(Jiz_url)
        data = response.json()
        region = data['region']
        date = data['date']
        weekday = data['weekday']
        hijri_date = data['hijri_date']
        hijri_date_date = hijri_date['month'] + ' ' + str(hijri_date['day'])
        hijri_day = str(hijri_date['day'])
        times = data['times']
        fajr = times['tong_saharlik']
        sunrise = times['quyosh']
        dhuhr = times['peshin']
        asr = times['asr']
        maghrib = times['shom_iftor']
        isha = times['hufton']
      
        bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:30 XUFTON.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
    if text == 'Toshkent':
        response = requests.get(Tosh_url)
        data = response.json()
        region = data['region']
        date = data['date']
        weekday = data['weekday']
        hijri_date = data['hijri_date']
        hijri_date_date = hijri_date['month'] + ' ' + str(hijri_date['day'])
        hijri_day = str(hijri_date['day'])
        times = data['times']
        fajr = times['tong_saharlik']
        sunrise = times['quyosh']
        dhuhr = times['peshin']
        asr = times['asr']
        maghrib = times['shom_iftor']
        isha = times['hufton']
        bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:30 XUFTON.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
    if text == 'Samarqand':
        response = requests.get(Sam_url)
        data = response.json()
        region = data['region']
        date = data['date']
        weekday = data['weekday']
        hijri_date = data['hijri_date']
        hijri_date_date = hijri_date['month'] + ' ' + str(hijri_date['day'])
        hijri_day = str(hijri_date['day'])
        times = data['times']
        fajr = times['tong_saharlik']
        sunrise = times['quyosh']
        dhuhr = times['peshin']
        asr = times['asr']
        maghrib = times['shom_iftor']
        isha = times['hufton']
        bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:45 XUFTON.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
    if text == 'Navoiy':
      response = requests.get(Nav_url)
      data = response.json()
      region = data['region']
      date = data['date']
      weekday = data['weekday']
      hijri_date = data['hijri_date']
      hijri_date_date = hijri_date['month'] + ' ' + str(hijri_date['day'])
      hijri_day = str(hijri_date['day'])
      times = data['times']
      fajr = times['tong_saharlik']
      sunrise = times['quyosh']
      dhuhr = times['peshin']
      asr = times['asr']
      maghrib = times['shom_iftor']
      isha = times['hufton']
      bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:50 XUFTON.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
    if text == 'Buxoro':
      response = requests.get(Bux_url)
      data = response.json()
      region = data['region']
      date = data['date']
      weekday = data['weekday']
      hijri_date = data['hijri_date']
      hijri_date_date = hijri_date['month'] + ' ' + str(hijri_date['day'])
      hijri_day = str(hijri_date['day'])
      times = data['times']
      fajr = times['tong_saharlik']
      sunrise = times['quyosh']
      dhuhr = times['peshin']
      asr = times['asr']
      maghrib = times['shom_iftor']
      isha = times['hufton']
      bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:50 XUFTON.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
bot.polling(non_stop=True)