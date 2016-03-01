from telegram import Updater

updater = Updater(token="INSERT_YOUR_TOKEN_HERE")

dispatcher = updater.dispatcher

def call(bot, chat_id, cmd_text):
  # Use TWILIO's API to call based on the cmd_text
  # Send a confirmation message to the issuer of the command
  msg = "My call method has not been implemented yet. Sorry!"
  bot.sendMessage(chat_id=chat_id, text=msg)

def text(bot, chat_id, cmd_text):
  # Use TWILIO's API to text based on the cmd_text
  # Send a confirmation message to the issuer of the command
  msg = "My text method has not been implemented yet. Sorry!"
  bot.sendMessage(chat_id=chat_id, text=msg)

def main(bot, update):
  message_text = update.message_text
  chat_id = update.message.chat_id
  
  words = message_text.split()
  cmd = words[0]
  cmd_text = ' '.join(words[1:]) if len(words) > 1 else ''

  if cmd == '!call':
    call(bot, chat_id, cmd_text)
  elif cmd == '!text':
    text(bot, chat_id, cmd_text)

dispatcher.addTelegramMessageHandler(main)

updater.start_polling()
