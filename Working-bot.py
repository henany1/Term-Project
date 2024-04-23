from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import bot_token
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('How are you? This is to test if the bot is working')

def main():
    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
