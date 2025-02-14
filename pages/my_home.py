#程序打开步骤如下
#点击运行
#然后在控制台输出中找到
#streamlit run H:\网页制作2\网页制作\my_home.py [ARGUMENTS]
#这行代码
#复制streamlit run H:\网页制作2\网页制作\my_home.py
#注意！后面的 [ARGUMENTS]不要复制
#然后点击终端在
#streamlit run H:\网页制作2\网页制作\my_home.py
#后面输入
#python -m streamlit run H:\网页制作2\网页制作\my_home.py
#输入完按回车
"""我的主页"""
import streamlit as st
import time
from PIL import Image
import base64
page = st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智慧词典","我的留言区"])
def page_1():
    col1,col2 = st.columns([1,1])
    col3,col4 = st.columns([1,1])
    col5,col6 = st.columns([1,1])
    with col1:
        st.write("我的游戏之旅")
        st.image("使命召唤.jpg")
        st.write("使命召唤")
        st.write("《使命召唤》（Call of Duty）是由动视发行的第一人称射击游戏系列，自2003年推出以来广受欢迎。游戏以二战为起点，逐步扩展至现代战争和未来科幻题材，凭借高质量的画面、引人入胜的剧情和紧张刺激的多人模式成为经典。其不仅推动了FPS游戏的发展，还对军事文化和社会历史教育产生了深远影响，成为全球知名的游戏品牌。")
    with col2:
        st.image("原神.jpeg")
        st.write("原神")
        word2 = st.text_input("请选择你要播放的音乐的序号（1-22）")
        if word2 and word2.isdigit() and 1 <= int(word2) <= 22:
            with open(f"{word2}.mp3", "rb") as f:
                mymp3 = f.read()
            st.audio(mymp3, format="audio/mp3", start_time=0)
        st.write("《原神》是由中国游戏公司米哈游开发并发行的一款开放世界动作角色扮演游戏。游戏于2020年9月28日正式上线，支持多平台游玩，包括PC、手机、PlayStation 4和PlayStation 5。游戏的背景设定在一个名为提瓦特的幻想世界，这个世界由七个不同的国家组成，每个国家对应一种元素。")
        st.write("在游戏中，玩家将扮演一位名为“旅行者”的角色，探索广阔的世界，解开隐藏的秘密，并与其他角色互动。游戏结合了探索、解谜和战斗元素，玩家可以操控多个角色，每个角色都有独特的技能和元素属性。")
        st.write("《原神》以其精美的画面、丰富的剧情和创新的玩法吸引了大量玩家。游戏的开放世界设计让玩家能够自由探索各种地形和场景，同时还有许多隐藏的任务和宝藏等待发现。此外，游戏还支持多人合作模式，玩家可以邀请好友一起组队探索世界、挑战副本。")
        st.write("《原神》的成功不仅在于其高质量的游戏内容，还在于其定期更新和扩展的游戏内容。米哈游每隔一段时间就会推出新的角色、剧情和活动，保持了玩家的新鲜感和持续兴趣。")
        st.write("总的来说，《原神》是一款兼具深度和广度的游戏，适合喜欢开放世界探索和角色扮演游戏的玩家。它的成功不仅为中国游戏产业赢得了国际声誉，也为全球玩家提供了一款高质量的游戏体验。")
    with col3:
        st.image("王者荣耀.jpeg")
        st.write("王者荣耀")
        st.write("《王者荣耀》是由腾讯游戏开发并运营的一款多人在线战术竞技游戏（MOBA），自2015年")
        st.write("上线以来迅速成为中国最 popular 的手游之一。游戏以5v5对战为核心玩法，玩家选择不同英雄，通过")
        st.write("策略配合击败对手、摧毁敌方水晶。拥有超过100位各具特色的英雄，涵盖多种职业定位，满足不同玩家需求。")
        st.write("游戏支持语音社交，便于好友组队开黑。凭借精良制作和持续更新，《王者荣耀》不仅在国内市场占据领先地位，")
        st.write("还在全球范围内拥有大量粉丝，成为现象级手游代表。")
    with col4:
        st.image("和平精英.jpg")
        st.write("和平精英")
        st.write("《和平精英》是由腾讯光子工作室群开发并发行的一款战术竞技类射击游戏，于2019年5月8日正式上线。游戏以“大逃杀”玩法为核心，最多支持100名玩家同场竞技，通过搜集武器、物资，击败其他玩家，最终成为幸存者。游戏采用虚幻引擎4打造，画面精美细腻，操作流畅，尤其在移动端表现出色。凭借创新玩法、丰富内容和持续更新，《和平精英》迅速成为中国乃至全球范围内最受欢迎的战术竞技手游之一，深受广大玩家喜爱。")
    with col5:
        st.image("暗区突围.jpeg")
        st.write("暗区突围")
        st.write("《暗区突围》是由腾讯魔方工作室自主研发的一款硬核战术射击手游，主打PVP与PVE结合的沉浸式战场体验。游戏以“携带物资成功撤离”为核心目标，玩家需在危机四伏的暗区中搜集资源、制定战术，并与其他玩家或AI敌人对抗。与传统射击游戏不同，其开放目标设定允许自由选择策略——全装强攻、半装游走或裸装潜行。成功撤离后，战利品可出售换币或用于枪械深度改装（700+配件）。游戏包含伪装潜入（随机装备/伪装友军）和战术行动（自带装备/任务驱动）双模式，搭配动态战局与高拟真操作（如手动换弹、真实弹道），塑造出兼具策略性与心跳体验的暗区战场")
    with col6:
        st.image("我的世界.jpeg")
        st.write("我的世界")
        st.write("《我的世界》（Minecraft）是由Mojang Studios开发的沙盒建造游戏，最初由Markus Persson（Notch）于2009年5月发布测试版，2011年正式发行。玩家可在3D像素化世界中自由探索、采集资源，通过放置或破坏方块建造建筑，支持生存（对抗怪物、管理资源）与创造（无限资源、自由建造）双模式。游戏涵盖红石电路、指令系统、多人联机等玩法，并拥有末地、下界等扩展维度。2014年微软以25亿美元收购Mojang，2017年网易代理中国版上线。截至2021年，其全球销量超2.38亿份，月活玩家达1.4亿，成为史上最畅销游戏，覆盖PC、主机及移动端全平台。")

        with open("霞光.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
        st.image("滑雪.png")
def page_2():#换色
    st.write(":sunglasses:欢迎进入换色程序:sunglasses:")
    upload_file = st.file_uploader("上传图片",type=["jpg","png","jpeg"])
    if upload_file:
        file_name = upload_file.name
        file_type = upload_file.type
        file_size = upload_file.size
        img = Image.open(upload_file)
        st.image(img)
        st.image(img_change(img))#展示换色图片
def img_change(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][0]
            g = img_array[x,y][1]
            b = img_array[x,y][2]
            img_array[x,y]=(255-r,255-g,255-b)#bbg,rrg,rbg,ggr
    return img
    
def img_L(img):
    img = img.convert("L")
    return img

def page_3():
    st.write("欢迎进入词典系统")
    st.image("编程猫1.jpg")
    with open("words_space.txt","r",encoding='utf-8')as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        #字典名[键名] = 值
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding='utf-8') as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    #输入框组件
    word = st.text_input("请输入需要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt","w",encoding='utf-8') as f:
            message = ""
            for k,v in times_dict.items():
                message += str(k)+"#"+str(v)+"\n"
            message = message[:-1]
            f.write(message)
        st.write("查询次数：",times_dict[n])
    elif word == "张宇翔":
        st.image("大胆.png")
        st.write("你确定要这么做吗？")
        word1 = st.text_input("请做选择：是或否")
        if word1 == "是":
            st.write("算你懂事")
            st.image("大胆2.jpg")
    elif word == "原神启动":
        st.image("原神.jpeg")
        word2 = st.text_input("请选择你要播放的音乐的序号（1-22）")
        if word2 and word2.isdigit() and 1 <= int(word2) <= 22:
            with open(f"{word2}.mp3", "rb") as f:
                mymp3 = f.read()
            st.audio(mymp3, format="audio/mp3", start_time=0)
def page_4():
    st.write("-------★网站留言区★-------")
    with open("leave_messages.txt","r",encoding='utf-8')as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message("🌞"):
                st.write(i[1],":",i[2])
        elif i[1] == "编程猫":
            with st.chat_message("🍥"):
                st.write(i[1],":",i[2])
    name = st.selectbox("我是谁？",["阿短","编程猫"])
    new_message = st.text_input("请输入留言内容：")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
    with open ("leave_messages.txt","w",encoding='utf-8')as f:
        message = ""
        for i in messages_list:
            message += i[0]+"#"+i[1]+"#"+i[2] +"\n"
        message = message[:-1]
        f.write(message)
        st.write("你觉得本网站还有什么可以优化？")
        cb1 = st.checkbox("没什么可优化的，都挺好")
        cb2 = st.checkbox("这个网站有点low")
        cb3 = st.checkbox("建议可以增加一些图片")
        cb4 = st.checkbox("建议可以多加一些文字说明")
        if    st.button("确定"):
            if cb1 == True and cb2 == False and cb3 == False and cb4 == False:
                st.write("还是你有品位")
                st.image("大胆2.jpg")
            elif cb1 == False and cb2 == True and cb3 == False and cb4 == False:
                st.write("你还是有点“可爱”")
            elif cb1 == False and cb2 == False and cb3 == False and cb4 == False:
                st.write("必须给面子做出选择")
                st.image("大胆.png")

def bigping(main_bg_path):#大背景
    main_bg_ext = "jpeg" #背景图片格式 使用滑雪.png.故声明png格式
    with open (main_bg_path,"rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{encoded_string});
            background-size : cover; /* 确保背景图片覆盖整个页面 */
        }}
        </style>
      """,
        unsafe_allow_html =True
    )

def sidebar_bg(side_bg_path):
    side_bg_ext = "jpeg"#声明图片格式
    with open (side_bg_path,"rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid = 'stSidebar'] > div:first-child{{
        background: url(data:image/{side_bg_ext};base64,{encoded_string});
        }}

        </style>
      """,
        unsafe_allow_html =True
    )
bigping("纸.jpeg")
sidebar_bg("星空.jpeg")
if page == "我的兴趣推荐":
    page_1()
elif page == "我的图片处理工具":
    page_2()
elif page == "我的智慧词典":
    page_3()
elif page == "我的留言区":
    page_4()
