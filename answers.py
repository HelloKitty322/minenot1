from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

import keyboards
from collection import RACES, CLASSES, all_professions, pics_list

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=keyboards.main_menu_keyboard())


@router.message(F.text.lower() == 'что умеет этот бот?')
async def cmd_q_a(message: Message):
    await message.answer('Этот бот выдает ссылку на интересующий вас раздел из базы знаний BSFG')


@router.message(F.text.lower() == 'посетить сайт базы знаний bsfg')
async def cmd_link_db(message: Message):
    await message.answer('↓↓↓Тык по ссылке↓↓↓', reply_markup=keyboards.db_link_keyboard())


@router.message(F.text.lower() == 'посетить сайт проекта bsfg')
async def cmd_link_site(message: Message):
    await message.answer('↓↓↓Тык по ссылке↓↓↓', reply_markup=keyboards.site_link_keyboard())


@router.message(F.text.lower() == 'профессии по расам')
async def cmd_begin_professions(message: Message):
    await message.answer('Выберете интересующую расу', reply_markup=keyboards.races_keyboard())


@router.message(F.text.lower() == 'начнем!')
async def cmd_begin(message: Message):
    await message.answer('Выберете интересующий вас раздел', reply_markup=keyboards.search_menu_keyboard())


@router.message(lambda F: F.text and F.text.lower() in RACES)
async def cmd_professions(message: Message):
    await message.answer('Выберете профессию', reply_markup=keyboards.jobs_by_race_keyboard(message.text))


@router.message(lambda F: F.text and F.text.lower() in all_professions)
async def link(message: Message):
    await message.answer_photo(photo=pics_list[message.text], reply_markup=keyboards.job_link_by_name_keyboard(message.text))


@router.message(F.text.lower() == 'профессии по классам')
async def cmd_begin_classes(message: Message):
    await message.answer('Выберете класс', reply_markup=keyboards.classes_keyboard())


@router.message(lambda F: F.text and F.text.lower() in CLASSES.keys())
async def cmd_classes(message: Message):
    await message.answer('Выберете профессию', reply_markup=keyboards.jobs_by_class_keyboard(message.text.lower()))


@router.message(lambda F: F.text and F.text.split(' (')[0].lower() in all_professions)
async def link_class(message: Message):
    await message.answer_photo(photo=pics_list[message.text.split(' (')[0]],
                               reply_markup=keyboards.job_link_by_name_and_race_keyboard(message.text))
