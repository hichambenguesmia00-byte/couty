from flask import Flask
import threading
from checker import run_checker

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ BLS slot checker is running!"

def start_checker():
    run_checker()

if __name__ == "__main__":
    # نشغل المراقبة في thread ثاني
    threading.Thread(target=start_checker, daemon=True).start()
    
    # Flask لازم يربط على 0.0.0.0 باش Render يقبل الخدمة
    app.run(host="0.0.0.0", port=10000)
