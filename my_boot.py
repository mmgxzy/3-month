from aiogram import Bot, Dispatcher, executor, types
import random
from config import TOKEN
bot = Bot(TOKEN)
dp = Dispatcher(bot)

num  = [1,2,3]
random_num = random.choice(num)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('привет, я тг бот где вы можете поиграть!')
    await message.answer("выберите одно число от 1 до 3")

@dp.message_handler(text='1')
async def cmd_one(message: types.Message):
    if random_num == 1:
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

@dp.message_handler(text='2')
async def cmd_two(message: types.Message):
    if random_num == 2:
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

@dp.message_handler(text='3')
async def cmd_three(message: types.Message):
    if random_num == 3:
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

executor.start_polling(dp, skip_updates = True)