import re
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from config.default import settings

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id,
        text=settings.STATIC_HELP_MSG
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = update.message.text

    try:
        pattern = re.compile(settings.LINK_REGEX)
        matches = re.findall(pattern=pattern, string=message)
        if matches:
            for link in matches:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=link
                )
    except Exception as e:
        await context.bot.send_message(
            chat_id=chat_id,
            text=str(e)
        )

def main():
    # Init Bot
    app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

    # Handlers
    help_handler = CommandHandler("help", help)
    chat_handler = MessageHandler(filters.TEXT, chat)

    # Add Handlers to Bot
    app.add_handler(help_handler)
    app.add_handler(chat_handler)

    # Run Bot
    app.run_polling()

if __name__ == "__main__":
    main()