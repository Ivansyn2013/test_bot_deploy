from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram import types
from aiogram import executor as ex
from aiogram.types import InputFile, InputMedia
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mysql_connet_connector import db_mysql_request
from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.utils.callback_data import CallbackData
from dotenv import load_dotenv
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook

load_dotenv()

import random

html_mes = '<b>bold</b>, <strong>bold</strong> \
<i>italic</i>, <em>italic</em> \
<u>underline</u>, <ins>underline</ins> \
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del> \
<span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler> \
<b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic ' \
           'bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> ' \
           'bold</b> \
<a href="http://www.example.com/">inline URL</a> \
<a href="tg://user?id=123456789">inline mention of a user</a> \
<code>inline fixed-width code</code> \
<pre>pre-formatted fixed-width code block</pre>' \
           '<pre><code class="language-python">pre-formatted fixed-width code block written in the \
        Python programming language</code></pre>'

test_mes = "'''\nLorem ipsum dolor sit amet, " \
           "consectetur adipisicing elit\. Aperiam dolor  \
           libero amet tempora, ducimus quo incidunt? Dicta magni  sed dolore tenetur  \
           quos amet  nihil, hic officiis ipsa, pariatur deserunt ut\.\n'''"

my_cb = CallbackData('id', 'action')

bot = Bot(token=os.getenv('BOTTOKEN'))
print(os.getenv('BOTTOKEN'))
dp = Dispatcher(bot)

WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')


dp.middleware.setup(LoggingMiddleware())

# кнопки
inline_k = InlineKeyboardMarkup(resize_keyboard=True)
inline_but1 = InlineKeyboardButton(text='Привет', callback_data='www')
inline_but2 = InlineKeyboardButton(text='dsd', callback_data='www')
inline_but3 = InlineKeyboardButton(text='sdsdds', callback_data='www')
buttons = []

for inx in range(10):
    buttons.append(InlineKeyboardButton(text=f'{inx}', callback_data='www'))


def get_inline_kb():
    some_kb = InlineKeyboardMarkup()
    for i in range(7):
        but_list = []
        for k in range(2):
            b = InlineKeyboardButton(text=f'{random.randint(0, 100)}',
                                     callback_data='www')
            but_list.append(b)
        some_kb.row(*but_list)
    some_kb.row(InlineKeyboardButton(text='<', callback_data='<:-1'),
                InlineKeyboardButton(text='>', callback_data=">:1"))
    return some_kb


kb_list = [get_inline_kb() for x in range(5)]

# inline_k.add(inline_but1, inline_but2, inline_but3)
inline_k.add(*buttons)


@dp.message_handler(commands=['start', 'help'])
async def start_test(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hellow')
    await bot.send_message(message.from_user.id, html_mes, parse_mode='html')
    # await bot.send_photo(message.from_user.id, types.InputFile(
    #   'Atom-Cyber-artist-Мрачная-Эротика-Мрачные-картинки-7407536.jpeg'))
    await bot.send_message(message.from_user.id, test_mes, parse_mode='MarkdownV2')


@dp.message_handler(commands=['search'])
async def start_search(message: types.Message):
    # all_products = db_mysql_request()
    message.text
    await message.delete()


@dp.message_handler(commands=['inline'])
async def inline_kb(message: types.Message):
    await message.answer('Lincks', reply_markup=inline_k)
    print('ANY_MESS::')
    print(message.get_args())


@dp.message_handler(commands=['in'])
async def inline_kb(message: types.Message):
    await message.answer('Lincks', reply_markup=kb_list[0])
    print('ANY_MESS::')
    print(message.get_args())


@dp.callback_query_handler(text='>:1')
async def callback_next(query: types.CallbackQuery):
    await query.answer()
    index = int(query.data.split(':')[1])
    await query.message.edit_text('Новая кб', reply_markup=kb_list[1])


@dp.callback_query_handler(text='www')
async def some_callback(callback: types.CallbackQuery):
    print('text', end='::')
    print(callback.message.text)
    print('val', end='::')
    print(callback.values)
    print('cap', end='::')
    print(callback.message.caption)
    print('data', end='::')
    print(callback.data)
    print('set', end='::')
    print(callback.message.from_user.id)

    # print(callback.set_current())
    await callback.answer('push but')


@dp.message_handler()
async def any_message(message: types.Message):
    print('ANY_MESS::')
    print(message.get_args())


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


def prim():
    print('work!')


# ex.start_polling(dp, skip_updates=True)
if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path='/',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
