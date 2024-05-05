#asam kuat
import streamlit as st
import math

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Konsentrasi')
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

#asam lemah
import streamlit as st
import math

st.title('Kalkulator pH Larutan')

konsentrasi = st.number_input('Masukkan Ka')
st.write("Ka = ", konsentrasi)
valensi = st.number_input('Masukkan Valensi', 0)
st.write("a = ", valensi)
hitung = st.button('Hitung pH')

if hitung:
    asam = konsentrasi * valensi
    akar = asam ** 0.5
    st.write('[H+] = ', akar)
    log = math.log10(akar)
    pH = log * -1
    st.write('pH = ', pH)
    st.success(f'pH Asam adalah {pH:.2f}')

#basa kuat
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

#basa lemah
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

   

