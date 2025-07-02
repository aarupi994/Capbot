import telebot
import random

# 🔐 Bot Token
BOT_TOKEN = "8164700708:AAETr8jBRXitDzMzG5R-HBL4y4FwCRp9Fdk"

# 🤖 Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# 🎉 /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "👋 Hello! I'm Rose 🌹 bot.\nType anything and I'll reply instantly!"
    )

# 💬 Random reply list for other messages
replies = [
    "😎 I'm still here!",
    "⚡ Got your message!",
    "🧠 Thinking... thinking... done!",
    "📩 Message received!",
    "😕 Sorry, I'm not able to type anything... Can you type and send me (Hello)?",
    "🔄 You sent something again? Interesting!",
    "🤖 I'm a bot, but I remember you 😉",
    "👋 Still with you!",
    "💬 Let’s keep talking!"
]

# 🧠 Main message handler
@bot.message_handler(func=lambda m: True)
def handle_messages(message):
    text = message.text.lower()

    if "helo" in text or "hello" in text or "hi" in text:
        bot.send_message(message.chat.id, "TERE CHUT ME HELO DAL DUNGA CHUTIYE😂")
    else:
        response = random.choice(replies)
        bot.send_message(message.chat.id, response)
print("🤖 ROSE 🌹's bot started... Waiting for messages.")
bot.infinity_polling()
