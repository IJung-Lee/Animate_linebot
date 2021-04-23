from linebot.models import *


##動畫選擇 #quickly reply
def ani_name_select(AniName_list):
    QuickReplyButtons = []
    for ani in AniName_list:
        QuickReplyButtons.append(
            QuickReplyButton(
                action=MessageAction(
                    label = ani, 
                    text = "#" + ani
                )
            )
        )

    text_message = TextSendMessage(
                text = "請選擇您欲查詢的動漫" ,
                quick_reply = QuickReply(items = QuickReplyButtons)
    )
    return text_message