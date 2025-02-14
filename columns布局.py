import streamlit as st

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
    word2 = st.text_input("请选择你要播放的音乐的序号（1-64）")
    if word2 == "1":
        with open("1.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "2":
        with open("2.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "3":
        with open("3.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "4":
        with open("4.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "5":
        with open("5.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "6":
        with open("6.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "7":
        with open("7.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "8":
        with open("8.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "9":
        with open("9.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "10":
        with open("10.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "11":
        with open("11.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "12":
        with open("12.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "13":
        with open("13.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "14":
        with open("14.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "15":
        with open("15.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "16":
        with open("16.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "17":
        with open("17.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "18":
        with open("18.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "19":
        with open("19.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "20":
        with open("20.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "21":
        with open("21.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "22":
        with open("22.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "23":
        with open("23.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "24":
        with open("24.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "25":
        with open("25.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "26":
        with open("26.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "27":
        with open("27.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "28":
        with open("28.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "29":
        with open("29.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "30":
        with open("30.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "31":
        with open("31.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "32":
        with open("32.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "33":
        with open("33.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "34":
        with open("34.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "35":
        with open("35.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "36":
        with open("36.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "37":
        with open("37.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "38":
        with open("38.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "39":
        with open("39.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "40":
        with open("40.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "41":
        with open("41.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "42":
        with open("42.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "43":
        with open("43.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "44":
        with open("44.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "45":
        with open("45.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "46":
        with open("46.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "47":
        with open("47.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "48":
        with open("48.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "49":
        with open("49.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "50":
        with open("50.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "51":
        with open("51.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "52":
        with open("52.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "53":
        with open("53.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "54":
        with open("54.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "55":
        with open("55.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "56":
        with open("56.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "57":
        with open("57.mp3","rb") as f:
                mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "58":
        with open("58.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "59":
        with open("59.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "60":
        with open("60.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "61":
        with open("61.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "62":
        with open("62.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "63":
        with open("63.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    if word2 == "64":
        with open("64.mp3","rb") as f:
            mymp3 = f.read()
        st.audio(mymp3,format = "audio/mp3",start_time = 0)
    st.write("《原神》是由中国游戏公司米哈游开发并发行的一款开放世界动作角色扮演游戏。游戏于2020年9月28日正式上线，支持多平台游玩，包括PC、手机、PlayStation 4和PlayStation 5。游戏的背景设定在一个名为提瓦特的幻想世界，这个世界由七个不同的国家组成，每个国家对应一种元素。")
    st.write("在游戏中，玩家将扮演一位名为“旅行者”的角色，探索广阔的世界，解开隐藏的秘密，并与其他角色互动。游戏结合了探索、解谜和战斗元素，玩家可以操控多个角色，每个角色都有独特的技能和元素属性。")
    st.write("《原神》以其精美的画面、丰富的剧情和创新的玩法吸引了大量玩家。游戏的开放世界设计让玩家能够自由探索各种地形和场景，同时还有许多隐藏的任务和宝藏等待发现。此外，游戏还支持多人合作模式，玩家可以邀请好友一起组队探索世界、挑战副本。")
    st.write("《原神》的成功不仅在于其高质量的游戏内容，还在于其定期更新和扩展的游戏内容。米哈游每隔一段时间就会推出新的角色、剧情和活动，保持了玩家的新鲜感和持续兴趣。")
    st.write("总的来说，《原神》是一款兼具深度和广度的游戏，适合喜欢开放世界探索和角色扮演游戏的玩家。它的成功不仅为中国游戏产业赢得了国际声誉，也为全球玩家提供了一款高质量的游戏体验。")
with col3:
    st.image("王者荣耀.jpeg")
    st.write("王者荣耀")
    st.write("《王者荣耀》是由腾讯游戏开发并运营的一款多人在线战术竞技游戏（MOBA），自2015年上线以来迅速成为中国最 popular 的手游之一。游戏以5v5对战为核心玩法，玩家选择不同英雄，通过策略配合击败对手、摧毁敌方水晶。拥有超过100位各具特色的英雄，涵盖多种职业定位，满足不同玩家需求。游戏支持语音社交，便于好友组队开黑。凭借精良制作和持续更新，《王者荣耀》不仅在国内市场占据领先地位，还在全球范围内拥有大量粉丝，成为现象级手游代表。")
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
