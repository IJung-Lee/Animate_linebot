import re
# from pymongo import MongoClient
# import pymongo
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *

# import Msg_Ani
from Msg_template import week_menu
from Msg_Template import category_menu

import Ani_info

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id) #獲取使用者資訊
    uid = profile.user_id # 使用者ID



    #星期
    if re.match("番劇時間", msg):
        reply = Msg_Template.week_menu()
        line_bot_api.reply_message(event.reply_token, reply)
    
    #類別
    elif re.match("番劇類別", msg):
        reply = Msg_Template.category_menu()
        line_bot_api.reply_message(event.reply_token, reply)


if __name__ == "__main__":
    app.run(debug=True)