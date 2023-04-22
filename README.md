# tg_simple

Simple telegram scripts

Send text message to chat:

```
from tg_simple.tg_msg import TgMsg

TG_TOKEN = # Telegram bot API token
TG_CHAT_ID = # Destination chat id (user id)

msg = "<b>Hello!</b> I'm notify from tg_simple."

tg = TgMsg(TG_TOKEN)
tg.send_text(msg, TG_CHAT_ID, html=True)

```
