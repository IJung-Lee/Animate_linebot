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


def ani_information(AniName): 
    flex_message = FlexSendMessage(
            alt_text = name + "資訊",
            contents = {
                "type": "bubble",
                "size": "kilo",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/87Mhknm.png",
                            "size": "full",
                            "aspectRatio": "1.54:1",
                            "aspectMode": "cover"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "漫畫改編",
                                "size": "xs",
                                "align": "center",
                                "gravity": "center",
                                "color": "#ffffff"
                            }
                            ],
                            "backgroundColor": "#ff334b",
                            "position": "absolute",
                            "offsetStart": "15px",
                            "offsetTop": "15px",
                            "cornerRadius": "100px",
                            "height": "25px",
                            "paddingStart": "md",
                            "paddingEnd": "md"
                        }
                        ]
                    }
                    ],
                    "paddingAll": "0px"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "動漫",
                        "weight": "bold",
                        "size": "lg",
                        "wrap": true
                    },
                    {
                        "type": "text",
                        "text": "簡介",
                        "wrap": true,
                        "margin": "md",
                        "size": "xs",
                        "color": "#666666"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "uri",
                                "label": "巴哈姆特",
                                "uri": "https://ani.gamer.com.tw/animeVideo.php?sn=22220"
                                },
                                "height": "sm"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "uri",
                                "label": "bilibili",
                                "uri": "http://linecorp.com/"
                                },
                                "height": "sm"
                            }
                            ],
                            "paddingAll": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "收藏",
                            "text": "收藏"
                            },
                            "style": "primary",
                            "color": "#81C7D4",
                            "height": "sm"
                        }
                        ]
                    }
                    ],
                    "paddingAll": "15px"
                }
            }
    )
    return flex_message