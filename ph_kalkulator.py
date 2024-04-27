import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = "Perhitungan pH Larutan", #required 
        options =["Menghitung dengan Konsentrasi", "Menghitung dengan Massa dan Volume"], #required 
    )

if (selected == "Menghitung dengan Konsentrasi") :
    st.title(f"Kalkulator pH Larutan {selected}")
if (selected == "Menghitung dengan Massa dan Volume") :
    st.title(f"Kalkulator Larutan {selected}")


    

