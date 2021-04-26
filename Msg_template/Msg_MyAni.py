from linebot.models import *

##收藏內容
def get_my_ani(AniName_list):
    contents = []
    for i in AniName_list:
        collect = {
            "type": "text",
            "text": "⊛ " + i,
            "size": "md",
            "wrap": False,
            "margin": "sm",
            "action": {
                "type": "message",
                "label": "action",
                "text": "#" + i
            }
        }
        contents.append(collect)
    return contents


# 收藏清單
def my_ani(Ani_list): 
    contents = get_my_ani(Ani_list)
    flex_message = FlexSendMessage(
        alt_text = "My Animation",
        contents = {
            "type": "bubble",
            "size": "kilo",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/UpwzZpL.png",
                "size": "full",
                "aspectRatio": "5:2",
                "aspectMode": "cover",
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": contents,
                "paddingAll": "lg"
            }
        },
        quick_reply = QuickReply(items=[QuickReplyButton(action=MessageAction(label = "清空收藏", text="清空收藏"))])
    )
    return flex_message