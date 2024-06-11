import streamlit as st
import pandas as pd

st.title("Caricamento File CSV/XLSX")

uploaded_file = st.file_uploader("Scegli un file CSV o XLSX", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Verifica l'estensione del file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.success("File CSV caricato con successo!")
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
        st.success("File XLSX caricato con successo!")
    else:
        st.error("Formato file non supportato!")

    st.dataframe(df)