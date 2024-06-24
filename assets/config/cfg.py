import configparser
from datetime import datetime
import sys
sys.dont_write_bytecode=True
read_config = configparser.ConfigParser()
read_config.read("settings.ini")

BOT_TOKEN = read_config['settings']['token'].strip().replace(" ", "")
PATH_DATABASE = 'assets/data/db.db'
a_chat_id = read_config["chats"]['a_chat_id']
a2_chat_id = read_config["chats"]['a2_chat_id']


#other
model_id = read_config["ids"]['model_id']

def get_admins():
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = read_admins['ids']['admin_id'].strip().replace(" ", "")

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "\r" in admins: admins.remove("\r")
    while "\n" in admins: admins.remove("\n")

    admins = list(map(int, admins))

    return admins

def get_models():
    read_support = configparser.ConfigParser()
    read_support.read("settings.ini")

    models = read_support['ids']['model_id'].strip().replace(" ", "")

    if "," in models:
        models = models.split(",")
    else:
        if len(models) >= 1:
            models = [models]
        else:
            models = []

    while "" in models: models.remove("")
    while " " in models: models.remove(" ")
    while "\r" in models: models.remove("\r")
    while "\n" in models: models.remove("\n")

    models = list(map(int, models))

    return models

def calculate_days_ago(date_str):
    try:
        post_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        delta = datetime.now() - post_date

        if delta.days > 0:
            return f"{delta.days} д. назад"
        elif delta.seconds < 60:
            return "менше хвилини тому"
        elif delta.seconds < 3600:
            minutes = delta.seconds // 60
            return f"{minutes} хв. назад"
        else:
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            if hours > 24:
                days = hours // 24
                return f"{days} д. назад"
            elif hours >= 1:
                return f"{hours} г. назад"
            else:
                return f"{minutes} хв. назад"

    except Exception as e:
        print(f"Error calculating time ago: {e}")
        return "невідомо"