import requests
import telebot
import os
from telebot import types
from keep_alive import keep_alive

keep_alive()


TOKEN = '6996337014:AAGXq-tQQbjbfT-RIXNdcppTZsPYAMbnzRQ'

bot = telebot.TeleBot(token=os.environ.get(TOKEN))



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
    Navoiy_butt = types.KeyboardButton("Navoiy")
    Toshkent_butt = types.KeyboardButton("Toshkent")
    bux_butt = types.KeyboardButton("Buxoro")
    sam_butt = types.KeyboardButton("Samarqand")
    markup.add(Jizzax_butt, Toshkent_butt, sam_butt, Navoiy_butt, bux_butt)
    mess = f"Salom <b>{message.from_user.first_name} {message.from_user.last_name}</b>, bu bot <u><b><i>Namoz Vaqtlarini</i></b></u> ko'rsatadi."
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')
    bot.send_message(message.chat.id, "Viloyatni tanlang:", reply_markup=markup)


@bot.message_handler(content_types='text')
def PrayTime(message):
    text = message.text
    #Jizzax
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

        if hijri_day == '1':
          saharlik = '5:29'
          iftorlik = '18:32'
        elif hijri_day == '2':
          saharlik = '5:27'
          iftorlik = '18:33'
        elif hijri_day == '3':
          saharlik = '5:26'
          iftorlik = '18:35'
        elif hijri_day == '4':
          saharlik = '5:24'
          iftorlik = '18:37'
        elif hijri_day == '5':
          saharlik = '5:22'
          iftorlik = '18:38'
        elif hijri_day == '6':
          saharlik = '5:20'
          iftorlik = '18:39'
        elif hijri_day == '7':
          saharlik = '5:19'
          iftorlik = '18:40'
        elif hijri_day == '8':
          saharlik = '5:17'
          iftorlik = '18:41'
        elif hijri_day == "9":
          saharlik = '5:15'
          iftorlik = '18:42'
        elif hijri_day == "10":
          saharlik = '5:15'
          iftorlik = '18:43'
        elif hijri_day == '11':
          saharlik = '5:13'
          iftorlik = '18:44'
        elif hijri_day == '12':
          saharlik = '5:12'
          iftorlik = '18:45'
        elif hijri_day == '13':
          saharlik = '5:10'
          iftorlik = '18:46'
        elif hijri_day == '14':
          saharlik = '5:08'
          iftorlik = '18:48'
        elif hijri_day == '15':
          saharlik = '5:06'
          iftorlik = '18:49'
        elif hijri_day == '16':
          saharlik = '5:05'
          iftorlik = '18:50'
        elif hijri_day == '17':
          saharlik = '5:03'
          iftorlik = '18:51'
        elif hijri_day == '18':
          saharlik = '5:01'
          iftorlik = '18:52'
        elif hijri_day == '19':
          saharlik = '4:59'
          iftorlik = '18:53'
        elif hijri_day == '20':
          saharlik = '4:57'
          iftorlik = '18:53'
        elif hijri_day == '21':
          saharlik = '4:56'
          iftorlik = '18:54'
        elif hijri_day == '22':
          saharlik = '4:54'
          iftorlik = '18:55'
        elif hijri_day == '23':
          saharlik = '4:52'
          iftorlik = '18:56'
        elif hijri_day == '24':
          saharlik = '4:50'
          iftorlik = '18:57'
        elif hijri_day == '25':
          saharlik = '4:48'
          iftorlik = '18:58'
        elif hijri_day == '26':
          saharlik = '4:46'
          iftorlik = '18:59'
        elif hijri_day == '27':
          saharlik = '4:44'
          iftorlik = '19:01'
        elif hijri_day == '28':
          saharlik = '4:42'
          iftorlik = '19:02'
        elif hijri_day == '29':
          saharlik = '4:40'
          iftorlik = '19:03'
        elif hijri_day == '30':
          saharlik = '4:39'
          iftorlik = '19:04'
        elif hijri_day == '31':
          saharlik = '4:38'
          iftorlik = '19:04'
        
        bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n<b>{saharlik} SAHARLIK\n\n{iftorlik} IFTORLIK</b>\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:30 XUFTON. Жамоат намози, кетидан ТАРОВЕХ намози.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
        #Toshkent
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
        bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:30 XUFTON. Жамоат намози, кетидан ТАРОВЕХ намози.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
        #Samarqand
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
        bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:45 XUFTON. Жамоат намози, кетидан ТАРОВЕХ намози.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
        #Navoiy
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
      bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:50 XUFTON. Жамоат намози, кетидан ТАРОВЕХ намози.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
      #Buxoro
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
      bot.send_message(message.chat.id, f"بِسْـــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِـــــــــــيم\n{region} {date} {hijri_date_date}\n{weekday}\nSollallohu 'alayka yaa Rosulalloh!\n\n{fajr} BOMDOD\n\n{sunrise} QUYOSH\n\n{dhuhr} PESHIN\n\n{asr} ASR\n\n{maghrib} SHOM\n\n{isha} XUFTON\n\n20:50 XUFTON. Жамоат намози, кетидан ТАРОВЕХ намози.\n\nMasjidlarda jamoat namoziga takbir turli xil vaqtlarda tushiriladi.", parse_mode='html')
bot.polling(non_stop=True)