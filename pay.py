from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, Invoice
from dotenv import load_dotenv

import os


load_dotenv()
PAY_TOKEN = os.getenv("PAY_TOKEN")

async def gift(message: Message, bot: Bot):
    invoce = Invoice()
    invoce.total_amount = 1000000

    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Сладкие пуки от Егора",
        description="Донат на бота",
        payload="hi",
        provider_token=PAY_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label="Поддержи нас",
                amount=20000*100
            ),
            # LabeledPrice(
            #     label="Эта долька для Чижа",
            #     amount=500*100
            # ),
            # LabeledPrice(
            #     label="Эта долька для Бобра",
            #     amount=50*100
            # )
        ],
        max_tip_amount=40000000,
        suggested_tip_amounts=[1000,2000,3000,4000],
        start_parameter='1',
        provider_data=None,
        #photo_url="https://wh.reactor.cc/post/5457713",
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpNyUe4j_3FxU-RdmCvGUwvqEd7aB0Azk6UA&usqp=CAU",
        #photo_url="file://localhost/home/user/PycharmProjects
        # /test_bot_deploy/photo/1.jpeg",
        photo_size=100,
        photo_width=100,
        photo_height=100,
        need_name=False,
        need_email=False,
        need_phone_number=False,
        need_shipping_address=False,
        send_email_to_provider=False,
        send_phone_number_to_provider=False,
        is_flexible=True,
        disable_notification=True,
        protect_content=True,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None, #keybord


    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Спасибо за поддержку ' \
          f'{message.successful_payment.total_amount //100 } ' \
          f'{message.successful_payment.currency}'
    await message.answer(msg)
