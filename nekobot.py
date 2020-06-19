import logging
import os
from aiogram import Bot, Dispatcher, executor, types
import nekos
from helpstr import HELPSTR

API_TOKEN = os.environ.get('TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_start(message: types.Message):

    "This handler will be called when user sends `/start` command"

    await message.reply("Hi!" + " " + message.from_user.first_name + " " +
                        "my name is Nekobot. I'm built on python3 & powerd by Nekos-life "
                        "I can supply you loads of anime wallpapers and hentai images.\n"
                        + "Click: /help to get started with the list of possible commands! "
                        "\n\nMade with ❤️ by [starry](tg://user?id=894380120) on aiogram.",
                        parse_mode='markdown')


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):

    "This handler will be called when user sends `/help` command"

    await message.reply(HELPSTR.format(message.from_user.first_name),
    parse_mode='html')


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
    await message.reply_photo(nekos.img('lesbian'))

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
