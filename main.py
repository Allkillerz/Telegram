from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 Pulsa & Data", callback_data="pulsa")],
        [InlineKeyboardButton("👥 Paket Akrab V1", callback_data="akrab1")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🚀 Silakan pilih menu:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "pulsa":
        await query.edit_message_text("Kamu pilih Pulsa & Data.")
    elif query.data == "akrab1":
        await query.edit_message_text("Kamu pilih Paket Akrab V1.")

# Token dari environment
TOKEN = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()