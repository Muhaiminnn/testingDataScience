import streamlit as st

def main():
    st.title("Aplikasi Streamlit dengan Ngrok")

    # Tambahkan elemen-elemen Streamlit
    nim = st.text_input("Masukkan NIM:", "Default")
    if nim == "200205501009":
        nama_pengguna = "Muhaimin"
    st.write(f'Selamat Seminar Proposal, {nama_pengguna}!')

if __name__ == '__main__':
    main()
