from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_buttons() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Начнем!')
    keyboard.button(text='Что умеет этот бот?')
    keyboard.button(text='Посетить сайт базы знаний BSFG')
    keyboard.button(text='Посетить сайт проекта BSFG')
    keyboard.adjust(4, 1)
    return keyboard.as_markup(resize_keyboard=True)
