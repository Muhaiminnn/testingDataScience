import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st

def beranda():
    st.title("Aplikasi Streamlit dengan Sidebar Permanen - Beranda")

    st.write("Selamat datang di halaman beranda!")

def bagian_pertama():
    st.title("Aplikasi Streamlit dengan Sidebar Permanen - Bagian Pertama")

    st.write("Anda berada di bagian pertama.")

def bagian_kedua():
    st.title("Aplikasi Streamlit dengan Sidebar Permanen - Bagian Kedua")

    st.write("Anda berada di bagian kedua.")

def main():
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                width: 300px;
                background-color: #f4f4f4;
                padding: 20px;
                position: fixed;
                height: 100%;
                overflow-y: auto;
            }
            .main {
                margin-left: 320px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("Navigasi")

    if "halaman" not in st.session_state:
        st.session_state.halaman = "Beranda"

    halaman = {"Beranda": beranda, "Bagian Pertama": bagian_pertama, "Bagian Kedua": bagian_kedua}

    st.sidebar.radio("Pilih halaman", list(halaman.keys()))

    halaman[st.session_state.halaman]()

if __name__ == "__main__":
    main()
