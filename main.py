from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='YOUR_TOKEN_HERE')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="👋 button1", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="💋 button2", callback_data="randomvalue_of100")
button3 = InlineKeyboardButton(text="button3", callback_data="randomvalue_of1000")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Hello!", "💋 Youtube", "Instagram")


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im a bot built using python", reply_markup=keyboard1)


@dp.callback_query_handler(text=["randomvalue_of10", "randomvalue_of100", "randomvalue_of1000"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of10":
        await call.message.answer(randint(1, 10))
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 100))
    if call.data == "randomvalue_of100":
        await call.message.answer(randint(1, 1000))
    await call.answer()


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Hello!':
        await message.reply("Hi! How are you?")
    elif message.text == '💋 Youtube':
        await message.reply("https://www.youtube.com/")
    elif message.text == 'Instagram':
        await message.reply("https://www.instagram.com/")
    else:
        await message.reply(f"Your message is: {message.text}")


executor.start_polling(dp)
