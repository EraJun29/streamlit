import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title("Stremlit 超入門")

st.write('DataFrame')

# df = pd.DataFrame(

#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']

# )
# st.dataframe(df)
# st.map(df)

# st.write('Interactive Widgets')

# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい、 ',
#     list(range(1,11))
# )
# st.write('あなたの好きな数字は',option,'です。')


# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味は、',text,'です。'
# 'あなたのコンディション:',condition

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1 }')
    bar.progress(i +1)
    time.sleep(0.1)



left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1：西日本工業大学の学部は何がありますか？')
expander1.write('工学部とデザイン学部があります')
expander2 = st.expander('問い合わせ2：それぞれのキャンパスはどこにありますか？')
expander2.write('工学部は小波瀬、デザイン学部は小倉にあります')
expander3 = st.expander('問い合わせ3：工学部ではどのようなことを学べますか')
expander3.write('機械科、電気科、土木科の各分野について学ぶことができます')





# if st.checkbox('Show Image'):

#     img = Image.open('八代バナナ_8月1.jpg')

#     st.image(img,caption = 'yatsushiro',use_column_width=True)

# st. table(df.style.highlight_max(axis=0))




