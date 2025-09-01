import os
import requests
from flask import Flask
from telegram.ext import Application, CommandHandler

# متغيرات عامة
COOKIES = {}
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # نخليه في Render env
CHAT_ID = os.environ.get("CHAT_ID")      # رقمك في تليغرام
URL = "https://algeria.blsspainglobal.com/DZA/Appointment/NewAppointment?msg=..."  # عدلها

app = Flask(__name__)

# وظيفة تحقق من الموقع
def check_appointments():
    global COOKIES
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        r = requests.get(URL, headers=headers, cookies=COOKIES, timeout=20)
        if "Currently, no slots are available" in r.text:
            return False
        elif "Appointment" in r.text or "slot" in r.text:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False

# بوت تليغرام
async def start(update, context):
    await update.message.reply_text("✅ البوت راه يخدم!")

async def ping(update, context):
    await update.message.reply_text("✅ السيرفر شغال!")

async def setcookies(update, context):
    global COOKIES
    try:
        cookie_text = " ".join(context.args)
        new_cookies = {}
        for c in cookie_text.split():
            k, v = c.split("=")
            new_cookies[k.strip()] = v.strip()
        COOKIES = new_cookies
        await update.message.reply_text(f"✅ كوكيز تبدل: {COOKIES}")
    except Exception as e:
        await update.message.reply_text(f"❌ خطأ: {e}")

async def check(update, context):
    if check_appointments():
        await context.bot.send_message(chat_id=CHAT_ID, text="🚨 مواعيد مفتوحة!")
    else:
        await update.message.reply_text("⏳ مازال مكاينش.")

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("setcookies", setcookies))
    application.add_handler(CommandHandler("check", check))

    application.run_polling()

@app.route("/")
def home():
    return "Flask Server is running with Telegram Bot!"

if __name__ == "__main__":
    run_bot()
