from telegram import ReplyKeyboardMarkup

def main_menu_keyboard():
    keyboard = [['Information', 'Help'], ['Register', 'Menu']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
