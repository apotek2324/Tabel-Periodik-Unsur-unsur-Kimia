import streamlit as st
import math

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Konsentrasi')
st.write("Konsentrasi = ", konsentrasi)
valensi = st.number_input('Masukkan Valensi', 0)
st.write("Valensi = ", valensi)
hitung = st.button('Hitung pH')

if hitung:
    basa = konsentrasi * valensi
    st.write('[OH-] = ', basa)
    log = math.log10(basa)
    pOH = log * -1
    pH = 14-pOH
    st.write('pOH = ', pOH)
    st.success(f'pH Basa adalah {pH:.2f}')

   

