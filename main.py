import os
import threading
import requests
from flask import Flask
from telegram import Update
from telegram.ext import Updater,CommandHandler, CallbackContext

# متغيرات
COOKIES = {}
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = "https://algeria.blsspainglobal.com/DZA/Appointment/NewAppointment?msg=ZokWWxtCWRl2wwydQeR8iMSec%2BFRGm9yoFAG67YF%2FE46MHPKOT4E5B42DNnLtDwr&d=vIl4VHDNjFut2gxJov6ucTev%2Fo864siLsWLuqQOrNmjX70CyvfreOCQkRSP3l98sKS85uaee%2B6ZgvWphouiemjMKWOmpGRJuLnOETWreviSyKxWcXudgMEZduaH%2FCiiiyTH%2Fni8F9z1i9gJBfdIy5LaaF0xP%2F9ZYmO0Qv1i6bKv90KpYGr6tXxH28U955kWbvK9W9fraA98ON3bl%2BHuHr2GOMHOQ1BhqHg5LhvxmxEBfpoZ5XanOcHypferontrbLmKZYSycAWdU3xd%2BjyfXjs0pGgL%2BftFlczaOfLYOMSm6SsqBo086dTopNJNlBJqC"

app = Flask(__name__)

# -------- التحقق من المواعيد --------
def check_appointments():
    global COOKIES
    headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"}
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

# -------- أوامر البوت --------
def start(update, context):
    update.message.reply_text("✅ البوت راه يخدم!")

def ping(update, context):
    update.message.reply_text("✅ السيرفر شغال!")

def setcookies(update, context):
    global COOKIES
    try:
        # نجيب النص كامل بعد الكوموند (حتى لو فيه سطور متعددة)
        cookie_text = update.message.text.replace("/setcookies", "", 1).strip()
        
        new_cookies = {}
        for line in cookie_text.splitlines():
            if "=" in line:
                k, v = line.split("=", 1)  # نقطع غير أول "="
                new_cookies[k.strip()] = v.strip()
        
        if new_cookies:
            # نمسح القديم ونخزن الجديد فقط
            COOKIES = new_cookies
            saved = "\n".join([f"{k}=..." for k in COOKIES.keys()])
            update.message.reply_text(f"✅ تم تخزين الكوكيز الجديد (تم مسح القديم):\n{saved}")
        else:
            update.message.reply_text("⚠️ ما لقيتش أي كوكيز في النص!")

    except Exception as e:
        update.message.reply_text(f"❌ خطأ: {e}")


def check(update, context):
    if check_appointments():
        context.bot.send_message(chat_id=CHAT_ID, text="🚨 مواعيد مفتوحة!")
    else:
        update.message.reply_text("⏳ مازال مكاينش.")


def probe(update: Update, context: CallbackContext):
    if not COOKIES:
        update.message.reply_text("⚠️ ما كاش كوكيز مخزّنين. استعمل /setcookies باش تزيدهم.")
        return

    session = requests.Session()
    # هيدرز “واقعية” (تبان كيما كروم)
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
        "Referer": "https://algeria.blsspainglobal.com/",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    })
    # زيد الكوكيز اللي عطيتهم
    try:
        session.cookies.update(COOKIES)
    except Exception as e:
        update.message.reply_text(f"❌ مشكل في parsing الكوكيز: {e}")
        return

    home = "https://algeria.blsspainglobal.com/"
    target = "https://algeria.blsspainglobal.com/DZA/Appointment/NewAppointment?msg=ZokWWxtCWRl2wwydQeR8iMSec%2BFRGm9yoFAG67YF%2FE46MHPKOT4E5B42DNnLtDwr&d=vIl4VHDNjFut2gxJov6ucTev%2Fo864siLsWLuqQOrNmjX70CyvfreOCQkRSP3l98sKS85uaee%2B6ZgvWphouiemjMKWOmpGRJuLnOETWreviSyKxWcXudgMEZduaH%2FCiiiyTH%2Fni8F9z1i9gJBfdIy5LaaF0xP%2F9ZYmO0Qv1i6bKv90KpYGr6tXxH28U955kWbvK9W9fraA98ON3bl%2BHuHr2GOMHOQ1BhqHg5LhvxmxEBfpoZ5XanOcHypferontrbLmKZYSycAWdU3xd%2BjyfXjs0pGgL%2BftFlczaOfLYOMSm6SsqBo086dTopNJNlBJqC"

    try:
        # خطوة 1: ديما جرّب الصفحة الرئيسية (بزاف مواقع تحط set-cookie هنا)
        r1 = session.get(home, timeout=20, allow_redirects=True)
        set_from_home = [c.name for c in session.cookies]

        # خطوة 2: الهدف
        r2 = session.get(target, timeout=20, allow_redirects=False)

        snippet = r2.text[:300].replace("\n", " ")
        msg = (
            "=== PROBE ===\n"
            f"🏠 HOME: {r1.status_code} -> {r1.url}\n"
            f"🍪 Cookies after HOME: {', '.join(set_from_home) or '(none)'}\n"
            f"🎯 TARGET: {r2.status_code}\n"
        )
        if r2.is_redirect:
            msg += f"↪️ Redirect to: {r2.headers.get('Location')}\n"
        if r2.status_code in (401, 403):
            msg += "❌ مرفوض (غالبًا IP/Token مرتبط بالجلسة الأصلية).\n"
        elif "Access Denied" in r2.text or "403" in snippet:
            msg += "❌ Access Denied من الـ WAF.\n"
        elif "Currently, no slots are available" in r2.text:
            msg += "✅ وصلت للصفحة: ما كاش مواعيد حالياً.\n"
        else:
            msg += "ℹ️ وصلنا رد مختلف، شوف الـ snippet.\n"

        msg += f"\n🔎 Snippet: {snippet}"
        update.message.reply_text(msg[:4000])

    except Exception as e:
        update.message.reply_text(f"⚠️ خطأ: {e}")


# -------- تشغيل البوت في Thread --------
def run_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("setcookies", setcookies))
    dp.add_handler(CommandHandler("check", check))
    dp.add_handler(CommandHandler("probe", probe))

    updater.start_polling()
    updater.idle()


# -------- Route Flask --------
@app.route("/")
def home():
    return "✅ Flask + Telegram Bot are running!"

# -------- تشغيل --------
if __name__ == "__main__":
    # نطلق البوت في Thread مستقل
    t = threading.Thread(target=run_bot)
    t.daemon = True
    t.start()

    # نشغل Flask (باش Render يشوف Port مفتوح)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
