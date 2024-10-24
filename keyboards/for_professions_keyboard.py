from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import csv


def professions(race) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    with open('professions.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        needed_profession = list(filter(lambda x: x['Раса'] == race, reader))
        for i in needed_profession:
            builder.button(text=i['Название профессии'])
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)

