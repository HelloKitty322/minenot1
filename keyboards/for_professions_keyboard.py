from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from minenot1.collection import file_list


def professions(race) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    needed_profession = list(filter(lambda x: x['Раса'] == race, file_list))
    for i in needed_profession:
        builder.button(text=i['Название профессии'])
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)
