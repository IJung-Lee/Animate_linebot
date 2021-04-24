from linebot.models import *

##觀看網址button
def get_link_box(web, url):
    links = []
    for i in range(len(web)):
        link = {
                "type": "button",
                "action": {
                            "type": "uri",
                            "label": web[i],
                            "uri": url[i]
                },
                "height": "sm"
        }
        links.append(link)
    return links
    

def ani_bubble(name, intro, image, tag, tag_color, links):
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
                    "url": image,
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
                        "text": tag,
                        "size": "xs",
                        "align": "center",
                        "gravity": "center",
                        "color": "#ffffff"
                    }
                    ],
                    "backgroundColor": tag_color,
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
                "text": intro,
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
                    "contents": links,
                    "paddingAll": "sm"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "收藏",
                    "text": "收藏" + name
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
def ani_information(AniData): 
    # data = Ani_info.get_ani_data(AniName)
    name = AniData[0]
    intro = AniData[1]
    image = AniData[2] 
    tag =  AniData[3]
    tag_color = AniData[4]
    links = get_link_box(AniData[5], AniData[6])
    content = ani_bubble(name, intro, image, tag, tag_color, links)
    flex_message = FlexSendMessage(
            alt_text = name + "資訊",
            contents = content
    )
    return flex_message