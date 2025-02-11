import pandas as pd

def load_csv(filepath):
    """Carrega um arquivo CSV e retorna um DataFrame do pandas"""
    return pd.read_csv(filepath)

def download_data(df):
    """Adiciona botão para baixar os dados filtrados no formato CSV"""
    import streamlit as st
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Baixar dados filtrados",
        data=csv,
        file_name="globe_data_filtered.csv",
        mime="text/csv",
    )
