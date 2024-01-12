import streamlit as st

def main():
    st.title("Seputar Sempro!")

    # Tambahkan elemen-elemen Streamlit
    nim = st.text_input("Masukkan NIM:")
    if nim == "200205501009":
        nama_pengguna = "Muhaimin"
        st.write(f'Selamat Seminar Proposal, {nama_pengguna}!')
        gambar_lokal = 'bah sod.jpg'
        st.image(gambar_lokal, caption='Korban Tumbuk Dada', use_column_width=True)
    elif nim == "200205502002":
        nama_pengguna = "Yusraul Fitrah"
        st.write(f'Sudah mki kita {nama_pengguna}, tapi semangatki jalani proses. Dan tunggui teman satu dosen PA ta kodong.')
        #gambar_lokal = 'bah sod.jpg'
        #st.image(gambar_lokal, caption='Korban Tumbuk Dada', use_column_width=True)
    elif nim == "200205501004":
        nama_pengguna = "Hasril"
        st.write(f'Baru-baru sudah {nama_pengguna} sempro nah, nah kita mi itu paling lancar bimbingan.')
        #gambar_lokal = 'bah sod.jpg'
        #st.image(gambar_lokal, caption='Korban Tumbuk Dada', use_column_width=True)
    elif nim == "200205502015":
        nama_pengguna = "Muhammad Ikram"
        st.write(f'Ededeh apaji kau {nama_pengguna}, kah lamami kau sudah.')
        #gambar_lokal = 'bah sod.jpg'
        #st.image(gambar_lokal, caption='Korban Tumbuk Dada', use_column_width=True)
    elif nim == "200205500002":
        nama_pengguna = "Yaya Ferida"
        st.write(f'wiss nih {nama_pengguna} nih boss *Ferdian, lekbak tongmi tawwa')
        #gambar_lokal = 'bah sod.jpg'
        #st.image(gambar_lokal, caption='Korban Tumbuk Dada', use_column_width=True)
    elif nim == "":
        st.write(f'Masukin NIM dulu lah kocak!')
    else:
        st.write(f'Lah kamu ga diajak...')

if __name__ == '__main__':
    main()
