import streamlit as st

st.title('Kalkulator pH Larutan')

Masukkan_Konsentrasi = st.text_input('Masukkan Konsentrasi')
Masukkan_Valensi = st.text_input('Masukkan Valensi')
hitung = st.button('Hitung pH')

if hitung:
    H = konsentrasi * valensi



    

