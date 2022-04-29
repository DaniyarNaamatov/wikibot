from aiogram import executor
from config import dp
import logging
from wiki import wikiparser


wikiparser.register_handler_inline(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
