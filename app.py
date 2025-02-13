import streamlit as st
import pandas as pd
import filters
import stats
import utils

# Configuração do Streamlit
st.set_page_config(page_title="GLOBE Research Dashboard", layout="wide")
st.title("🌍 GLOBE Research Dashboard")

# Carregar os dados do JSON
df = utils.load_json()

# Verifica se os dados foram carregados corretamente
if df.empty:
    st.error("Erro ao carregar os dados! Verifique se o arquivo JSON está no diretório correto.")
else:
    # Filtros laterais
    selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year = filters.sidebar_filters(df)

    # Aplicar filtros
    filtered_df = filters.apply_filters(df, selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year)

    # Exibir Tabela
    st.subheader("📜 Trabalhos Submetidos")
    st.dataframe(filtered_df[["Title", "Organization", "Country", "Students", "Protocols", "Date Submitted", "Link"]])

    # Exibir detalhes do trabalho selecionado
    stats.show_details(filtered_df)

    # Estatísticas
    stats.show_statistics(filtered_df)

    # Botão para baixar os dados filtrados
    utils.download_data(filtered_df)
