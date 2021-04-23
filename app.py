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


flex_message = FlexSendMessage(
        alt_text = "Week Menu",
        contents = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "5:2",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "番劇時間",
                "weight": "bold",
                    "size": "xl",
                    "align": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週一",
                            "text": "星期一番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週二",
                            "text": "星期二番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週三",
                            "text": "星期三番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        }
                        ],
                        "paddingAll": "none"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週四",
                            "text": "星期四番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週五",
                            "text": "星期五番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週六",
                            "text": "星期六番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "週日",
                            "text": "星期日番劇查詢"
                            },
                            "height": "sm",
                            "style": "link"
                        }
                        ],
                        "paddingAll": "none"
                    },
                    {
                        "type": "spacer"
                    }
                    ],
                    "paddingAll": "xs"
                }
                ],
                "paddingAll": "md"
            }
        }
)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id # 發訊者ID

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