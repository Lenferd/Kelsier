import telebot
from modules.tokens import TelegramToken
from core.command_home.headquarter import Headquarter

# TODO How the hell to wrap this into class?
if __name__ == '__main__':
  telegram = telebot.TeleBot(TelegramToken)

  @telegram.message_handler(func=lambda message: True)
  def echo_all(message):
    # TODO Proper try-catch handling
    reply = Headquarter.process(message.text)
    # TODO reply is bool. Need to work with callbacks
    print(reply)
    telegram.reply_to(message, reply)


  telegram.polling()
