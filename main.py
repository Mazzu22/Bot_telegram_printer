import telebot
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import bot_token, pass_iniziale, to_email, smtp_server, smtp_port, smtp_username, smtp_password

bot = telebot.TeleBot(bot_token)


# Handle /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.reply_to(message,
               "Hi. For security reasons, please enter your password: 🔒")
  bot.register_next_step_handler(message, handle_password)


# Handle /stop command
@bot.message_handler(commands=['stop'])
def handle_stop(message):
  bot.reply_to(message, "Bot ended")


# Handle the password auth
def handle_password(message):
    while message.text != pass_iniziale:
        bot.reply_to(message, "The password inserted is wrong. Retry 😡.")
        bot.register_next_step_handler(message, handle_password)
        return  # Return to prevent the function from continuing if password is incorrect

    bot.reply_to(
        message,
        "Correct password. Send me an image or document to forward as an attachment.")
    bot.register_next_step_handler(message, mannalo)



# Func to handle the forwarding of image and document
@bot.message_handler(content_types=['photo', 'document'])
def mannalo(message):
  # Handle of image forwarding 
  if message.content_type == 'photo':
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.reply_to(message, "I have received the image. Sending the email... ⌛")
    send_email(downloaded_file, 'image.jpg')
    bot.reply_to(message, "Send another photo or document")
   # Handle of document forwarding
  elif message.content_type == 'document':
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    bot.reply_to(message, "I have received the file. Sending the email... ⌛")
    send_email(downloaded_file, message.document.file_name)
    bot.reply_to(message, "Send another photo or document")
  
  else:
    bot.reply_to(message,"You must send an image or a file. Please try again. 😡")


# Func to send the mail
def send_email(file_data, file_name):
  msg = MIMEMultipart()
  msg['From'] = smtp_username
  msg['To'] = to_email
  msg['Subject'] = "Email from Telegram"

  # Add the file as attachment
  attachment = MIMEBase('application', 'octet-stream')
  attachment.set_payload(file_data)
  encoders.encode_base64(attachment)
  attachment.add_header('Content-Disposition',
                        'attachment',
                        filename=file_name)
  msg.attach(attachment)

  server = smtplib.SMTP(smtp_server, smtp_port)
  server.starttls()
  server.login(smtp_username, smtp_password)
  server.sendmail(smtp_username, to_email, msg.as_string())
  server.quit()


# Start the bot
bot.polling()
