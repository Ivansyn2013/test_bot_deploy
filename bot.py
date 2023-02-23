from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
import uuid
import typing
from aiogram import types
from aiogram import executor as ex
from aiogram.types import InputFile, InputMedia
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.utils.callback_data import CallbackData
from dotenv import load_dotenv
import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook
from aiogram.utils.callback_data import CallbackData
from test import TEST_DICT


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
cd_data = CallbackData('button', 'id', 'bd_id', 'action', 'kb_number')
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

@dp.message_handler(commands=['spinner'])
async def test_spinner(message: types.Message):
    global kb_fruts
    kb_fruts = await get_product_list_kb(TEST_DICT)
    print('Len of kb_fruts ' + str(len(kb_fruts)))
    await message.answer('fdfd', reply_markup=kb_fruts[0])

##########################
@dp.callback_query_handler(cd_data.filter(action='next'))
async def product_list_callback_next(query: types.CallbackQuery,
                                     callback_data: typing.Dict[str, str]):
    print(callback_data['kb_number'])

    kb_number = int(callback_data['kb_number'])
    if kb_number >= len(kb_fruts) - 1:
        await  query.answer()
    else:
        await query.answer()
        await query.message.edit_text('Список продуктов',
                                      reply_markup=kb_fruts[kb_number + 1])

@dp.callback_query_handler(cd_data.filter(action='back'))
async def product_list_callback_back(query: types.CallbackQuery,
                                     callback_data: typing.Dict[str, str]):
    print(callback_data['kb_number'])

    kb_number = int(callback_data['kb_number'])
    if kb_number == 0:
        await  query.answer()
    else:
        await query.answer()
        await query.message.edit_text('Список продуктов',
                                      reply_markup=kb_fruts[kb_number - 1])
###################################


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


#@dp.callback_query_handler(text='>:1')
async def callback_next(query: types.CallbackQuery):
    await query.answer()
    index = int(query.data.split(':')[1])
    await query.message.edit_text('Новая кб', reply_markup=kb_list[1])


#@dp.callback_query_handler(text='www')
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


async def get_product_list_kb(all_product_dict: dict) -> types.InlineKeyboardButton:
    '''

    :param all_product_dict:dict with product name: product id from db
    :return:inline_kb
    '''
    cd_data = CallbackData('button', 'id', 'bd_id', 'action', 'kb_number')

    pd = all_product_dict
    kb_list = []
    but_list = []
    inline_but_kb = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    for name, id in sorted(pd.items()):
        b = InlineKeyboardButton(text=f'{name}',
                                 callback_data=cd_data.new(
                                     id=str(uuid.uuid4()),
                                     action='search_in',
                                     bd_id=id,
                                     kb_number=0,
                                 ),
                                 )
        but_list.append(b)

    if len(but_list) > 15:

        for index in range(0, len(but_list), 14):
            inline_but_kb.add(*but_list[index:index+14])

            inline_but_kb.row(InlineKeyboardButton(text='Назад',
                                                   callback_data=cd_data.new(
                                                       id=str(uuid.uuid4()),
                                                       action='back',
                                                       bd_id=id,
                                                       kb_number=index // 14,
                                                   )
                                                   ),
                              InlineKeyboardButton(text='Вперед',
                                                   callback_data=cd_data.new(
                                                       id=str(uuid.uuid4()),
                                                       action='next',
                                                       bd_id=id,
                                                       kb_number=index // 14,
                                                   )
                                                   ))

            kb_list.append(inline_but_kb)

            inline_but_kb = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
        else:
            inline_but_kb.add(*but_list[(len(but_list)//14)*14:])
            inline_but_kb.row(InlineKeyboardButton(text='Назад',
                                                   callback_data=cd_data.new(
                                                       id=str(uuid.uuid4()),
                                                       action='back',
                                                       bd_id=id,
                                                       kb_number=(len(but_list) // 14 +1),
                                                   )
                                                   ),
                              InlineKeyboardButton(text='Вперед',
                                                   callback_data=cd_data.new(
                                                       id=str(uuid.uuid4()),
                                                       action='next',
                                                       bd_id=id,
                                                       kb_number=(len(but_list) // 14 +1),
                                                   )
                                                   ))

            kb_list.append(inline_but_kb)


    else:
        inline_but_kb.add(*but_list)
        kb_list.append(inline_but_kb)
    # print(len(kb_list))
    return kb_list


if __name__ == '__main__':
    ex.start_polling(dp, skip_updates=True)
    # start_webhook(
    #     dispatcher=dp,
    #     webhook_path='/',
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT,
    # )
