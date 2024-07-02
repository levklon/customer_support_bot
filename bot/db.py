from pymongo import MongoClient
from config.settings import MONGODB_URI

# Setting up logging
import logging
logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

client = MongoClient(MONGODB_URI)
db = client['customer_support']
