import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st

def beranda():
    st.title("Mini Project Kalla - Prediksi Minyak Dunia")
    st.write("Task Mini Project:")

def bagian_pertama():
    st.title("Mini Project Kalla - Prediksi Minyak Dunia")
    st.write("Eksplorasi dan Analisis Data")
    st.write("Muhaimin - Universitas Negeri Makassar")
    st.write("14 Januari 2023")

def bagian_kedua():
    st.title("Mini Project Kalla - Prediksi Minyak Dunia")
    st.write("Analisis Time Series - ARIMA")

def main():
    st.set_page_config(page_title="Sidebar Permanen", page_icon=":house:", layout="wide")

    st.sidebar.title("Navigasi")

    if "halaman" not in st.session_state:
        st.session_state.halaman = "Beranda"

    halaman = {"First Page": beranda, "About Data": bagian_pertama, "Analisis": bagian_kedua}

    st.sidebar.write("Pilih halaman:")
    halaman_terpilih = st.sidebar.radio("", list(halaman.keys()))

    if st.session_state.halaman != halaman_terpilih:
        st.session_state.halaman = halaman_terpilih

    halaman[st.session_state.halaman]()

    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                width: 200px;
                background-color: #44c944;
                padding: 20px;
                position: fixed;
                height: 100%;
                overflow-y: auto;
            }
            .main {
                margin-left: 25px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
if __name__ == "__main__":
    main()
