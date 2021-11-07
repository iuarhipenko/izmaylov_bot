from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

btnAppointment = types.KeyboardButton('📅Записаться')
btnCancelAppointment = types.KeyboardButton('😥Отменить запись')
btnFAQ = types.KeyboardButton('✍Оставить вопрос')
btnAdress = types.KeyboardButton('🏢Напомнить адрес')
btnsData = types.ReplyKeyboardMarkup()
btnsData.add(btnAppointment, btnCancelAppointment, btnFAQ, btnAdress)

findDateVizit = '17'
btnsDates = types.ReplyKeyboardMarkup()
btnsDates.add(findDateVizit, '12', '29', '1')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("✋Привет!\nЯ виртуальный ассистент доктора 👨‍⚕️ Измайлова!", reply_markup=btnsData)
       
@dp.message_handler()
async def echo(message: types.Message): 
    if message.text == '📅Записаться':
        await message.reply("Ок я проверю доступные для визита даты")
       # await message.reply("Убираем шаблоны сообщений", reply_markup=btnsData.ReplyKeyboardRemove())
    await message.reply("Итак, выберите доступную дату", reply_markup=btnsDates)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    if message.text == '📅Записаться':
        print(message.text == '📅Записаться')
        await message.reply("Убираем шаблоны сообщений", reply_markup=btnsData.ReplyKeyboardRemove())

# @dp.message_handler(commands=[btnAppointment])
# async def process_btnAppointment_command(message: types.Message):
#     await message.reply("Ок, я посмотрю свободную запись!")


# @dp.callback_query_handler(func=lambda c: c.data and c.data.startswith('btnAppointment'))
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
#     code = callback_query.data[-1]
#     print(code)
#     if code.isdigit():
#         code = int(code)
#     if code == 2:
#         await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
#     elif code == 5:
#         await bot.answer_callback_query(
#             callback_query.id,
#             text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
#     else:
#         await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


# @dp.message_handler()
# async def echo(message: types.Message): 
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Да"))
#     if message.text == 'да':
#         await message.reply("Ок я проверю доступные для визита даты")


#@dp.message_handler(commands=['keyboard'])
# async def open_keyboard(message: types.Message): 
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Да"))
#     btn1 = types.KeyboardButton('Массаж')
#     btn2 = types.KeyboardButton('Встерча')
#     btn3 = types.KeyboardButton('Другое')
#     btn4 = types.KeyboardButton('Запись')
#     markup.add(btn1, btn2, btn3, btn4)
#     await message.reply(message.chat.id, "Отличный выбор")
#     # if message.text == 'да':
#     #     await message.reply("Ок я проверю доступные для визита даты")

# @dp.message_handler(commands=['subscribe'])
# async def subscribe(message: types.Message):
#     if(not db.subscriber_exists(message.from_user.id)):
#         db.add_subscriber(message.from_user.id)
#     else: 
#         db.update_subscription(message.from_user.id, True)
    
#     await message.answer("Вы успешло получили запись!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
