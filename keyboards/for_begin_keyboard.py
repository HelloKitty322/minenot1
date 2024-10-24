from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def begin_buttons_professions() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    races = ['Империя', 'Альянс', 'Доминион', 'Орда', 'Союз', 'Легион', 'Белатто']
    for i in races:
        keyboard.button(text=f'{i}')
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
    data = ['Чародеи', 'Тяжелые воины', 'Легкие воины', 'Маги', 'Мастера Войны', 'Рыцари', 'Убийцы', 'Стрелки',
            'Лекари', 'Менталисты']
    for i in data:
        keyboard.button(text=f'{i}')
    keyboard.adjust(5)
    return keyboard.as_markup(resize_keyboard=True)
