import streamlit as st
import math

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Konsentrasi')
st.write("Konsentrasi = ", konsentrasi)
valensi = st.number_input('Masukkan Valensi')
st.write("Valensi = ", valensi)
hitung = st.button('Hitung pH')

if hitung:
    asam = konsentrasi * valensi
    st.write('Hasil = ', asam)
    st.success(f'Hasil = {asam}')
    st.write('log(fabs(x), base) is', math.log(math.fabs(asam),10))
    st.write('Hasil = ', pH)



    

