import streamlit as st

st.title('Kalkulator pH Larutan')

konsentrasi = st.text_input('Masukkan Konsentrasi', 0)
valensi = st.text_input('Masukkan Valensi', 0)
hitung = st.button('Hitung pH')

if hitung:
    H = konsentrasi * valensi
    st.write('Hasil = ', H)
    st.success(f'Hasil = {H}')



    

