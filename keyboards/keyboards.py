from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from minenot1.collection import CLASSES, RACES
from minenot1.collection import jobs_data


def jobs_by_class_keyboard(needed_class) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    needed_professions = list(filter(lambda x: x['Класс'] == CLASSES[needed_class.lower()], jobs_data))
    for i in needed_professions:
        builder.button(text=f"{i['Название профессии']} ({i['Раса']})")
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)


def get_jobs_by_race(race) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    needed_profession = list(filter(lambda x: x['Раса'] == race, jobs_data))
    for i in needed_profession:
        builder.button(text=i['Название профессии'])
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def races_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for i in RACES:
        keyboard.button(text=f'{i.title()}')
    keyboard.adjust(4, 1)
    return keyboard.as_markup(resize_keyboard=True)


def search_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Профессии по расам')
    keyboard.button(text='Профессии по классам')
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)


def classes_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for i in CLASSES.keys():
        keyboard.button(text=f'{i.title()}')
    keyboard.adjust(5)
    return keyboard.as_markup(resize_keyboard=True)


def job_link_by_name_keyboard(arg) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    needed_profession = list(filter(lambda x: x['Название профессии'] == arg, jobs_data))
    builder.row(InlineKeyboardButton(text=f'{needed_profession[0]["Название профессии"]}',
                                     url=f'{needed_profession[0]["Ссылка"]}'))
    return builder.as_markup(resize_keyboard=True)


def job_link_by_name_and_race_keyboard(arg) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    needed_class = arg.split(' (')[0]
    data = list(filter(lambda x: x['Название профессии'] == needed_class, jobs_data))
    builder.row(InlineKeyboardButton(text=f'{data[0]["Название профессии"]}',
                                     url=f'{data[0]["Ссылка"]}'))
    return builder.as_markup(resize_keyboard=True)


def site_link_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Сайт игры', url='https://bsfg.ru'))
    return builder.as_markup(resize_keyboard=True)


def db_link_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Сайт базы знаний', url='https://db.bsfg.ru'))
    return builder.as_markup(resize_keyboard=True)


def jobs_by_race_keyboard(race) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    needed_profession = list(filter(lambda x: x['Раса'] == race, jobs_data))
    for i in needed_profession:
        builder.button(text=i['Название профессии'])
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Начнем!')
    keyboard.button(text='Что умеет этот бот?')
    keyboard.button(text='Посетить сайт базы знаний BSFG')
    keyboard.button(text='Посетить сайт проекта BSFG')
    keyboard.adjust(4, 1)
    return keyboard.as_markup(resize_keyboard=True)
