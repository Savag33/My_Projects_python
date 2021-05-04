from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="1627120214:AAFikeGnLmoBWRQqoO3lar8JfIOM3_DZ5no")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    # chat_id = message.chat.id
    # text = 'Some text'
    # sent_message = await bot.send_message(chat_id=chat_id, text=text)
    # print(sent_message.to_python())

    # sent_message = await bot.send_photo(chat_id=chat_id,
    #                                    photo="https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png")

    # print(sent_message.photo[-1].file_unique_id)

    bot_user = await bot.get_me()
    print(bot_user.username)


executor.start_polling(dp)
