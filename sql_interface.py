import streamlit as st
from smart_sql import get_answer
import sqlite3
import pandas as pd

#вставить верхушку исходной sql таблички
st.title('Ask anything about my table')

df_original = pd.read_csv('data/bank_data.csv')
st.dataframe(df_original.head(5))

question = st.text_input('Enter your question')
if question:
    query = get_answer(question)
    conn = sqlite3.connect('data/bank_data.db')
    df_result = pd.read_sql(query, conn)
    conn.close()
    st.dataframe(df_result)
