import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

ADMIN_ID = int(os.environ.get("ADMIN_ID"))  # Telegram ID владельца
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Токен бота

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне сообщение, и я анонимно передам его администратору.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await context.bot.send_message(chat_id=ADMIN_ID, text=f"Анонимное сообщение:\n\n{user_message}")
    await update.message.reply_text("Твоё сообщение отправлено анонимно!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
