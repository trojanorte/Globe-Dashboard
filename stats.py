import streamlit as st
import plotly.express as px
import pandas as pd
import json

# Carregar os dados JSON
with open("extracted_reports.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Converter para DataFrame
df = pd.DataFrame(data)

def show_details(filtered_df):
    """Exibe detalhes do trabalho selecionado"""
    st.subheader("📖 Detalhes do Trabalho")
    
    if filtered_df.empty:
        st.warning("Nenhum trabalho disponível para exibir detalhes.")
        return

    selected_title = st.selectbox("Escolha um trabalho para ver detalhes", filtered_df["Title"])

    selected_data = filtered_df[filtered_df["Title"] == selected_title].iloc[0]

    st.write(f"**Título:** {selected_data['Title']}")
    st.write(f"**Organização:** {selected_data.get('Organization', 'Não informado')}")
    st.write(f"**País:** {selected_data.get('Country', 'Não informado')}")
    st.write(f"**Estudantes:** {selected_data.get('Students', 'Não informado')}")
    st.write(f"**Nível Escolar:** {selected_data.get('Grade Level', 'Não informado')}")
    st.write(f"**Educador GLOBE:** {selected_data.get('GLOBE Educator(s)', 'Não informado')}")
    st.write(f"**Colaboradores:** {selected_data.get('Contributors', 'Não informado')}")
    st.write(f"**Tipo de Relatório:** {selected_data.get('Report Type(s)', 'Não informado')}")
    st.write(f"**Protocolos Utilizados:** {selected_data.get('Protocols', 'Não informado')}")
    st.write(f"**Data de Submissão:** {selected_data.get('Date Submitted', 'Não informado')}")
    
    # Adiciona link para visualizar o relatório completo
    st.write(f"**Relatório Completo:** [Acessar]({selected_data['Link']})")
    
    # Adiciona link para visualizar o pôster, se disponível
    if "Presentation Poster" in selected_data and selected_data["Presentation Poster"] != "N/A":
        st.write(f"**Pôster de Apresentação:** [Ver Pôster]({selected_data['Presentation Poster']})")

def show_statistics(filtered_df):
    """Mostra gráficos estatísticos"""
    st.subheader("📊 Estatísticas")

    if filtered_df.empty:
        st.warning("Nenhum dado disponível para exibir estatísticas.")
        return

    # Distribuição de Protocolos de Pesquisa
    protocol_counts = filtered_df["Protocols"].str.split(", ").explode().value_counts()
    
    if not protocol_counts.empty:
        fig = px.bar(
            protocol_counts, 
            x=protocol_counts.index, 
            y=protocol_counts.values, 
            title="Distribuição dos Protocolos de Pesquisa",
            labels={'x': 'Protocolos', 'y': 'Quantidade'},
            text_auto=True
        )
        st.plotly_chart(fig)
    else:
        st.warning("Nenhuma estatística disponível para protocolos.")

    # Distribuição por País
    country_counts = filtered_df["Country"].value_counts()
    
    if not country_counts.empty:
        fig = px.pie(
            names=country_counts.index, 
            values=country_counts.values, 
            title="Distribuição de Trabalhos por País"
        )
        st.plotly_chart(fig)
    else:
        st.warning("Nenhuma estatística disponível para países.")

    # Distribuição por Ano de Submissão
    filtered_df["Year Submitted"] = filtered_df["Date Submitted"].str.extract(r'(\d{4})')
    year_counts = filtered_df["Year Submitted"].value_counts().sort_index()

    if not year_counts.empty:
        fig = px.line(
            x=year_counts.index, 
            y=year_counts.values, 
            title="Evolução do Número de Trabalhos ao Longo dos Anos",
            labels={'x': 'Ano', 'y': 'Quantidade de Trabalhos'}
        )
        st.plotly_chart(fig)
    else:
        st.warning("Nenhuma estatística disponível para os anos de submissão.")
