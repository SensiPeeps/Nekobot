# MIT License
#
# Copyright (c) 2020 Stɑrry Shivɑm // This file is part of Nekobot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import logging
import os
from aiogram import Bot, Dispatcher, executor, types
import nekos
from helpstr import HELPSTR, STARTSTR

API_TOKEN = os.environ.get('TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
btns = types.InlineKeyboardButton("Commands available ❔", callback_data='send_help')
keyboard_markup.row(btns)

@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):

    "This handler will be called when user sends `/start` command"

    await message.reply(STARTSTR.format(
          name=" ".join([message.from_user.first_name, message.from_user.last_name])
          if message.from_user.last_name else message.from_user.first_name),
          parse_mode='markdown', reply_markup=keyboard_markup,
          disable_web_page_preview=True)


@dp.callback_query_handler(text='send_help')
async def help_callback(query: types.CallbackQuery):

    "This handler answer callback query data to send help string"

    # Scoped variable of keyboard_markup for help callback
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    btns = types.InlineKeyboardButton("Go back ↩️", callback_data='go_back')
    keyboard_markup.row(btns)

    await query.message.edit_text(HELPSTR.format(
    name=" ".join([query.from_user.first_name, query.from_user.last_name])
    if query.from_user.last_name else query.from_user.first_name),
    parse_mode='html', reply_markup=keyboard_markup)

@dp.callback_query_handler(text='go_back')
async def back_callback(query: types.CallbackQuery):

    "This handler answer callback query data to send back start msg"

    await query.message.edit_text(STARTSTR.format(
    name=" ".join([query.from_user.first_name, query.from_user.last_name])
    if query.from_user.last_name else query.from_user.first_name),
    parse_mode='markdown', reply_markup=keyboard_markup,
    disable_web_page_preview=True)


# Begin hentai functions ....

@dp.message_handler(commands=['pussy'])
async def pussy(message: types.Message):
    await message.reply_photo(nekos.img('pussy_jpg'))

@dp.message_handler(commands=['hentaigif'])
async def hentaig(message: types.Message):
    await message.reply_video(nekos.img('random_hentai_gif'))

@dp.message_handler(commands=['neko'])
async def neko(message: types.Message):
    await message.reply_document(nekos.img('neko'))

@dp.message_handler(commands=['feet'])
async def feet(message: types.Message):
    await message.reply_photo(nekos.img('feet'))

@dp.message_handler(commands=['yuri'])
async def yuri(message: types.Message):
    await message.reply_photo(nekos.img('yuri'))

@dp.message_handler(commands=['trap'])
async def trap(message: types.Message):
    await message.reply_photo(nekos.img('trap'))

@dp.message_handler(commands=['futanari'])
async def futanari(message: types.Message):
    await message.reply_photo(nekos.img('futanari'))

@dp.message_handler(commands=['hololewd'])
async def hololewd(message: types.Message):
    await message.reply_photo(nekos.img('hololewd'))

@dp.message_handler(commands=['lewdkemo'])
async def lewdkemo(message: types.Message):
    await message.reply_photo(nekos.img('lewdkemo'))

@dp.message_handler(commands=['sologif'])
async def solog(message: types.Message):
    await message.reply_video(nekos.img('solog'))

@dp.message_handler(commands=['feetgif'])
async def feetg(message: types.Message):
    await message.reply_video(nekos.img('feetg'))

@dp.message_handler(commands=['cumgif'])
async def cum(message: types.Message):
    await message.reply_video(nekos.img('cum'))

@dp.message_handler(commands=['erokemo'])
async def erokemo(message: types.Message):
    await message.reply_photo(nekos.img('erokemo'))

@dp.message_handler(commands=['lesbian'])
async def lesbian(message: types.Message):
    await message.reply_photo(nekos.img('les'))

@dp.message_handler(commands=['wall'])
async def wallpaper(message: types.Message):
    await message.reply_document(nekos.img('wallpaper'))

@dp.message_handler(commands=['lewdk'])
async def lewdk(message: types.Message):
    await message.reply_photo(nekos.img('lewdk'))

@dp.message_handler(commands=['ngif'])
async def ngif(message: types.Message):
    await message.reply_video(nekos.img('ngif'))

@dp.message_handler(commands=['tickle'])
async def tickle(message: types.Message):
    await message.reply_photo(nekos.img('tickle'))

@dp.message_handler(commands=['lewd'])
async def lewd(message: types.Message):
    await message.reply_photo(nekos.img('lewd'))

@dp.message_handler(commands=['feed'])
async def feed(message: types.Message):
    await message.reply_photo(nekos.img('feed'))

@dp.message_handler(commands=['eroyuri'])
async def eroyuri(message: types.Message):
    await message.reply_photo(nekos.img('eroyuri'))

@dp.message_handler(commands=['eron'])
async def eron(message: types.Message):
    await message.reply_photo(nekos.img('eron'))

@dp.message_handler(commands=['cum'])
async def cum(message: types.Message):
    await message.reply_photo(nekos.img('cum_jpg'))

@dp.message_handler(commands=['bjgif'])
async def bjgif(message: types.Message):
    await message.reply_video(nekos.img('bj'))

@dp.message_handler(commands=['bj'])
async def bj(message: types.Message):
    await message.reply_photo(nekos.img('blowjob'))

@dp.message_handler(commands=['nekonsfw'])
async def nekonsfw(message: types.Message):
    await message.reply_video(nekos.img('nsfw_neko_gif'))

@dp.message_handler(commands=['solo'])
async def solo(message: types.Message):
    await message.reply_photo(nekos.img('solo'))

@dp.message_handler(commands=['kemonomimi'])
async def kemonomimi(message: types.Message):
    await message.reply_photo(nekos.img('kemonomimi'))

@dp.message_handler(commands=['pokegif'])
async def pokeg(message: types.Message):
    await message.reply_video(nekos.img('poke'))

@dp.message_handler(commands=['analgif'])
async def analg(message: types.Message):
    await message.reply_video(nekos.img('anal'))

@dp.message_handler(commands=['hentai'])
async def hentai(message: types.Message):
    await message.reply_photo(nekos.img('hentai'))

@dp.message_handler(commands=['erofeet'])
async def erofeet(message: types.Message):
    await message.reply_photo(nekos.img('erofeet'))

@dp.message_handler(commands=['holo'])
async def holo(message: types.Message):
    await message.reply_photo(nekos.img('holo'))

@dp.message_handler(commands=['pussygif'])
async def pussyg(message: types.Message):
    await message.reply_video(nekos.img('pussy'))

@dp.message_handler(commands=['boobs'])
async def tits(message: types.Message):
    await message.reply_photo(nekos.img('tits'))

@dp.message_handler(commands=['holoero'])
async def holoero(message: types.Message):
    await message.reply_photo(nekos.img('holoero'))

@dp.message_handler(commands=['classic'])
async def classic(message: types.Message):
    await message.reply_video(nekos.img('classic'))

@dp.message_handler(commands=['kuni'])
async def kuni(message: types.Message):
    await message.reply_video(nekos.img('kuni'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
