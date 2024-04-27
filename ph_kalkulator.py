import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar:
    selected = option_menu("Perhitungan pH Larutan", ['Menghitung dengan Konsentrasi', 'Menghitung dengan Massa dan Volume'], 
    default_index=1)
    selected

# halaman perhitungan pH
if (selected == 'Menghitung dengan Konsentrasi') :
    st.title('Kalkulator pH Larutan')
    
    senyawa_asam_kuat = st.selectbox(
    "Masukkan senyawa",
    ("Asam Nitrat-HNO3","Asam Klorida-HCl","Asam Sulfat-H2SO4","Asam Iodida-HI","Asam Flourida-HF"),
    index=None,
    placeholder="Pilih senyawa...",)
    st.write('Anda memilih:', senyawa_asam_kuat)


    

