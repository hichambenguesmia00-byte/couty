from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Service is running"

def background_job():
    while True:
        print("⏳ Checking slots...")
        time.sleep(120)

if __name__ == "__main__":
    threading.Thread(target=background_job, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
