import requests
from datetime import datetime


def send_msg(**kwargs):
    token = "8027212830:AAHWGchHyHEhEzNrfA7qn0hlwHW0ZSqk9n4"  # bot token

    user_id = "1269687077"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {kwargs}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())



