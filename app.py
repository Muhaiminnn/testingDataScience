import streamlit as st

def main():
    st.title("Aplikasi Streamlit dengan Ngrok")

    # Tambahkan elemen-elemen Streamlit
    nim = st.text_input("Masukkan NIM:")
    if nim == "200205501009":
        nama_pengguna = "Muhaimin"
    elif nim == "":
        st.write(f'Masukin NIM dulu lah kocak!')
    else:
        st.write(f'Lah kamu ga diajak...')
    st.write(f'Selamat Seminar Proposal, {nama_pengguna}!')

if __name__ == '__main__':
    main()
