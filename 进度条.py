import streamlit as st
import time
#进度条

roading = st.progress(0,"★开始加载★")

for i in range(1,101,1):
    time.sleep(0.2)
    roading.progress(i,"正在加载"+str(i)+"%")
    if i == 85:
        roading.progress(85,"正在加载游戏资源，请稍候")
        time.sleep(8)
    if i == 99:
        roading.progress(99,"即将进入，请准备")
        time.sleep(10)
roading.progress(100,"★加载完毕★")
