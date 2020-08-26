from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from core.execution_unit.unit_status import UnitStatus
from modules.tokens import TelegramToken
from core.command_home.headquarter import Headquarter
import logging

logging.basicConfig(
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.DEBUG)
logger = logging.getLogger(__name__)

exec_unit = None
reply = False


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
  """Send a message when the command /start is issued."""
  update.message.reply_text('Hi!')


def help_command(update, context):
  """Send a message when the command /help is issued."""
  update.message.reply_text('Help!')


def echo(update, context):
  logger.info(echo)
  global exec_unit, reply
  # TODO Proper try-catch handling
  text = update.message.text
  logger.info(text)
  if text.find("end suffering") != -1:
    _end_suffering(update)
  if exec_unit is None:
    _create_exec_unit(text, update)
    return
  if reply:
    _action_from_user_required(text, update)
  else:
    _action_from_bot_required(update)


def _end_suffering(update):
  logger.info("_end_suffering")
  update.message.reply_text("Goodbye, my friend")
  exit()

def _action_from_user_required(text, update):
  logger.info("_action_from_user_required")
  global exec_unit, reply
  exec_unit.execute(text)
  reply = False
  _action_from_bot_required(update)


# TODO Please hide this shit under class
def _action_from_bot_required(update):
  logger.info("_action_from_bot_required")
  global exec_unit, reply
  if exec_unit.getStatus() == UnitStatus.HAVE_QUESTION:
    question = exec_unit.getQuestion()
    update.message.reply_text(question)
  else:
    update.message.reply_text("I don't know what do you want :(")
  reply = True


def _create_exec_unit(creation_text, update):
  logger.info("_create_exec_unit")
  global exec_unit, reply
  exec_unit = Headquarter.process(creation_text)
  update.message.reply_text("Exec unit created")
  _action_from_bot_required(update)


def main():
  """Start the bot."""
  # Create the Updater and pass it your bot's token.
  # Make sure to set use_context=True to use the new context based callbacks
  # Post version 12 this will no longer be necessary
  updater = Updater(TelegramToken, use_context=True)

  # Get the dispatcher to register handlers
  dp = updater.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", help_command))

  # on noncommand i.e message - echo the message on Telegram
  dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

  # Start the Bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C or the process receives SIGINT,
  # SIGTERM or SIGABRT. This should be used most of the time, since
  # start_polling() is non-blocking and will stop the bot gracefully.
  updater.idle()


if __name__ == '__main__':
  main()
