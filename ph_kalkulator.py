#asam kuat
import streamlit as st
import math

st.title('Kalkulator pH Larutan')

senyawa = st.selectbox(
    "Masukkan senyawa asam",
    ("Asam Nitrat-HNO3","Asam Klorida-HCl","Asam Sulfat-H2SO4"),
    index='1','1','2'
    placeholder="Pilih senyawa...",)

st.write('Anda memilih:', senyawa_asam_kuat)
konsentrasi = st.number_input('Masukkan Konsentrasi') 
st.write("Konsentrasi = ", konsentrasi)

hitung = st.button('Hitung pH')

if hitung:
    asam = konsentrasi * index
    st.write('[H+] = ', asam)
    log = math.log10(asam)
    pH = log * -1
    st.write('pH = ', pH)
    st.success(f'pH Asam adalah {pH:.2f}')
