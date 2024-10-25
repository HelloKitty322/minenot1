from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from minenot1.collection import RACES, CLASSES, all_professions
from keyboards.answer_inline_keybords import classes
from keyboards.for_begin_keyboard import begin_buttons_professions, begin_buttons, begin_buttons_classes
from keyboards.for_classes_keyboard import profession_link, off_site_link, off_db_link, classes_link, pic
from keyboards.for_professions_keyboard import professions
from keyboards.for_start_keyboard import start_buttons

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=start_buttons())


@router.message(F.text.lower() == 'что умеет этот бот?')
async def cmd_q_a(message: Message):
    await message.answer('Этот бот выдает ссылку на интересующий вас раздел из базы знаний BSFG')


@router.message(F.text.lower() == 'посетить сайт базы знаний bsfg')
async def cmd_link_db(message: Message):
    await message.answer('↓↓↓Тык по ссылке↓↓↓', reply_markup=off_db_link())


@router.message(F.text.lower() == 'посетить сайт проекта bsfg')
async def cmd_link_site(message: Message):
    await message.answer('↓↓↓Тык по ссылке↓↓↓', reply_markup=off_site_link())


@router.message(F.text.lower() == 'профессии по расам')
async def cmd_begin_professions(message: Message):
    await message.answer('Выберете интересующую расу', reply_markup=begin_buttons_professions())


@router.message(F.text.lower() == 'начнем!')
async def cmd_begin(message: Message):
    await message.answer('Выберете интересующий вас раздел', reply_markup=begin_buttons())


@router.message(lambda F: F.text and F.text.lower() in RACES)
async def cmd_professions(message: Message):
    await message.answer('Выберете профессию', reply_markup=professions(message.text))


@router.message(lambda F: F.text and F.text.lower() in all_professions)
async def link(message: Message):
    await message.answer_photo(photo=pic(message.text), reply_markup=profession_link(message.text))


@router.message(F.text.lower() == 'профессии по классам')
async def cmd_begin_classes(message: Message):
    await message.answer('Выберете класс', reply_markup=begin_buttons_classes())


@router.message(lambda F: F.text and F.text.lower() in CLASSES.keys())
async def cmd_classes(message: Message):
    await message.answer('Выберете профессию', reply_markup=classes(message.text.lower()))


@router.message(lambda F: F.text and F.text.split(' (')[0].lower() in all_professions)
async def link_class(message: Message):
    await message.answer_photo(photo=pic(message.text.split(' (')[0]), reply_markup=classes_link(message.text))
