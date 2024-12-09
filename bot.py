import feedparser
import os
from dotenv import load_dotenv
import telegram
import asyncio

load_dotenv() # load environment variables

# feed RSS and token bot
RSS_FEED_URL = "" # put url rss
BOT_TOKEN = os.getenv("TOKEN")
CHAT_ID = ""  # Telegram chat ID

bot = telegram.Bot(token=BOT_TOKEN)

sent_posts = set()

async def send_recent_posts():
    feed = feedparser.parse(RSS_FEED_URL)
    recent_posts = feed.entries[:5] 
    for entry in reversed(recent_posts): 
        await bot.send_message(
            chat_id=CHAT_ID,
            text=f"<a href='{entry.link}'>{entry.title}</a>",
            parse_mode="HTML"
        )
        sent_posts.add(entry.link)

async def check_new_posts():
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        if entry.link not in sent_posts:
            await bot.send_message(
                chat_id=CHAT_ID,
                text=f"<a href='{entry.link}'>{entry.title}</a>",
                parse_mode="HTML"
            )
            sent_posts.add(entry.link)

async def main():
    try:
        await send_recent_posts()
        while True:
            await asyncio.sleep(300) 
            await check_new_posts()

    except asyncio.CancelledError:
        print("Bot interrotto manualmente.")
    except KeyboardInterrupt:
        print("Interruzione del programma da parte dell'utente.")

if __name__ == "__main__":
    asyncio.run(main())