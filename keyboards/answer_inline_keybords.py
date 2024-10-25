from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from minenot1.collection import CLASSES, file_list


def classes(needed_class) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    needed_professions = list(filter(lambda x: x['Класс'] == CLASSES[needed_class.lower()], file_list))
    for i in needed_professions:
        builder.button(text=f"{i['Название профессии']} ({i['Раса']})")
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)
