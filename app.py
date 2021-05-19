

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

line_bot_api = LineBotApi('XG1W3hNciszo2GwIjlAmRZ4p80OQ3Ap1FPtcF67R0h77iz7gvF4gBTzjxWDFXEAgY5WzXyFWGCcHY7KdOxd9xF0SKW6gzoAMVqRwZjQMK5dS+2qBN3IRSDNq9Nri/FZ3ifmkHU0P84Ag0Zd4+Pq7aAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2ab8e04f307a061960866f6053a13889')


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
    except InvalidSignature Error:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '蛤'

    if msg == '安安':
        r = '安安 '
    elif msg == '你吃飯了嗎':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main_ _":
    app.run()