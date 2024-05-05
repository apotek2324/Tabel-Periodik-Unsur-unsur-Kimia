import streamlit as st
import math

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Konsentrasi',)
st.write("Konsentrasi = ", konsentrasi)
valensi = st.number_input('Masukkan Valensi', 0)
st.write("a = ", valensi)
hitung = st.button('Hitung pH')

if hitung:
    asam = konsentrasi * valensi
    st.write('[H+] = ', asam)
    log = math.log10(asam)
    pH = log * -1
    st.write('pH = ', pH)
    st.success(f'pH Asam adalah {pH:.2f}')
