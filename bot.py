from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7724200385:AAFpmFXegWZaRKPje-gmYi0FFIRV7XD7IM8"  # আপনার টোকেন

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        'Online Free income platform "BD Online Work"\n'
        'Join link :- https://t.me/BD_Onliine_Work'
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
