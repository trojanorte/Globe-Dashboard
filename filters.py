import streamlit as st
import pandas as pd

def sidebar_filters(df):
    """Configura os filtros da barra lateral"""
    st.sidebar.header("🔍 Filtros")

    # Filtro por Organização
    selected_organization = st.sidebar.selectbox(
        "Filtrar por Organização", 
        ["Todos"] + sorted(df["Organization"].dropna().unique())
    )

    # Filtro por País
    selected_country = st.sidebar.selectbox(
        "Filtrar por País", 
        ["Todos"] + sorted(df["Country"].dropna().unique())
    )

    # Filtro por Protocolo
    protocol_list = set(", ".join(df["Protocols"].fillna("")).split(", "))
    selected_protocol = st.sidebar.selectbox(
        "Filtrar por Protocolo", 
        ["Todos"] + sorted(protocol_list)
    )

    # Filtro por Nível de Ensino
    grade_levels = set(df["Grade Level"].dropna().unique())
    selected_grade = st.sidebar.selectbox(
        "Filtrar por Nível de Ensino", 
        ["Todos"] + sorted(grade_levels)
    )

    # Filtro por Tipo de Relatório
    report_types = set(df["Report Type(s)"].dropna().unique())
    selected_report_type = st.sidebar.selectbox(
        "Filtrar por Tipo de Relatório", 
        ["Todos"] + sorted(report_types)
    )

    # Filtro por Ano de Submissão
    date_years = set([str(x).split("/")[-1] for x in df["Date Submitted"].dropna()])
    selected_year = st.sidebar.selectbox(
        "Filtrar por Ano", 
        ["Todos"] + sorted(date_years)
    )

    return selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year

def apply_filters(df, selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year):
    """Aplica os filtros selecionados ao DataFrame"""
    filtered_df = df.copy()

    if selected_organization != "Todos":
        filtered_df = filtered_df[filtered_df["Organization"] == selected_organization]

    if selected_country != "Todos":
        filtered_df = filtered_df[filtered_df["Country"] == selected_country]

    if selected_protocol != "Todos":
        filtered_df = filtered_df[filtered_df["Protocols"].fillna("").str.contains(selected_protocol, na=False)]

    if selected_grade != "Todos":
        filtered_df = filtered_df[filtered_df["Grade Level"] == selected_grade]

    if selected_report_type != "Todos":
        filtered_df = filtered_df[filtered_df["Report Type(s)"] == selected_report_type]

    if selected_year != "Todos":
        filtered_df = filtered_df[filtered_df["Date Submitted"].str.endswith(selected_year)]

    return filtered_df
