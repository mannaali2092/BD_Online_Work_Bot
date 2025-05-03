from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = '7593398312:AAGtGXWEK8w15yeRud--2VsVyDTg9QMZFWs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- Start Button Layout ---
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("⭐ Admin Plan"),
    KeyboardButton("👤 My Profile")
).add(
    KeyboardButton("🔗 Referral Earn"),
    KeyboardButton("🎁 Join Giveaways")
)

# --- /start Command ---
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = "<b>BD Free income platform</b>\n\nJoin: https://t.me/BD_Onliine_Work"
    await message.answer(text, reply_markup=main_menu, parse_mode='HTML')

# --- Default Response ---
@dp.message_handler()
async def default_reply(message: types.Message):
    await message.reply("Please choose an option from the menu below.")

# --- Run Bot ---
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)