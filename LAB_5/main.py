import telebot

token = '5062047028:AAHMl5UoYK3WTm-XZRPFjHp5xlp1imptGmk'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
 keyboard = telebot.types.ReplyKeyboardMarkup(True)
 keyboard.row('Отлично', 'Плохо')
 bot.send_message(message.chat.id, 'Привет! Как дела?',
reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
 if message.text.lower() == 'отлично':
   bot.send_message(message.chat.id, 'Это очень хорошо!')
 elif message.text.lower() == 'плохо':
   bot.send_message(message.chat.id, 'Не сдавайся! Все будет хорошо!')

bot.polling()
