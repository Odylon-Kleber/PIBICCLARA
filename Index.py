import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl


pg = st.navigation([
    st.Page("Pages/Dadosdoprojeto.py", title="Dados do projeto"),
    st.Page("Pages/Analisequalitativa.py", title="Análise qualitativa"),
    st.Page("Pages/Analisequantitativa.py", title="Análise quantitativa"),
    st.Page("Pages/Conclusão.py", title="Conclusão"),
])

pg.run()

