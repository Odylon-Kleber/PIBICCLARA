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