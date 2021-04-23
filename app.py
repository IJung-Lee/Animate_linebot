import os
import re
from datetime import datetime

# from Msg_template import Msg_Template

from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id # 發訊者ID
    flex_message = FlexSendMessage(
        alt_text='hello',
        contents={
            'type': 'bubble',
            'direction': 'ltr',
            'hero': {
                'type': 'image',
                'url': 'https://example.com/cafe.jpg',
                'size': 'full',
                'aspectRatio': '20:13',
                'aspectMode': 'cover',
                'action': { 'type': 'uri', 'uri': 'http://example.com', 'label': 'label' }
            }
        }
    )

    #時間
    if re.match("時間", msg):
        #flex_message = week_menu()
        line_bot_api.push_message(uid, flex_message)

    #類別
    elif re.match("類別", msg):
        #flex_message = Msg_Template.category_menu()
        line_bot_api.push_message(uid, flex_message)
    else:
        line_bot_api.push_message(uid, TextSendMessage('很抱歉我們無法回應該訊息 \n\n輸入《時間》找尋每日番劇！ \n輸入《類別》查找各類番劇！'))



if __name__ == "__main__":
    app.run(debug=True)