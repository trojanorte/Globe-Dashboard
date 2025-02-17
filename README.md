# 🌍 GLOBE Research Dashboard

Este é um **dashboard interativo** desenvolvido com **Streamlit** para visualizar e analisar pesquisas submetidas ao programa **GLOBE**. Ele permite filtrar, visualizar estatísticas e explorar os trabalhos submetidos por estudantes ao redor do mundo.

---

## 📌 Funcionalidades
✅ **Filtrar pesquisas** por país, protocolo, idioma e ano  
✅ **Visualizar detalhes completos** de cada pesquisa  
✅ **Explorar estatísticas interativas** sobre protocolos utilizados  
✅ **Baixar os dados filtrados** em formato JSON, CSV ou Excel  

---

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

---

## ⚙️ Tecnologias e Habilidades Utilizadas
Este projeto foi desenvolvido aplicando habilidades avançadas de Engenharia de Produção e Ciência de Dados:

### 🖥️ Desenvolvimento
🚀 **Streamlit** → Construção de dashboards interativos  
🐍 **Python** → Programação e manipulação de dados  
🌐 **Selenium** → Automação de coleta de dados via Web Scraping  
🛠️ **Git/GitHub** → Controle de versão e colaboração  

### 📊 Análise de Dados
📊 **Pandas** → Manipulação e análise de dados tabulares  
🔢 **NumPy** → Operações matemáticas e estatísticas  
📈 **Plotly & Matplotlib** → Visualização interativa de dados  

### 🏗 Pesquisa Operacional e Otimização
📉 **Modelagem matemática** → Aplicação de algoritmos para estruturação de dados  
📊 **Tomada de Decisão Multicritério** → Suporte para análise de impacto  
🔄 **ETL (Extract, Transform, Load)** → Processamento e estruturação dos dados coletados  

---

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

---

## 📂 Dependências
As bibliotecas utilizadas no projeto são:
- `streamlit`
- `pandas`
- `plotly`
- `numpy`
- `selenium` (para extração de dados)

📤 **Exportação de Dados**  
Os dados podem ser exportados diretamente do dashboard nos seguintes formatos:
- 📄 CSV
- 📝 JSON
- 📊 Excel (XLSX)

---

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo!

**Criado por [Allyson Aires Pimentel da Silva]** 🚀

