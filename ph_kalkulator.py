import streamlit as st

st.title('Kalkulator pH Larutan')

your-repository/
├pages/
│   ├── Asam_Kuat_dan_Basa_Kuat.py
│   ├── Asam_Kuat_dan_Basa_Lemah.py
│   ├── Asam_Lemah_dan_Basa_Kuat.py
│   └── Asam_Lemah_dan_Basa_Lemah.py
└── Kalkulator_pH_Campuran.py

st.page_link("Kalkulator_pH_Campuran.py", label="Kalkulator pH", icon="🏠")
st.page_link("Asam_Kuat_dan_Basa_Kuat.py", label="Page 1", icon="1️⃣")
st.page_link("Asam_Kuat_dan_Basa_Lemah.py", label="Page 2", icon="2️⃣")
st.page_link("Asam_Lemah_dan_Basa_Kuat.py", label="Page 3", icon="🌎")
st.page_link("Asam_Lemah_dan_Basa_Lemah.py", label="Page 4", icon="p", disabled=True)
    
    

