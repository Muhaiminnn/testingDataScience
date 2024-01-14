import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st

# -- Import File --
file = "dailybrentoil.csv"

df_daily = pd.read_csv(file)
df_daily = df_daily.iloc[:, :-3]
df_plt = df_daily[['Date', 'Close']].copy()
# -- -- --

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
    st.write("Preview Data")
    st.dataframe(df_daily.head(6))
    st.write("Info Data")
    st.dataframe(df_daily.describe())

    df_daily[['tanggal','jam']] = df_daily['Date'].str.split(' ',expand = True)
    df_daily.drop("Date",inplace = True, axis = 1)
    
    column_a = df_daily['tanggal']
    column_b = df_daily['Close']

    array_a = column_a.to_numpy()
    array_b = column_b.to_numpy()

    df_plt['Date'] = array_a
    df_plt['Close'] = array_b
    
    df_daily['tanggal'] = pd.to_datetime(df_daily['tanggal'], format='%Y-%m-%d')
    plt.figure(figsize=(10, 6))
    plt.plot(df_daily['tanggal'], df_daily['Close'], label='Close Price')
    plt.title('Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()
    st.pyplot(plt)
    

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
