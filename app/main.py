
import pandas as pd
import sys
import os
import streamlit as st
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from processor import process

st.set_page_config(layout="wide")
st.title("Анализ риска госзакупок")

def highlight_risk(val):
    color = {
        'green': 'background-color: #d4edda; color: #155724',
        'yellow': 'background-color: #fff3cd; color: #856404',
        'orange': 'background-color: #ffeeba; color: #8a6d3b',
        'red': 'background-color: #f8d7da; color: #721c24'
    }.get(val, '')
    return color
if st.button("Запуск"):
    df = process()
    st.success("Завершено")

    styled_df = df[["item", "price", "supplier", "customer", "risk_level"]].style.apply(
        lambda x: [highlight_risk(v) for v in x], subset=["risk_level"]
    )
    
    st.dataframe(styled_df, use_container_width=True)
    st.bar_chart(df["risk_level"].value_counts())