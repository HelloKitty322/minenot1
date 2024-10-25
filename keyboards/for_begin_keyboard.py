from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from minenot1.collection import RACES, CLASSES


def begin_buttons_professions() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for i in RACES:
        keyboard.button(text=f'{i.title()}')
    keyboard.adjust(4, 1)
    return keyboard.as_markup(resize_keyboard=True)


def begin_buttons() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Профессии по расам')
    keyboard.button(text='Профессии по классам')
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)


def begin_buttons_classes() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for i in CLASSES.keys():
        keyboard.button(text=f'{i.title()}')
    keyboard.adjust(5)
    return keyboard.as_markup(resize_keyboard=True)
