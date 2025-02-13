import streamlit as st
import pandas as pd
import json
import os

# Caminho dinâmico para o JSON
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "data", "extracted_reports.json")

# Função para carregar o JSON corretamente
def load_json():
    """Carrega o arquivo JSON corretamente e converte para DataFrame"""
    if not os.path.exists(DATA_FILE):
        st.error(f"❌ Erro: Arquivo {DATA_FILE} não encontrado!")
        return pd.DataFrame()  # Retorna um DataFrame vazio para evitar falhas

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Converter para DataFrame e garantir que todas as colunas existam
    df = pd.DataFrame(data)

    # Garantir que 'Country' e outros campos críticos não tenham valores ausentes
    for col in ["Country", "Protocols", "Grade Level", "Report Type(s)", "Date Submitted"]:
        df[col] = df.get(col, "Não informado").fillna("Não informado")

    return df

def sidebar_filters(df):
    """Configura os filtros da barra lateral"""
    st.sidebar.header("Filtros")

    selected_organization = st.sidebar.selectbox(
        "Filtrar por Organização", ["Todos"] + sorted(df["Organization"].dropna().unique())
    )

    selected_country = st.sidebar.selectbox(
        "Filtrar por País", ["Todos"] + sorted(df["Country"].unique())  # Agora inclui "Não informado"
    )

    protocol_list = set(", ".join(df["Protocols"]).split(", "))
    selected_protocol = st.sidebar.selectbox("Filtrar por Protocolo", ["Todos"] + sorted(protocol_list))

    grade_levels = set(df["Grade Level"].unique())
    selected_grade = st.sidebar.selectbox("Filtrar por Nível de Ensino", ["Todos"] + sorted(grade_levels))

    report_types = set(df["Report Type(s)"].unique())
    selected_report_type = st.sidebar.selectbox("Filtrar por Tipo de Relatório", ["Todos"] + sorted(report_types))

    date_years = set([str(x).split("/")[-1] for x in df["Date Submitted"] if x != "Não informado"])
    selected_year = st.sidebar.selectbox("Filtrar por Ano", ["Todos"] + sorted(date_years))

    return selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year

def apply_filters(df, selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year):
    """Aplica os filtros selecionados ao DataFrame"""
    filtered_df = df.copy()

    if selected_organization != "Todos":
        filtered_df = filtered_df[filtered_df["Organization"] == selected_organization]

    if selected_country != "Todos":
        filtered_df = filtered_df[filtered_df["Country"] == selected_country]

    if selected_protocol != "Todos":
        filtered_df = filtered_df[filtered_df["Protocols"].str.contains(selected_protocol, na=False)]

    if selected_grade != "Todos":
        filtered_df = filtered_df[filtered_df["Grade Level"] == selected_grade]

    if selected_report_type != "Todos":
        filtered_df = filtered_df[filtered_df["Report Type(s)"] == selected_report_type]

    if selected_year != "Todos":
        filtered_df = filtered_df[filtered_df["Date Submitted"].str.endswith(selected_year)]

    return filtered_df
