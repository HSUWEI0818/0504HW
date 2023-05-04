from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Fiqkwf+OEaMe/bSA1rczIqlEsm4/SW58rWp3y2aH7MT5STKDBQcHHo2j2JE2PNmPHCVEVqj1jBhSN/kLNPZZjs+TJyytZb/X3xbEaaKU3G71Qcr2X8XSy21IYTl+vG/YOSbbFxLOewxGr5QwIyL1jwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('18ad5f24a6e29e6c942ac87ebda55d90')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()