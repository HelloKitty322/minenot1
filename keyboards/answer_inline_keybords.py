from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import csv


def classes(needed_class) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    with open('professions.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        needed_professions = list(filter(lambda x: x['Класс'] == needed_class, reader))
        for i in needed_professions:
            builder.button(text=f"{i['Название профессии']} ({i['Раса']})")
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)
