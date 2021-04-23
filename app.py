import os
import re
from datetime import datetime

from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from Msg_template import Msg_Template

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))

# 監聽所有來自 /callback 的 Post Request
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
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id # 發訊者ID

    #時間
    if re.match("時間", msg):
        content = Msg_Template.week_menu()
        line_bot_api.push_message(uid, content)

    #類別
    elif re.match("類別", msg):
        content = Msg_Template.category_menu()
        line_bot_api.push_message(uid, content)

    else:
        line_bot_api.push_message(uid, TextSendMessage('我不懂你在說啥'))



if __name__ == "__main__":
    app.run(debug=True)