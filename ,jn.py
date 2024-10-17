Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... from aiogram import *
... 
... API_TOKEN = '7799158291:AAGqCpCuykEivT6oyUD3GDOlbCV3cs6yh9U'
... 
... bot = Bot(token=API_TOKEN)
... storage = MemoryStorage()
... dp = Dispatcher(bot, storage=storage)
... 
... class Form(StatesGroup):
...     waiting_for_choice = State()
...     waiting_for_upgrade = State()
... 
... @dp.message_handler(commands=['start'])
... async def start_command(message: types.Message):
...     await message.answer("🧛🏻‍♂️ Привет!\n— — — — — — —\nХочешь принять участие в нашем ивенте?\n\n        Да! 🎃")
...     await choose_coffin(message)
... 
... async def choose_coffin(message: types.Message):
...     await message.answer("🧛🏻‍♂️ Дракула\n— — — — — — —\n🎁 Возьми, оно поможет собрать больше конфет\n— — — — — — —\nвыбери один из трех гробов:\n\n⚰️       ⚰️       ⚰️")
...     await Form.waiting_for_choice.set()
... 
... @dp.message_handler(state=Form.waiting_for_choice, content_types=types.ContentTypes.TEXT)
... async def process_coffin_choice(message: types.Message, state: FSMContext):
...     pet = random.choice(["👻 Призрак", "🕷️ Паук", "🦇 Мышь"])
...     await message.answer(f"🎁 Ого! Тебе выпал:\n- {pet}\nтеперь прокачаем его, куда потратишь кровь?")
...     await state.update_data(pet=pet)
...     await Form.waiting_for_upgrade.set()
... 
... @dp.message_handler(state=Form.waiting_for_upgrade, content_types=types.ContentTypes.TEXT)
... async def upgrade_pet(message: types.Message, state: FSMContext):
    data = await state.get_data()
    pet = data.get('pet')
    await message.answer(f"{pet}\n— — — — — — —\n🎃 мешок: 1\n❤️ хп: 100 \n🗡️сила: 5\n🎲 шанс: 15%\n🥀 магия: 5\n— — — — — — —\n🩸 кровь: 3\n\n 🔝 прокачать \n   🎃 мешок")
    await Form.waiting_for_upgrade.set()

@dp.message_handler(lambda message: message.text in ["❤️", "🗡️", "🎲", "🥀"], state=Form.waiting_for_upgrade)
async def upgrade_choice(message: types.Message, state: FSMContext):
    if message.text == "❤️":
        await message.answer("❤️ хп увеличилось на 10 пунктов")
    elif message.text == "🗡️":
        await message.answer("🗡️ сила увеличилась на 1 пункт")
    elif message.text == "🎲":
        await message.answer("🎲 шанс увеличился на 5%")
    elif message.text == "🥀":
        await message.answer("🥀 магия увеличилась на 1 пункт")
    await choose_bag(message)

async def choose_bag(message: types.Message):
    await message.answer("🎃 Мешок\n— — — — — —\nУровень: 1\n0 🍬 / 6 🍬\n— — — — — —\nещё немного!\n\n 👈🏻 назад")

if __name__ == '__main__':
