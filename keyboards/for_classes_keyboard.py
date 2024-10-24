from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import csv


def profession_link(arg) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    with open('professions.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        needed_profession = list(filter(lambda x: x['Название профессии'] == arg, reader))
        builder.row(InlineKeyboardButton(text=f'{needed_profession[0]["Название профессии"]}',
                                         url=f'{needed_profession[0]["Ссылка"]}'))
    return builder.as_markup(resize_keyboard=True)


def classes_link(arg) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    needed_class = arg.split(' (')[0]
    with open('professions.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        data = list(filter(lambda x: x['Название профессии'] == needed_class, reader))
        builder.row(InlineKeyboardButton(text=f'{data[0]["Название профессии"]}',
                                         url=f'{data[0]["Ссылка"]}'))
        return builder.as_markup(resize_keyboard=True)


def off_site_link():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Сайт игры', url='https://bsfg.ru'))
    return builder.as_markup(resize_keyboard=True)


def off_db_link():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Сайт базы знаний', url='https://db.bsfg.ru'))
    return builder.as_markup(resize_keyboard=True)


def all_professions():
    with open('professions.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        professions = list(map(lambda x: x['Название профессии'].lower(), reader))
    return professions


def classes_list():
    data = ['Чародеи', 'Тяжелые воины', 'Легкие воины', 'Маги', 'Мастера Войны', 'Рыцари', 'Убийцы', 'Стрелки',
            'Лекари', 'Менталисты']
    return data
