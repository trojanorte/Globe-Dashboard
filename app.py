import streamlit as st

# ✅ `set_page_config()` deve ser o primeiro comando do Streamlit
st.set_page_config(page_title="GLOBE Research Dashboard", layout="wide")

import filters 
import stats 
import utils

# Título da aplicação
st.title("🌍 GLOBE Research Dashboard")

# Carregar os dados do JSON
df = utils.load_json()

# Filtros laterais
selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year = filters.sidebar_filters(df)

# Aplicar filtros
filtered_df = filters.apply_filters(df, selected_organization, selected_country, selected_protocol, selected_grade, selected_report_type, selected_year)

# Exibir Tabela
st.subheader("📜 Trabalhos Submetidos")
st.dataframe(filtered_df[["Title", "Country", "Students", "Protocols", "Date Submitted", "View Research Report"]])

# Exibir detalhes do trabalho selecionado
stats.show_details(filtered_df)

# Estatísticas
stats.show_statistics(filtered_df)

# **Botões para baixar os dados**
st.subheader("📥 Exportar Dados")
utils.download_data(filtered_df)
