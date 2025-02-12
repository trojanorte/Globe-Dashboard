import pandas as pd
import streamlit as st

def load_csv(filepath):
    """Carrega o arquivo CSV corretamente"""
    return pd.read_csv(filepath, encoding="utf-8")

def download_data(df):
    """Adiciona botão para baixar os dados filtrados"""
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(label="📥 Baixar dados filtrados",
                       data=csv,
                       file_name="globe_data_filtered.csv",
                       mime="text/csv")
