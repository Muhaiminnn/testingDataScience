import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st
import pandas as pd
data = pd.read_csv('dailybrentoil.csv')

def main():
    st.title("Prediksi Harga Minyak Dunia By Muhaimin\n Mini Project Data Scientist Kalla")
    st.table(data)

if __name__ == '__main__':
    main()
