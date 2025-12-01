import time 

def get_welcome_message():
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        return "Dobré ráno!"
    elif 12 <= current_hour < 18:
        return "Dobrý den!"
    elif 18 <= current_hour < 22:
        return "Dobrý večer!"
    else:
        return "Dobrou noc!"