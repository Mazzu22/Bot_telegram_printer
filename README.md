# Bot_telegram_printer
## Overview
This Telegram bot allows users to send images or documents from your Telegram account as email attachments (the recommended use is to send files to a printer to send them to print).


## Getting Started
To use the Telegram Email Bot, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mazzu22/Bot_telegram_printer.git
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
3.**Configure config.py file with the following variables:**
  - bot_token: Telegram Bot Token
  - pass_iniziale: Initial Password for bot access
  - to_email: Email address to send attachments
  - smtp_server: SMTP server address
  - smtp_port: SMTP server port
  - smtp_username: SMTP server username
  - smtp_password: SMTP server password

4.**Run the bot:**
  ```bash
  python main.py
   ```

## Commands

To use the Telegram Email Bot, follow these steps:

### /start
  The /start command initiates the bot and prompts the user to enter a password for authentication.
 ### /stop
   The /stop command terminates the bot.
  


