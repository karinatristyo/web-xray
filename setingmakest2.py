import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

# --- Setup database ---
conn = sqlite3.connect('database_pasien.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS pasien (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    umur INTEGER,
    kv REAL,
    ma REAL,
    sec REAL
)
''')
conn.commit()

# --- Initialize session state ---
if "page" not in st.session_state:
    st.session_state.page = "Input Data"

def navigate_to(page):
    st.session_state.page = page

# --- Sidebar menu ---
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Input Data", "Data Pasien"],
        icons=["clipboard-data", "table"],
        menu_icon="cast",
        default_index=0 if st.session_state.page == "Input Data" else 1,
    )
    st.session_state.page = selected

# --- Halaman Input Data ---
if st.session_state.page == "Input Data":
    st.title("Input Data Pasien dan Pengaturan Eksposur")
    st.write("Isi informasi pasien dan atur pengaturan eksposur.")

    # Input data pasien
    st.subheader("Data Pasien")
    nama = st.text_input("Nama Pasien", placeholder="Masukkan nama lengkap")
    umur = st.number_input("Umur Pasien", min_value=0, max_value=120, step=1, placeholder="Masukkan umur pasien")

    # Pengaturan eksposur
    st.subheader("Pengaturan Eksposur")
    col1, col2, col3 = st.columns(3)
    with col1:
        kv = st.number_input("kV", value=100.0, min_value=0.0, max_value=150.0, step=0.1)
    with col2:
        ma = st.number_input("mA", value=81.0, min_value=0.0, max_value=500.0, step=0.1)
    with col3:
        sec = st.number_input("sec", value=1.0, min_value=0.0, max_value=10.0, step=0.1)

    # Tombol untuk expose
    if st.button("Expose"):
        if nama and umur > 0:
            cursor.execute('''
            INSERT INTO pasien (nama, umur, kv, ma, sec)
            VALUES (?, ?, ?, ?, ?)
            ''', (nama, umur, kv, ma, sec))
            conn.commit()
            st.success(f"Data pasien {nama} berhasil disimpan!")
            navigate_to("Data Pasien")
        else:
            st.error("Harap isi semua data dengan benar.")

# --- Halaman Data Pasien ---
if st.session_state.page == "Data Pasien":
    st.title("Data Pasien Tersimpan")
    st.write("Berikut adalah data pasien yang tersimpan di database.")

    # Ambil data dari database
    data = cursor.execute("SELECT * FROM pasien").fetchall()

    # Tampilkan data dalam tabel
    if data:
        st.table(data)
    else:
        st.info("Belum ada data pasien yang tersimpan.")

# --- CSS untuk mempercantik tampilan ---
st.markdown("""
    <style>
    .css-18e3th9 {
        padding-top: 2rem;
    }
    .css-1d391kg {
        text-align: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
