import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl
import plotly


# Configurações da página
st.set_page_config(
    page_title="AnalisaMed",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.image(r"C:\Users\odylo\Desktop\PIBIC CLARA\imagem\logomarca.png", caption="AnalisaMed")
st.sidebar.write("Odylon Kleber Pereira de Souza")
st.sidebar.write("© 2026 AnalisaMed. Todos os direitos reservados.")

# Título do dashboard
st.markdown('# 📊 ANÁLISE DE DADOS')
st.header("Educação em saúde sexual e reprodutiva para adolescentes: diálogo entre a universidade e estudantes de escolas públicas de Marabá", text_alignment="justify")
st.header('Banco de dados')

dados_ANISIO = pd.read_excel("ANISIO.xlsx")
dados_ANISIO
df = dados_ANISIO