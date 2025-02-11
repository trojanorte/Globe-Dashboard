import streamlit as st
import plotly.express as px

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
    st.write(f"**País:** {selected_data['Country']}")
    st.write(f"**Estudantes:** {selected_data['Students']}")
    st.write(f"**Protocolos Utilizados:** {selected_data['Protocols']}")
    st.write(f"**Data de Submissão:** {selected_data['Date Submitted']}")
    st.write(f"**Link:** [Acessar relatório]({selected_data['Link']})")

def show_statistics(filtered_df):
    """Mostra gráficos estatísticos"""
    st.subheader("📊 Estatísticas")

    if filtered_df.empty:
        st.warning("Nenhum dado disponível para exibir estatísticas.")
        return

    protocol_counts = filtered_df["Protocols"].str.split(", ").explode().value_counts()
    
    if not protocol_counts.empty:
        fig = px.bar(protocol_counts, x=protocol_counts.index, y=protocol_counts.values, title="Distribuição dos Protocolos de Pesquisa")
        st.plotly_chart(fig)
    else:
        st.warning("Nenhuma estatística disponível para protocolos.")
