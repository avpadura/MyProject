import telebot
import pyowm

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'ua'


owm = pyowm.OWM('Enter Your Key')
bot = telebot.TeleBot('Enter Your Key')


@bot.message_handler(content_types=['text'])


def text_message(message):
    mrg = owm.weather_manager()
    observation = mrg.weather_at_place(message.text)
    w = observation.weather
    w.detailed_status
    w.wind()
    humidity = w.humidity
    temp = w.temperature('celsius')['temp']

    answer = 'У місті ' + message.text + ' на даний момент ' + w.detailed_status + '\n'
    answer += 'Температура повітря орієнтовно ' + str(temp) + ' градусів' + '\n'
    answer += 'Відносна вологість повітря = ' + str(humidity) + '%' + '\n\n'
    if temp < -10:
        answer += "Дуже холодно, одягайтеся дуже тепло!"
    elif temp < 10:
        answer += "Холодно, одягайтеся дуже тепло."
    elif temp > 25:
        answer += "Дуже спекотно."
    else:
        answer += "Приємна погода!"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)

