import pandas as pd

df = pd.read_csv('Ani_data.csv') 

def get_tag_color(tag):
    if tag == "漫畫改編":
        tag_color = "#ED784A"
    elif tag == "小說改編":
        tag_color = "#5DAC81"
    elif tag == "動畫原創":
        tag_color = "#2EA9DF"
    elif tag == "遊戲改編":
        tag_color = "#FF334B"

    return tag_color


##搜索動畫
def ani_search(ani_name):
    data = df[df["番名"].str.contains(ani_name)]
    ani = list(data["番名"].values)
    return ani


##動畫資訊
def get_ani_data(ani_name):
    name = ani_name
    data = df[df["番名"] == ani_name]
    intro = data.簡介.values[0]
    image = data.封面.values[0]
    tag = data.Tag.values[0]
    tag_color = get_tag_color(tag)
        
    web = []
    url = []
    web.append(data.平台1.values[0].split( )[0])
    url.append(data.平台1.values[0].split( )[1])
    if data.平台2.values[0] != "N":
        web.append(data.平台2.values[0].split( )[0])
        url.append(data.平台2.values[0].split( )[1])
    
    return name, intro, image, tag, tag_color, web, url


##星期資訊
def get_week_data(ani_week):
    data = df[df["星期"] == ani_week]
    data.reset_index(inplace=True)
    name = list(data.番名.values)
    intro = list(data.簡介.values)
    image = list(data.封面.values)
    tag = list(data.Tag.values)
    tag_color = [get_tag_color(x) for x in tag]
    
    web = []
    url = []
    for i in range(len(data)):
        a = []
        b = []
        a.append(data.平台1.values[i].split( )[0])
        b.append(data.平台1.values[i].split( )[1])
        if data.平台2.values[i] != "N":
            a.append(data.平台2.values[i].split( )[0])
            b.append(data.平台2.values[i].split( )[1])
        web.append(a)
        url.append(b)
    
    return name, intro, image, tag, tag_color, web, url


##類別資訊
def get_category_data(ani_cate):
    data = df[df[ani_cate] == 1]
    data.reset_index(inplace=True)
    name = list(data.番名.values)
    intro = list(data.簡介.values)
    image = list(data.封面.values)
    tag = list(data.Tag.values)
    tag_color = [get_tag_color(x) for x in tag]
    
    web = []
    url = []
    for i in range(len(data)):
        a = []
        b = []
        a.append(data.平台1.values[i].split( )[0])
        b.append(data.平台1.values[i].split( )[1])
        if data.平台2.values[i] != "N":
            a.append(data.平台2.values[i].split( )[0])
            b.append(data.平台2.values[i].split( )[1])
        web.append(a)
        url.append(b)
    
    return name, intro, image, tag, tag_color, web, url