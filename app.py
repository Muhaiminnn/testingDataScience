import streamlit as st

def main():
    st.title("Aplikasi Streamlit dengan Ngrok")

    # Tambahkan elemen-elemen Streamlit
    nim = st.text_input("Masukkan NIM:")
    if nim == "200205501009":
        nama_pengguna = "Muhaimin"
        st.write(f'Selamat Seminar Proposal, {nama_pengguna}!')
        gambar_lokal = 'bah sod.jpg'
        st.image(gambar_lokal, caption='Korban Tumbuk Dada', use_column_width=True)
    elif nim == "":
        st.write(f'Masukin NIM dulu lah kocak!')
    else:
        st.write(f'Lah kamu ga diajak...')

if __name__ == '__main__':
    main()
