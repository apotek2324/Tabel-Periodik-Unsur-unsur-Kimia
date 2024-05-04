import streamlit as st

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Konsentrasi', 0)
valensi = st.number_input('Masukkan Valensi', 0)
hitung = st.button('Hitung pH')

if hitung:
    asam = konsentrasi * valensi
    st.write('Hasil = ', asam)
    st.success(f'Hasil = {asam}')
    pH = log10(asam)
    st.write('Hasil = ', pH)



    

