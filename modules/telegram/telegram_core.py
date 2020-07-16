import telebot
from modules.tokens import TelegramToken
from core.command_extractor import command_home

# TODO How the hell to wrap this into class?
if __name__ == '__main__':
  telegram = telebot.TeleBot(TelegramToken)

  @telegram.message_handler(func=lambda message: True)
  def echo_all(message):
    # TODO Proper try-catch handling
    reply = command_home.process(message.text)
    print(reply)
    telegram.reply_to(message, reply)


  telegram.polling()
