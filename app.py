import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st

def beranda():
    st.title("Aplikasi Streamlit dengan Sidebar Permanen - Beranda")
    st.write("Selamat datang di halaman beranda!")
    if st.button("Pergi ke Bagian Pertama"):
        st.session_state.halaman = "Bagian Pertama"

def bagian_pertama():
    st.title("Aplikasi Streamlit dengan Sidebar Permanen - Bagian Pertama")
    st.write("Anda berada di bagian pertama.")
    if st.button("Pergi ke Bagian Kedua"):
        st.session_state.halaman = "Bagian Kedua"

def bagian_kedua():
    st.title("Aplikasi Streamlit dengan Sidebar Permanen - Bagian Kedua")
    st.write("Anda berada di bagian kedua.")
    if st.button("Kembali ke Beranda"):
        st.session_state.halaman = "Beranda"

def main():
    st.set_page_config(page_title="Sidebar Permanen", page_icon=":house:", layout="wide")

    st.sidebar.title("Navigasi")

    if "halaman" not in st.session_state:
        st.session_state.halaman = "Beranda"

    halaman = {"Beranda": beranda, "Bagian Pertama": bagian_pertama, "Bagian Kedua": bagian_kedua}

    st.sidebar.write("Pilih halaman:")
    halaman_terpilih = st.sidebar.radio("", list(halaman.keys()))

    if st.session_state.halaman != halaman_terpilih:
        st.session_state.halaman = halaman_terpilih
        
    halaman[st.session_state.halaman]()

if __name__ == "__main__":
    main()
