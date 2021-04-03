#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Ph0nest v1.0
# Author: vsecoder
import os
def MAIN():
	try:
		import random
		import sys
		from colorama import Fore, Back, Style
		from aiogram import Bot, types
		from aiogram.dispatcher import Dispatcher
		from aiogram.utils import executor
		from aiogram.types import ReplyKeyboardRemove, \
		    ReplyKeyboardMarkup, KeyboardButton, \
		    InlineKeyboardMarkup, InlineKeyboardButton
		def Main():
			r = Fore.RED
			g = Fore.GREEN
			y = Fore.YELLOW
			s = Style.RESET_ALL

			
			def logo():
				logo = r+"Ph0nest  "+s+"by vsecoder"+r+" ░░░\n"+y + \
					" [ 💻 ]\n [ Dev: Vsevolod ]"+s
				print(logo)
			
			def main():
				logo()
				try:
					token = input('Токен бота телеграмм: ')
					bot = Bot(token=token)
					dp = Dispatcher(bot)

					@dp.message_handler(commands=['start'])
					async def send_welcome(message: types.Message):
						global users
						keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
						button_phone = types.KeyboardButton(
							text="📲Предоставить", request_contact=True)
						keyboard.add(button_phone)

						await bot.send_message(message.chat.id, '🙋Здравствуйте, я бот, для продолжения вам придётся предоставить номер', reply_markup=keyboard)

					@dp.message_handler(content_types=["contact"])
					async def number(message: types.Message):
						print('Юзер: ' + message.from_user.first_name + \
						      ' Номер: ' + y + message.contact.phone_number+s)

					print('[ 💻 ] Bot запущен!')
					executor.start_polling(dp)
				except:
					print('[ 💻 ] Token не правильный!')
					main()
			main()
		Main()	
	except ModuleNotFoundError:
		os.system('cls' if os.name=='nt' else 'clear')
		print("Нажмите Enter чтобы установить недостающие библиотеки...")
		input()
		os.system("python -m pip install aiogram colorama")

		MAIN()

MAIN()
