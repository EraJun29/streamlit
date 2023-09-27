import streamlit as st
import pandas as pd
import numpy as np

st.title("title") # タイトル
st.header("header") # ヘッダー
st.write("write") # 表示
st.markdown("# markdown") # マークダウンで表示
st.text("text") # テキスト表示

st.button("button") # ボタン
st.selectbox("selectbox", ("select1", "select2")) # セレクトボックス
st.multiselect("multiselectbox", ("select1", "select2")) # 複数選択可能なセレクトボックス
st.radio("radiobutton", ("radio1", "radio2")) # ラジオボタン
st.text_input("text input") # 文字入力(1行)
st.text_area("text area") # 文字入力(複数行)
st.slider("slider", 0, 100, 50) # スライダー
st.file_uploader("Choose file") # ファイルアップロード

dataframe = pd.read_csv('C:\streamlit\streamlit-sample\yatusiro.csv',encoding = 'shift_jis')
st.write(dataframe)

st.line_chart(dataframe)