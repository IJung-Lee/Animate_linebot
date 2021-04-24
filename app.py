import os
import re
from datetime import datetime

import Ani_info
from Msg_template import Msg_Ani
from Msg_template import Msg_info
from Msg_template import Msg_quick
from Msg_template import Msg_Template


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

    #動畫
    if re.match("#", msg):
        search_result = Ani_info.ani_search(msg[1:])
        if len(search_result) > 1:
            message = Msg_quick.ani_name_select(search_result)
            line_bot_api.push_message(uid, message)
        elif len(search_result) == 1:
            ani_data = Ani_info.get_ani_data(search_result[0])
            message = Msg_info.ani_information(ani_data)
            line_bot_api.push_message(uid, message)
        else:
            line_bot_api.push_message(uid, TextSendMessage('查無此番劇，請重新搜尋。'))
    
    #時間
    elif re.match("時間", msg):
        message = Msg_Template.week_menu()
        line_bot_api.push_message(uid, message)

    elif re.match("星期", msg):
        week = msg[2] 
        ani_data = Ani_info.get_week_data(week)
        content = Msg_Ani.ani_week(week, ani_data)
        line_bot_api.push_message(uid, content)

    #類別
    elif re.match("類別", msg):
        message = Msg_Template.category_menu()
        line_bot_api.push_message(uid, message)

    elif re.match(r'\s校園|戀愛|科幻|奇幻|日常|冒險|動作|其他', msg):
        ani_data = Ani_info.get_category_data(msg[:2])
        # line_bot_api.push_message(uid, TextSendMessage(str(ani_data)))
        content = Msg_Ani.ani_category(msg[:2], ani_data)
        line_bot_api.push_message(uid, content)

    # elif re.match("戀愛", msg):
    #     ani_data = Ani_info.get_category_data("戀愛")
    #     line_bot_api.push_message(uid, TextSendMessage(str(ani_data)))
    #     content = Msg_Ani.ani_category("戀愛", ani_data)
    #     line_bot_api.push_message(uid, content)

    # elif re.match("科幻番劇", msg):
    #     ani_data = Ani_info.get_category_data("科幻")
    #     content = Msg_Ani.ani_category("科幻", ani_data)
    #     line_bot_api.push_message(uid, content)

    # elif re.match("奇幻番劇", msg):
    #     ani_data = Ani_info.get_category_data("奇幻")
    #     content = Msg_Ani.ani_category("奇幻", ani_data)
    #     line_bot_api.push_message(uid, content)

    # elif re.match("日常番劇", msg):
    #     ani_data = Ani_info.get_category_data("日常")
    #     content = Msg_Ani.ani_category("日常", ani_data)
    #     line_bot_api.push_message(uid, content)

    # elif re.match("冒險番劇", msg):
    #     ani_data = Ani_info.get_category_data("冒險")
    #     content = Msg_Ani.ani_category("冒險", ani_data)
    #     line_bot_api.push_message(uid, content)
    
    # elif re.match("動作番劇", msg):
    #     ani_data = Ani_info.get_category_data("動作")
    #     content = Msg_Ani.ani_category("動作", ani_data)
    #     line_bot_api.push_message(uid, content)
    
    # elif re.match("其他番劇", msg):
    #     ani_data = Ani_info.get_category_data("其他")
    #     content = Msg_Ani.ani_category("其他", ani_data)
    #     line_bot_api.push_message(uid, content)

    else:
        line_bot_api.push_message(uid, TextSendMessage('很抱歉我們無法回應該訊息 \n\n輸入《時間》找尋每日番劇！ \n輸入《類別》查找各類番劇！'))



if __name__ == "__main__":
    app.run(debug=True)