import time
from telegram import Bot
from strategy import check_bias, check_entry

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHANNEL_ID"

bot = Bot(token=TOKEN)

pairs = ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD"]

def send_signal(pair, direction, price):
    message = f"""
📊 {pair} SIGNAL

Direction: {direction}
Timeframe: H1
Bias: H4
Entry Price: {price}

Strategy:
EMA 21 / EMA 50 / RSI 14
"""
    bot.send_message(chat_id=CHAT_ID, text=message)

while True:
    for pair in pairs:
        # MOCK DATA (replace with real data later)
        h4 = {"price": 1.20, "ema21": 1.18, "ema50": 1.15, "rsi": 60}
        h1 = {"price": 1.19, "ema50": 1.17, "rsi": 45}

        bias = check_bias(h4)
        entry = check_entry(h1, bias)

        if entry:
            send_signal(pair, entry, h1["price"])

    time.sleep(3600)
