"""
	Телеграм бот для обучения Теи
"""


#	Import
import asyncio
import random
import datetime
import time
import os
import json

#		AIOGRAM
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


class Main:
	def __init__(self):
		
		self.token = "TOKEN"
		self.bot = Bot(token=self.token)
		self.dp = Dispatcher(self.bot)

	async def loop(self):

		# OnStarted
		@self.dp.message_handler(commands=["start"])
		async def start_command(message: Message):

			await self.bot.send_message(message.from_user.id,
				"Научи меня говорить, мой Друг)")

		# COMMAND
		@self.dp.message_handler(content_types="text")
		async def text_types(message: Message):

			input_text = str(message.text).lower()
			input_text = input_text.split()


			if self.status == "get_command":
				# Если программа ожидает комманды

				if input_text[0] == "new_trigger":
					type_trigger = input_text[1]
					word_trigger = input_text[2]
					width_trigger = input_text[3]

		# RUN BOT
		await self.dp.start_polling(self.bot)


#	Run
if __name__ == '__main__':
	# RUN
	engine = Main()
	asyncio.run(engine.loop())
