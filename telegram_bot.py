from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests
from dotenv import load_dotenv
import os
import glob

env_file = glob.glob("./*.env")
if env_file:
    load_dotenv(dotenv_path=env_file[0])
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if BOT_TOKEN:
        print(f"Loaded BOT_TOKEN: {BOT_TOKEN[:2]}...{BOT_TOKEN[-2:]}")
    else:
        print("BOT_TOKEN not loaded — check .env path or variable name.")
else:
    print("No .env file found in current directory for BOT TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = update.effective_chat.id

    print(f"Recieved user_text:{user_text}")
    await context.bot.send_message(chat_id=chat_id, text="Listening Patently: Received ["+user_text+"]")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running... (Polling mode)")
    app.run_polling()

if __name__ == "__main__":
    main()