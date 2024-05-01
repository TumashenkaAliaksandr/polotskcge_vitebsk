import pyowm

def get_weather():
    city = 'Полоцк'
    api_key = '1cf35ad39537a5446d53689cdd3da27a'
    owm = pyowm.OWM(api_key)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    weather_data = {
        'temperature1': w.temperature('celsius')['temp'],  # Подставьте актуальные данные о температуре для каждого дня
        'temperature2': w.temperature('celsius')['temp'],
        'temperature3': w.temperature('celsius')['temp']
    }
    return weather_data
