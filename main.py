import os
import requests
from flask import Flask
from telegram.ext import Updater, CommandHandler


# متغيرات عامة
COOKIES = {}
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # نخليه في Render env
CHAT_ID = os.environ.get("CHAT_ID")      # رقمك في تليغرام
URL = "https://algeria.blsspainglobal.com/DZA/Appointment/NewAppointment?msg=ZokWWxtCWRl2wwydQeR8iMSec%2BFRGm9yoFAG67YF%2FE46MHPKOT4E5B42DNnLtDwr&d=vIl4VHDNjFut2gxJov6ucTev%2Fo864siLsWLuqQOrNmjX70CyvfreOCQkRSP3l98sKS85uaee%2B6ZgvWphouiemjMKWOmpGRJuLnOETWreviSyKxWcXudgMEZduaH%2FCiiiyTH%2Fni8F9z1i9gJBfdIy5LaaF0xP%2F9ZYmO0Qv1i6bKv90KpYGr6tXxH28U955kWbvK9W9fraA98ON3bl%2BHuHr2GOMHOQ1BhqHg5LhvxmxEBfpoZ5XanOcHypferontrbLmKZYSycAWdU3xd%2BjyfXjs0pGgL%2BftFlczaOfLYOMSm6SsqBo086dTopNJNlBJqC"  # عدلها

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
def start(update, context):
    update.message.reply_text("✅ البوت راه يخدم!")

def ping(update, context):
    update.message.reply_text("✅ السيرفر شغال!")

def setcookies(update, context):
    global COOKIES
    try:
        # الكوكيز لازم تجيه بصيغة key=value key2=value2 ...
        cookie_text = " ".join(context.args)
        new_cookies = {}
        for c in cookie_text.split():
            k, v = c.split("=")
            new_cookies[k.strip()] = v.strip()
        COOKIES = new_cookies
        update.message.reply_text(f"✅ كوكيز تبدل: {COOKIES}")
    except Exception as e:
        update.message.reply_text(f"❌ خطأ: {e}")

def check(update, context):
    if check_appointments():
        context.bot.send_message(chat_id=CHAT_ID, text="🚨 مواعيد مفتوحة!")
    else:
        update.message.reply_text("⏳ مازال مكاينش.")

def run_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("setcookies", setcookies))
    dp.add_handler(CommandHandler("check", check))

    updater.start_polling()
    updater.idle()

@app.route("/")
def home():
    return "Flask Server is running with Telegram Bot!"

if __name__ == "__main__":
    run_bot()
