import logging
import random

from handlers.common import get_info_about_user
import modules.filters as ft
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters.state import State, StatesGroup


class PhotoEdit(StatesGroup):
    waiting_for_mode = State()
    waiting_for_image = State()


async def start_edit(message: types.Message):
    print(get_info_about_user(message))
    await message.answer('Введите номер режима редактирования')
    await message.answer('1 - Мультик\n2 - Блюр\n3 - Стиль\n4 - Скетч(Ч/Б)\n5 - Скетч(Цветной)')
    await PhotoEdit.waiting_for_mode.set()


async def get_mode(message: types.Message, state: FSMContext):
    if not message.text.lower().isdigit():
        await message.answer("Неверно введено число, попробуйте ещё раз")
        return
    if int(message.text.lower()) < 1 or int(message.text.lower()) > 5: # Проверка на кол-во модов
        await message.answer("Выбран неверный режим редактирования, попробуйте ещё раз")
        return
    await state.update_data(mode=int(message.text.lower()))
    await PhotoEdit.next()
    await message.answer('Отправьте фото, которое нужно редактировать')


async def get_photo(message: types.Message, state: FSMContext):
    try:
        name = f'images/test{random.randint(1, 100)}.jpg'
        await message.photo[-1].download(name)
    except Exception as e:
        logging.exception(e)
        await message.answer('Произошла ошибка, отправьте фото ещё раз')
        return
    await state.update_data(image_name=name)
    user_data = await state.get_data()
    if user_data['mode'] == 1:
        image = ft.cartoon_edit(user_data['image_name'])
        photo = open(image, 'rb')
        await message.answer_photo(photo, 'Ваше фото')
        await state.finish()
    elif user_data['mode'] == 2:
        image = ft.blur_edit(user_data['image_name'])
        photo = open(image, 'rb')
        await message.answer_photo(photo, 'Ваше фото')
        await state.finish()
    elif user_data['mode'] == 3:
        image = ft.style_edit(user_data['image_name'])
        photo = open(image, 'rb')
        await message.answer_photo(photo, 'Ваше фото')
        await state.finish()
    elif user_data['mode'] == 4:
        image = ft.sketch1_edit(user_data['image_name'])
        photo = open(image, 'rb')
        await message.answer_photo(photo, 'Ваше фото')
        await state.finish()
    elif user_data['mode'] == 5:
        image = ft.sketch2_edit(user_data['image_name'])
        photo = open(image, 'rb')
        await message.answer_photo(photo, 'Ваше фото')
        await state.finish()


def register_handlers_editor(dp: Dispatcher):
    dp.register_message_handler(start_edit, commands='edit')
    dp.register_message_handler(get_mode, state=PhotoEdit.waiting_for_mode)
    dp.register_message_handler(get_photo, content_types=['photo'], state=PhotoEdit.waiting_for_image)