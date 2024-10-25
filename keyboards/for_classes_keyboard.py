from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from minenot1.collection import file_list, pics_list


def profession_link(arg) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    needed_profession = list(filter(lambda x: x['Название профессии'] == arg, file_list))
    builder.row(InlineKeyboardButton(text=f'{needed_profession[0]["Название профессии"]}',
                                     url=f'{needed_profession[0]["Ссылка"]}'))
    return builder.as_markup(resize_keyboard=True)


def classes_link(arg) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    needed_class = arg.split(' (')[0]
    data = list(filter(lambda x: x['Название профессии'] == needed_class, file_list))
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


def pic(name_pic) -> str:
    for i in pics_list:
        if i['Название профессии'] == name_pic:
            picture_url = i['Ссылка на картинку']
            return picture_url
