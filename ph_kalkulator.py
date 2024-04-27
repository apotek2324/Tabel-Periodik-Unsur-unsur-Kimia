import streamlit as st

Kategori_Larutan = st.selectbox(
    "Pilih kategori larutan",
    ("Asam Kuat dan Basa Kuat","Konsentrasi Basa","Massa dan Volume Asam","Massa dan Volume Basa"),
    index=None,
    placeholder="Pilih kategori larutan...",)
st.write('Anda memilih:', Kategori_Larutan)

senyawa_asam_kuat = st.selectbox(
    "Masukkan senyawa asam",
    ("Asam Nitrat-HNO3","Asam Klorida-HCl","Asam Sulfat-H2SO4","Asam Iodida-HI","Asam Flourida-HF"),
    index=None,
    placeholder="Pilih senyawa...",)
st.write('Anda memilih:', senyawa_asam_kuat)

senyawa_basa_kuat = st.selectbox(
    "Masukkan senyawa basa",
    ("Kalium Hidroksida-KOH","Natrium Hidroksida-NaOH","Litium Hidroksida-LiOH","Kalsium Hidroksida-Ca(OH)2"),
    index=None,
    placeholder="Pilih senyawa...",)
st.write('Anda memilih:', senyawa_basa_kuat)

Masukkan_Konsentrasi = st.text_input('Masukkan Konsentrasi')
