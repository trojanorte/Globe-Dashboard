# 🌍 GLOBE Research Dashboard

Este é um **dashboard interativo** desenvolvido com **Streamlit** para visualizar e analisar pesquisas submetidas ao programa **GLOBE**. Ele permite filtrar, visualizar estatísticas e explorar os trabalhos submetidos por estudantes ao redor do mundo.

## 📌 Funcionalidades
✅ **Filtrar pesquisas** por país, protocolo, idioma e ano
✅ **Visualizar detalhes completos** de cada pesquisa
✅ **Explorar estatísticas interativas** sobre protocolos utilizados
✅ **Baixar os dados filtrados** em formato JCSV ou CSV ou Excel

## 🏗 Estrutura do Projeto
```
globe_dashboard/
│── app.py  # Arquivo principal do Streamlit
│── data/
│   ├── extracted_data.json  # Dados das pesquisas
│── modules/
│   ├── filters.py  # Lógica para filtragem de dados
│   ├── stats.py  # Funções para análises estatísticas
│   ├── utils.py  # Funções auxiliares
│── requirements.txt  # Dependências do projeto
│── README.md  # Documentação do projeto
```

## 🚀 Como Executar
1. Clone o repositório ou copie os arquivos.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o Streamlit:
   ```bash
   streamlit run app.py
   ```

## 📂 Dependências
As bibliotecas utilizadas no projeto são:
- `streamlit`
- `pandas`
- `plotly`
- `numpy`
- `selenium` (para extração de dados)

## 📤 Exportação de Dados
Os dados filtrados podem ser exportados diretamente pelo dashboard em JSON ou CSV para maior flexibilidade.

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo!
