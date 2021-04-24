from linebot.models import *
import Ani_info

def ani_bubble(name):
    Ani = {
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
                "text": name,
                "weight": "bold",
                "size": "lg",
                "wrap": True
            },
            {
                "type": "text",
                "text": "簡介",
                "wrap": True,
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
    return Ani

##動畫資訊 #圖文選單
def ani_information(AniName): 
    # data = Ani_info.get_ani_data(AniName)

    # intro = data[1]
    # image = data[2] 
    # tag =  data[3]
    # tag_color = data[4]
    # links = get_link_box(data[5], data[6])
    # content = ani_bubble(AniName, intro, image, tag, tag_color)
    content = ani_bubble(AniName)
    flex_message = FlexSendMessage(
            alt_text = AniName + "資訊",
            contents = content
    )
    return flex_message