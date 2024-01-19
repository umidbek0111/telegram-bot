from aiogram import Bot, types, F, Dispatcher
from stets import Form
from config import TOKKEN, admin
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
import logging
from aiogram.enums import ParseMode
import sys
import asyncio
from buttons import button1, phone, confirm


# logging.basicConfig(level=logging.INFO)

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(TOKKEN, parse_mode=ParseMode.HTML)
chanel_id = '-1002142798901'


@dp.message(CommandStart())
async def get_start(message: types.Message, state: FSMContext):
    await message.answer(f"Asslomu allaykum {message.from_user.first_name}", reply_markup=button1)
    await state.set_state(Form.kasb)

@dp.message(Form.kasb, F.text)
async def get_kasb(message: types.Message, state: FSMContext):
    kasb = message.text
    user_id = message.from_user.id
    await state.set_data(
        {'kasb':kasb,
         'user_id':user_id}
    )
    await message.answer(f"Ismingizni kiriting ... ")
    await state.set_state(Form.name)


@dp.message(Form.name, F.text)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.set_data(
        {'name': name}
        )
    await message.answer("Telefon no'mringizni kiriting ...", reply_markup=phone)
    await state.set_state(Form.phone)

@dp.message(Form.phone, F.contact)
async def get_contact(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.set_data(
        {'phone':phone}
    )
    await message.answer(f"Yashash joyingizni yozib yuboring ...")
    await state.set_state(Form.lacation)


@dp.message(Form.lacation, F.text)
async def get_lacation(message: types.Message, state: FSMContext):
    lacotion = message.text
    await state.set_state(
        {'joylashuv': lacotion}
    )
    data = await state.get_data()
    kasb = data.get('kasb')
    ism = data.get('name')
    nomr = data.get("phone")
    await message.answer(f"Ism: {ism}\nKasb: {kasb}\nNo'mringiz: {nomr}\nJoylashuv {lacotion}\n\nSizning ma'lumotlaringizni tasdiqlaysizmi ", reply_markup=confirm)
    await state.set_state(Form.admin)



@dp.message(Form.admin, F.text=="HA")
async def get_admin(message: types.Message, state: FSMContext):
    data = await state.get_data()
    kasb = data.get('kasb')
    ism = data.get('name')
    nomr = data.get("phone")
    lacotion = data.get('joylashuv')
    await bot.send_message(chanel_id,text=f"Ism: {ism}\nKasb: {kasb}\nNo'mringiz: {nomr}\nJoylashuv {lacotion}\n\nSizning ma'lumotlaringizni tasdiqlaysizmi ")



# @dp.message()
# async def get_kanal(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     user_id = data.get('user_id')
#     kasb = data.get('kasb')
#     ism = data.get('name')
#     nomr = data.get("phone")
#     lacotion = data.get('joylashuv')
#     if 'HA' == message.text:
#         await bot.send_message(chanel_id=chanel_id,text=f"Ism: {ism}\nKasb: {kasb}\nNo'mringiz: {nomr}\nJoylashuv {lacotion}\n\nSizning ma'lumotlaringizni tasdiqlaysizmi ")    
#     else:
#         await bot.send_message(chat_id=user_id, text="Arizangiz Qobul qilinmadi")
#     await state.clear()



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
