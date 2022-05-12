import logging
from datetime import datetime
from aiogram import Dispatcher, types


def get_info_about_user(message):
    text = f'\n##### {datetime.now()} #####\n'
    text += f'ID: {message.from_user.id}, Text: {message.text}'
    try:
        text += f'\nUsername: {message.from_user.username},' \
                f' Name: {message.from_user.first_name},' \
                f' Surname: {message.from_user.last_name} '
    except Exception as e:
        logging.exception(e)
        text += 'Нет имени'
    return text


async def cmd_start(message: types.Message):
    print(get_info_about_user(message))
    await message.reply("Редактирую фотки, команды можно посмотреть туть /commands")


async def cmd_list_cmds(message: types.Message):
    print(get_info_about_user(message))
    await message.answer('/edit - Применить фильтр на выбор к фото')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cmd_list_cmds, commands='commands')
