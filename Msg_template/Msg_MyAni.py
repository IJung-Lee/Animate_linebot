from linebot.models import *

##收藏清單
def ani_category(MyAni): 
    contents = []
    for ani in range(len(MyAni)):
        contents.append({
                "type": "text",
                "text": ani,
                "action": {
                    "type": "message",
                    "label": "action",
                    "text": "#" + ani
                },
                "color": "#006284",
                            "margin": "md"
        })

    flex_message = FlexSendMessage(
            alt_text = "番劇收藏清單",
            contents = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "以下為您的收藏清單，請點擊番名來查看動畫資訊。",
                            "wrap": True
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": contents
                        }
                    ]
                }
            }
    )
    return flex_message