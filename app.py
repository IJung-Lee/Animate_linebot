import os
import re
from datetime import datetime

from Msg_template import Ani_info
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
            content = Msg_quick.ani_name_select(search_result)
            line_bot_api.push_message(uid, content)
        elif len(search_result) == 1:
            # line_bot_api.push_message(uid, TextSendMessage(search_result[0]))
            content = Msg_info.ani_information(search_result[0])
            line_bot_api.push_message(uid, content)
        else:
            line_bot_api.push_message(uid, TextSendMessage('查無此番劇，請重新搜尋。'))
    
    #時間
    elif re.match("時間", msg):
        flex_message = Msg_Template.week_menu()
        line_bot_api.push_message(uid, flex_message)


    #類別
    elif re.match("類別", msg):
        flex_message = Msg_Template.category_menu()
        line_bot_api.push_message(uid, flex_message)

    else:
        line_bot_api.push_message(uid, TextSendMessage('很抱歉我們無法回應該訊息 \n\n輸入《時間》找尋每日番劇！ \n輸入《類別》查找各類番劇！'))



if __name__ == "__main__":
    app.run(debug=True)