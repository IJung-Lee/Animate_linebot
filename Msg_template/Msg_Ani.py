from linebot.models import *

import Ani_info

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

##收藏判斷
def ani_collect(collect , AniName):
    if collect == True:
        action = {
            "type": "message",
            "label": "已收藏",
            "text": "取消收藏" + AniName
        }
    elif collect == False:
        action = {
            "type": "message",
            "label": "收藏",
            "text": "收藏" + AniName
        }
    return action


##動畫bubble
def ani_bubble(name, intro, image, tag, tag_color ,links, collect):
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
                        "action": ani_collect(collect, name),
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



##動畫資訊 #圖文選單
def ani_information(AniName, collect): 
    data = get_ani_data(AniName)

    name = data[0]
    intro = data[1]
    image = data[2] 
    tag =  data[3]
    tag_color = data[4]
    links = get_link_box(data[5], data[6])
    content = ani_bubble(name, intro, image, tag, tag_color ,links, collect)
    flex_message = FlexSendMessage(
            alt_text = name + "資訊",
            contents = content
    )
    return flex_message

##星期資訊 #多頁訊息
def ani_week(AniWeek): 
    data = Ani_info.get_week_data(AniWeek)

    name = data[0]
    intro = data[1]
    image = data[2] 
    tag =  data[3]
    tag_color = data[4]
    web = data[5]
    url = data[6]

    ani_bubbles = []
    for i in range(len(name)):
        links = links = get_link_box(web[i], url[i])
        ani_bubbles.append(ani_bubble(name[i], intro[i], image[i], tag[i], tag_color[i] ,links, collect[i]))

    flex_message = FlexSendMessage(
            alt_text = AniWeek + "番劇資訊",
            contents = {
                        "type": "carousel",
                        "contents": ani_bubbles
            }
    )
    return flex_message

##類別資訊 ＃多頁訊息
def ani_category(AniCategory): 
    data = Ani_info.get_category_data(AniCategory)

    name = data[0]
    intro = data[1]
    image = data[2] 
    tag =  data[3]
    tag_color = data[4]
    web = data[5]
    url = data[6]

    ani_bubbles = []
    for i in range(len(name)):
        links = links = get_link_box(web[i], url[i])
        ani_bubbles.append(ani_bubble(name[i], intro[i], image[i], tag[i], tag_color[i] ,links, collect[i]))

    flex_message = FlexSendMessage(
            alt_text = AniCategory + "番劇資訊",
            contents = {
                        "type": "carousel",
                        "contents": ani_bubbles
            }
    )
    return flex_message


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