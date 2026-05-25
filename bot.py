import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

8821005134:AAEjevowV6OR5gYO-xyk gnWaOOZc572Cosk = os.getenv("TELEGRAM_TOKEN")
AIzaSyBlw7n6gwApoqqnu-cAch7dBsdQg18ZM1o = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = model.generate_content(
        f"Ты дружелюбный помощник. Отвечай коротко и по-дружески на русском языке. Сообщение: {user_message}"
    )
    await update.message.reply_text(response.text)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
