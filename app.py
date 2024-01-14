import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st

def beranda():
    st.title("Mini Project Kalla - Prediksi Minyak Dunia")
    st.write("Muhaimin - Universitas Negeri Makassar")
    st.write("14 Januari 2023")
    st.write("Task Mini Project:")
    st.write("Hasil pengerjaan bisa diliat pada Navigasi bagian kiri")
    st.image("GambarTask.jpg", caption="Sebagai Pemenuhan Kualifikasi Posisi Data Scientist di Kalla")

def bagian_pertama():
    st.title("Mini Project Kalla - Prediksi Minyak Dunia")
    st.write("Eksplorasi dan Analisis Data")
    

def bagian_kedua():
    st.title("Mini Project Kalla - Prediksi Minyak Dunia")
    st.write("Analisis Time Series - ARIMA")

def main():
    st.set_page_config(page_title="Sidebar Permanen", page_icon=":house:", layout="wide")

    st.sidebar.title("Navigasi")

    if "halaman" not in st.session_state:
        st.session_state.halaman = "First"

    halaman = {"First": beranda, "About Data": bagian_pertama, "Analisis": bagian_kedua}

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
