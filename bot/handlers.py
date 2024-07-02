import logging
from telegram import Update
from telegram.ext import CallbackContext
from bot.db import db
from bot.menu import main_menu_keyboard

def log_request(update: Update):
    logging.info(f"User {update.message.from_user.username} sent a message: {update.message.text}")

def start(update: Update, context: CallbackContext) -> None:
    log_request(update)
    username = update.message.from_user.username
    if not db.users.find_one({"username": username}):
        db.users.insert_one({"username": username, "info": "New user"})
    update.message.reply_text('Welcome! How can I assist you?', reply_markup=main_menu_keyboard())

def help_command(update: Update, context: CallbackContext) -> None:
    log_request(update)
    update.message.reply_text('Available commands: /start, /help, /info, /menu')

def info(update: Update, context: CallbackContext) -> None:
    log_request(update)
    username = update.message.from_user.username
    user_info = db.users.find_one({"username": username})
    if user_info:
        update.message.reply_text(f'User information: {user_info["info"]}')
    else:
        update.message.reply_text('User information not found.')

def menu(update: Update, context: CallbackContext) -> None:
    log_request(update)
    update.message.reply_text('Choose an option from the menu:', reply_markup=main_menu_keyboard())
