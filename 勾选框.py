import streamlit as st

#勾选框checkbox
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