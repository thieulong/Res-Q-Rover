import telepot
import ip_location
import json

with open('info.json') as file:
    info = json.load(file)

name = info["person_name"]
telegram_token = info["telegram_token"]
user_id = info["telegram_user_id"]

telegram_bot = telepot.Bot(token=telegram_token)

def send_image(user_id=user_id):
    telegram_bot.sendMessage(chat_id=user_id, text="{} has been found!".format(name))
    telegram_bot.sendPhoto(chat_id=user_id, photo=open("found.jpg", "rb"))

def send_location(user_id=user_id):
    try:
        location_data = ip_location.retrieve_current_location()
        google_map_link = "https://www.google.com.au/maps/@{},{},15z".format(location_data[0], location_data[1])
        message = "{}'s found location:\nLatitude: {}\nLongtitude: {}\nRegion: {}\nState: {}\nCountry: {}\nOpen map here: {}".format(name, location_data[0], location_data[1], location_data[2], location_data[3], location_data[4], google_map_link)
        telegram_bot.sendMessage(chat_id=user_id, text=message)
    except Exception:
        message = "{} Due to several problems I am unable to retrieve my current location!"
        telegram_bot.sendMessage(chat_id=user_id, text=message)
