from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.files import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "7771128523:AAE6tlBg2GpJVrRc3hdhD157Kt8vCiAxVNg"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard = True)
in_kb = InlineKeyboardMarkup(resize_keyboard = True)
in_button1 = InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data='calories')
in_button2 = InlineKeyboardButton(text= 'Формулы расчёта', callback_data='formulas')
in_kb.row(in_button1)
in_kb.row(in_button2)
button1 = KeyboardButton( text= 'Рассчитать')
button2 = KeyboardButton( text= 'Информация')
button3 = KeyboardButton( text= 'Купить')
kb.row(button1)
kb.row(button2)
kb.row(button3)

in_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= 'Product1', callback_data="product_buying")],
    [InlineKeyboardButton(text= 'Product2', callback_data="product_buying")],
    [InlineKeyboardButton(text= 'Product3', callback_data="product_buying")],
    [InlineKeyboardButton(text= 'Product4', callback_data="product_buying")]],
    resize_keyboard = True)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Выберите опцию:', reply_markup=in_kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for number in range(1, 5):
        with open('Protein.png', 'rb') as img:
            await message.answer_photo(img, f'Название: Продукт {number} | Описание: описание {number} | Цена: {number * 100}')
    await message.answer("Выберите продукт для покупки:", reply_markup=in_kb2)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес + 6.25 х рост - 5 * возраст + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    bmr = (10 * data['weight']) + (6.25 * data['growth']) - (5 * data['age']) + 5
    await message.answer(f'Ваша норма по  количеству калорий в сутки: {bmr}')
    state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
