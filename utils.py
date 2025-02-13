import os
import json
import pandas as pd
import streamlit as st
from io import BytesIO  # Import necessário para manipulação do Excel

# Caminho dinâmico para o JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "extracted_reports.json")

def load_json():
    """Carrega o arquivo JSON corretamente e converte para DataFrame"""
    if not os.path.exists(DATA_FILE):
        st.error(f"Erro: Arquivo {DATA_FILE} não encontrado!")
        print(f"Erro: Arquivo {DATA_FILE} não encontrado!")  # Mensagem no terminal
        return pd.DataFrame()  # Retorna um DataFrame vazio para evitar falhas

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Garantir que todas as colunas esperadas existam
    expected_columns = ["Title", "Organization", "Country", "Students", "Protocols", "Date Submitted", "Link"]
    for col in expected_columns:
        if col not in df.columns:
            df[col] = "Não informado"  # Preenche colunas ausentes

    return df.fillna("Não informado")  # Substitui valores ausentes por "Não informado"

def download_data(df):
    """Adiciona botões para baixar os dados filtrados em JSON, CSV e Excel"""

    # **Download JSON**
    json_data = df.to_json(orient="records", force_ascii=False, indent=4).encode("utf-8")
    st.download_button(label="📥 Baixar dados filtrados (JSON)",
                       data=json_data,
                       file_name="globe_data_filtered.json",
                       mime="application/json")

    # **Download CSV**
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(label="📥 Baixar dados filtrados (CSV)",
                       data=csv_data,
                       file_name="globe_data_filtered.csv",
                       mime="text/csv")

    # **Download Excel**
    output = BytesIO()  # Criar buffer para armazenar o arquivo Excel
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    
    output.seek(0)  # Retornar ao início do buffer

    st.download_button(label="📥 Baixar dados filtrados (Excel)",
                       data=output,
                       file_name="globe_data_filtered.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")