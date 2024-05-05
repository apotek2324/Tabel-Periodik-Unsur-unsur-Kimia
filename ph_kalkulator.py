import streamlit as st
import math

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Ka')
st.write("Ka = ", konsentrasi)
valensi = st.number_input('Masukkan Valensi', 0)
st.write("a = ", valensi)
hitung = st.button('Hitung pH')

if hitung:
    basa = konsentrasi * valensi
    akar = basa ** 0.5
    st.write('[OH-] = ', akar)
    log = math.log10(akar)
    pOH = log * -1
    pH = 14-pOH
    st.write('pOH = ', pOH)
    st.success(f'pH Basa adalah {pH:.2f}')

   

