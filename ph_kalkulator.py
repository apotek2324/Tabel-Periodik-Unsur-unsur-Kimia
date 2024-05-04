import streamlit as st
import math

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Konsentrasi')
st.write("Konsentrasi = ", konsentrasi)
valensi = st.number_input('Masukkan Valensi', 0)
st.write("Valensi = ", valensi)
hitung = st.button('Hitung pH')

if hitung:
    asam = konsentrasi * valensi
    st.write('Hasil = ', asam)
    log = math.log10(asam)
    pH = log * -1
    st.success(f'Hasil = {pH}')

   

