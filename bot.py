from telegram import Updater
from twilio.rest import TwilioRestClient

TELEGRAM_TOKEN = "INSERT_YOUR_TOKEN_HERE"
TWILIO_ACCOUNT_SID = "INSERT_ACCOUNT_SID_HERE"
TWILIO_AUTH_TOKEN = "INSERT_AUTH_TOKEN_HERE"

# initialize telegram updater and dispatcher
updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher

# initialize twilio client
client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def call(bot, chat_id, cmd_text):
  # set source_number to be a number associated with the account
  source_number = "+18668675309"

  # cmd_text should be in format [Phone Number] [Message]
  cmd_words = cmd_text.split()
  phone_number = cmd_words[0]
  message_text = cmd_words[1:] if len(cmd_words) > 1 else "Yes"

  # Use TWILIO's API to call based on the cmd_text
  call = client.calls.create(
          url="http://demo.twilio.com/docs/voice.xml",
          to=phone_number,
          from=source_number)

  # Send a confirmation message to the issuer of the command
  msg = "Sent a call to the phone number with the default message."
  bot.sendMessage(chat_id=chat_id, text=msg)

def text(bot, chat_id, cmd_text):
  # set source_number to be a number associated with the account
  source_number = "+18668675309"

  # cmd_text should be in format [Phone Number] [Message]
  cmd_words = cmd_text.split()
  phone_number = cmd_words[0]
  message_text = cmd_words[1:] if len(cmd_words) > 1 else "Yes"

  # Use TWILIO's API to text based on the cmd_text
  call = client.calls.create(
          to=phone_number,
          from=source_number,
          body=message_text)

  # Send a confirmation message to the issuer of the command
  msg = "Sent a text to the phone number with your message."
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
