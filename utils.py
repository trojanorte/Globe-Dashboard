import pandas as pd
import streamlit as st
import json

def load_json(filepath):
    """Carrega o arquivo JSON corretamente e converte para DataFrame"""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def download_data(df):
    """Adiciona botão para baixar os dados filtrados"""
    json_data = df.to_json(orient="records", force_ascii=False, indent=4).encode("utf-8")
    
    st.download_button(label="📥 Baixar dados filtrados (JSON)",
                       data=json_data,
                       file_name="globe_data_filtered.json",
                       mime="application/json")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(label="📥 Baixar dados filtrados (CSV)",
                       data=csv_data,
                       file_name="globe_data_filtered.csv",
                       mime="text/csv")
