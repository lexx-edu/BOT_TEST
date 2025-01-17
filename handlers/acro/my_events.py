
from aiogram.types import Message, InputFile, CallbackQuery, InputMediaPhoto

from handlers.search_navigation import parse_callback
from loader import dp, db
from keyboards.hjk import menu_main
from keyboards.inline import kb_no_events, create_kb_event_navigation
from config import system_pictures
# from keyboards import kb_main_menu, main_menu
from aiogram.utils.markdown import hbold, hlink, hitalic, hunderline, hstrikethrough

# @dp.callback_query_handler(menu_main.filter(button='my_events'))
# async def my_events(call: CallbackQuery):
#     call_data = parse_callback(call.data)
#     events_list = db.user_events(call.message.chat.id)
#     name = call.message.chat.full_name
#     current_chat_id = call.message.chat.id
#     current_message_id = call.message.message_id
#     if not events_list:
#         photo = system_pictures.get('no_events')
#         caption = f'Братишка, у тебя пока нет мероприятий'
#         await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
#                                                               caption=caption),
#                                         chat_id=current_chat_id,
#                                         message_id=current_message_id,
#                                         reply_markup=kb_no_events)
#     else:
#         photo = 'AgACAgIAAxkBAAIGNmP_N9wsrb6RYQkwvSZqsxB-n7qnAAIryTEbnhj4S2P5teSqRJ8DAQADAgADcwADLgQ'
#         caption = f'Братишка, у тебя пока нет мероприятий'
#         await dp.bot.edit_message_media(media=InputMediaPhoto(media=photo,
#                                                               caption=caption),
#                                         chat_id=current_chat_id,
#                                         message_id=current_message_id,
#                                         reply_markup=create_kb_event_navigation(call_data, ))