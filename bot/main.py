import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config.settings import TELEGRAM_TOKEN
from bot.handlers import start, help_command, info, menu

# Setting up logging
logging.basicConfig(filename='logs/bot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, menu))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
