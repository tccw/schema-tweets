import os
import dotenv
import logging
from datetime import datetime

dotenv.load_dotenv(dotenv.find_dotenv())


def get_auth():
    return (os.getenv('TWTR_APIKEY'),
            os.getenv('TWTR_SECRET'),
            os.getenv('TWTR_ACCESS_TOKEN'),
            os.getenv('TWTR_ACCESS_TOKEN_SECRET'))
