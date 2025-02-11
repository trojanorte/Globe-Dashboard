import streamlit as st

def sidebar_filters(df):
    """Configura os filtros da barra lateral"""
    st.sidebar.header("Filtros")

    selected_country = st.sidebar.selectbox("Filtrar por país", ["Todos"] + sorted(df["Country"].dropna().unique()))

    protocol_list = set(", ".join(df["Protocols"].fillna("")).split(", "))
    selected_protocol = st.sidebar.selectbox("Filtrar por protocolo", ["Todos"] + sorted(protocol_list))

    date_years = set([str(x).split("/")[-1] for x in df["Date Submitted"].dropna()])
    selected_year = st.sidebar.selectbox("Filtrar por ano", ["Todos"] + sorted(date_years))

    return selected_country, selected_protocol, selected_year

def apply_filters(df, selected_country, selected_protocol, selected_year):
    """Aplica os filtros selecionados ao DataFrame"""
    filtered_df = df.copy()
    
    if selected_country != "Todos":
        filtered_df = filtered_df[filtered_df["Country"] == selected_country]

    if selected_protocol != "Todos":
        filtered_df = filtered_df[filtered_df["Protocols"].fillna("").str.contains(selected_protocol, na=False)]

    if selected_year != "Todos":
        filtered_df = filtered_df[filtered_df["Date Submitted"].str.endswith(selected_year)]

    return filtered_df
