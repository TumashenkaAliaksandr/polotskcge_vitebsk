import pyowm
from datetime import datetime
import locale
import calendar

# Устанавливаем локаль на русский
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

def get_wind_direction(degrees):
    if degrees < 45 or degrees >= 315:
        return 'С'
    elif 45 <= degrees < 135:
        return 'В'
    elif 135 <= degrees < 225:
        return 'Ю'
    elif 225 <= degrees < 315:
        return 'З'
    else:
        return ''

def get_weather():
    city = 'Полоцк'
    api_key = '1cf35ad39537a5446d53689cdd3da27a'
    owm = pyowm.OWM(api_key)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    # Получаем сегодняшнюю дату
    today = datetime.today()
    # Получаем день недели (0 - понедельник, 1 - вторник, ..., 6 - воскресенье)
    weekday_dict = {
        0: 'Понедельник',
        1: 'Вторник',
        2: 'Среда',
        3: 'Четверг',
        4: 'Пятница',
        5: 'Суббота',
        6: 'Воскресенье'
    }
    weekday = weekday_dict[today.weekday()]

    # Получаем номер дня месяца
    day_of_month = today.day

    # Получаем номер месяца (1 - январь, 2 - февраль, ..., 12 - декабрь)
    month_number = today.month

    # Получаем название месяца
    month_name = calendar.month_name[month_number]

    # Форматируем дату в переменную date
    date = today.strftime("%d %B %Y")  # Изменяем формат даты на "день месяц год"

    weather_data = {
        'day': weekday,          # День недели
        'date': date,            # Дата
        'day_of_month': day_of_month,  # Номер дня месяца
        'month': month_name,     # Название месяца
        'temperature': w.temperature('celsius')['temp'],
        'wind_speed': w.wind()['speed'],
        'wind_direction': get_wind_direction(w.wind()['deg']),
        'pressure': w.pressure['press']
    }
    return weather_data
