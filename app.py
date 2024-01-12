import streamlit as st

def main():
    st.title("Aplikasi Streamlit dengan Ngrok")

    # Tambahkan elemen-elemen Streamlit
    nama_pengguna = st.text_input("Masukkan Nama Pengguna:", "Default")
    st.write(f'Halo, {nama_pengguna}!')

if __name__ == '__main__':
    main()
