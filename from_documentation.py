import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, types

from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.dispatcher import Dispatcher

from aiogram.dispatcher.webhook import SendMessage

from aiogram.utils.executor import start_webhook

load_dotenv()

API_TOKEN = os.getenv('BOTTOKEN')


# webhook settings




# webserver settings

WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())



@dp.message_handler()

async def echo(message: types.Message):

    # Regular request

    # await bot.send_message(message.chat.id, message.text)


    # or reply INTO webhook

    return SendMessage(message.chat.id, message.text)



async def on_startup(dp):

    await bot.set_webhook(WEBHOOK_URL)

    # insert code here to run it after start



async def on_shutdown(dp):

    logging.warning('Shutting down..')


    # insert code here to run it before shutdown


    # Remove webhook (not acceptable in some cases)

    await bot.delete_webhook()


    # Close DB connection (if used)

    await dp.storage.close()

    await dp.storage.wait_closed()


    logging.warning('Bye!')



if __name__ == '__main__':

    start_webhook(

        dispatcher=dp,

        webhook_path=WEBHOOK_PATH,

        on_startup=on_startup,

        on_shutdown=on_shutdown,

        skip_updates=True,

        host=WEBAPP_HOST,

        port=WEBAPP_PORT,

    )
