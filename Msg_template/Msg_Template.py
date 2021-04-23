from linebot.models import *

###########################
# 星期選單###圖片須改
def week_menu(): 
    flex_message = FlexSendMessage(
            alt_text = "Week Menu",
            contents = {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",  ##待修改圖片
                            "size": "full",
                            "aspectRatio": "5:2",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "番劇時間",
                                "weight": "bold",
                                "size": "xl",
                                "align": "center"
                            }
                            ],
                            "paddingAll": "md"
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "週一",
                                    "text": "星期一番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "週二",
                                    "text": "星期二番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "週三",
                                    "text": "星期三番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                }
                                ],
                                "paddingAll": "none"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "週四",
                                    "text": "星期四番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "週五",
                                    "text": "星期五番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "週六",
                                    "text": "星期六番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "週日",
                                    "text": "星期日番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                }
                                ],
                                "paddingAll": "none"
                            },
                            {
                                "type": "spacer"
                            }
                            ],
                            "paddingAll": "xs"
                        }
            }
    )
    return flex_message


# 類別選單 ###圖片須改
def category_menu(): 
    flex_message = FlexSendMessage(
            alt_text = "Category Menu",
            contents = {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",  #待修改圖片
                            "size": "full",
                            "aspectRatio": "5:2",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "番劇類別",
                                "weight": "bold",
                                "size": "xl",
                                "align": "center"
                            }
                            ],
                            "paddingAll": "md"
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "校園",
                                    "text": "校園番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "戀愛",
                                    "text": "戀愛番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "科幻",
                                    "text": "科幻番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "奇幻",
                                    "text": "奇幻番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                }
                                ],
                                "paddingAll": "none"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "日常",
                                    "text": "日常番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "冒險",
                                    "text": "冒險番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "動作",
                                    "text": "動作番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "message",
                                    "label": "其他",
                                    "text": "其他番劇查詢"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                }
                                ],
                                "paddingAll": "none"
                            },
                            {
                                "type": "spacer"
                            }
                            ],
                            "paddingAll": "xs"
                        }
            }
    )
    return flex_message